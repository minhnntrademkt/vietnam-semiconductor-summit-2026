# ==============================================================================
# PRODUCTION DEPLOY SCRIPT (STRICT ZERO-LEAKAGE WHITELIST)
# Target: vietnam-semiconductor-summit-2026.marvell.com
# Server: 103.130.217.103 (cPanel / LiteSpeed)
# Rule: CHỈ DEPLOY NHỮNG FILE CẦN THIẾT CHO RUNTIME WEBSITE.
#       NGHIÊM CẤM TẤT CẢ FILE LÀM VIỆC (.md, .py, .gs, .ps1, raw_speakers...)
# ==============================================================================

$credFile = Join-Path $PSScriptRoot "ftp_credentials.local.ps1"
if (Test-Path $credFile) {
    . $credFile
} else {
    Write-Error "FTP credentials file not found!"
    exit 1
}

$wc = New-Object System.Net.WebClient
$wc.Credentials = New-Object System.Net.NetworkCredential($global:FTP_USER, $global:FTP_PASS)
$cred = New-Object System.Net.NetworkCredential($global:FTP_USER, $global:FTP_PASS)

function Ensure-FtpDirectory($ftpUrl) {
    try {
        $req = [System.Net.FtpWebRequest]::Create($ftpUrl)
        $req.Method = [System.Net.WebRequestMethods+Ftp]::MakeDirectory
        $req.Credentials = $cred
        $resp = $req.GetResponse()
        $resp.Close()
    } catch {
        # Directory might already exist
    }
}

function Upload-FtpFile($ftpUrl, $localPath) {
    if (-not (Test-Path $localPath)) {
        Write-Warning "Local file not found, skipping: $localPath"
        return
    }
    
    # Security Gate: Double check file extension
    $ext = [System.IO.Path]::GetExtension($localPath).ToLower()
    $forbiddenExts = @(".md", ".py", ".pyc", ".gs", ".ps1", ".sh", ".bat", ".cmd", ".env", ".bak", ".log", ".jsonl")
    if ($ext -in $forbiddenExts) {
        Write-Error "SECURITY VIOLATION: Attempted to upload forbidden file $localPath. Upload aborted!"
        exit 1
    }

    try {
        Write-Output "Uploading: $(Split-Path $localPath -Leaf) -> $ftpUrl"
        $wc.UploadFile($ftpUrl, $localPath)
        Write-Output "Success: $(Split-Path $localPath -Leaf)"
    } catch {
        Write-Warning "Failed to upload $localPath : $_"
    }
}

$remoteDomain = "vietnam-semiconductor-summit-2026.marvell.com"
$ftpBase = "ftp://$($global:FTP_HOST)/$remoteDomain"
$localBase = $PSScriptRoot

Write-Output "=== 1. ENSURING RUNTIME DIRECTORIES ON FTP ==="
Ensure-FtpDirectory $ftpBase
Ensure-FtpDirectory "$ftpBase/images"
Ensure-FtpDirectory "$ftpBase/images/speakers"
Ensure-FtpDirectory "$ftpBase/images/partners"

Write-Output "`n=== 2. UPLOADING CORE WEB RUNTIME ASSETS (WHITELIST ONLY) ==="
$rootWhitelist = @(
    "index.html",
    "styles.css",
    "app.js",
    "agenda.html",
    "agenda.json",
    "favicon.svg",
    "marvell-logo.svg",
    ".htaccess"
)

foreach ($f in $rootWhitelist) {
    $localFile = Join-Path $localBase $f
    if (Test-Path $localFile) {
        Upload-FtpFile "$ftpBase/$f" $localFile
    } else {
        Write-Warning "Missing core file: $f"
    }
}

Write-Output "`n=== 3. UPLOADING PRODUCTION IMAGES (WHITELIST ONLY) ==="
# 3.1 Banner images in root images/
$bannerWhitelist = @(
    "hero-marvell-chip.jpg",
    "marvell-plenary-chip.jpg",
    "marvell-logo-black.png",
    "og-banner.jpg"
)

foreach ($b in $bannerWhitelist) {
    $localFile = Join-Path $localBase "images\$b"
    if (Test-Path $localFile) {
        Upload-FtpFile "$ftpBase/images/$b" $localFile
    }
}

# 3.2 Approved Speaker portraits
$speakerFiles = Get-ChildItem -Path (Join-Path $localBase "images\speakers") -File | Where-Object {
    $_.Extension.ToLower() -in @(".jpg", ".jpeg", ".png", ".webp")
}
foreach ($s in $speakerFiles) {
    Upload-FtpFile "$ftpBase/images/speakers/$($s.Name)" $s.FullName
}

# 3.3 Approved Partner logos
$partnerFiles = Get-ChildItem -Path (Join-Path $localBase "images\partners") -File | Where-Object {
    $_.Extension.ToLower() -in @(".svg", ".png", ".jpg")
}
foreach ($p in $partnerFiles) {
    Upload-FtpFile "$ftpBase/images/partners/$($p.Name)" $p.FullName
}

Write-Output "`n=== 4. RUNNING HEALTH CHECK ==="
$testUrls = @(
    "https://$remoteDomain/",
    "https://$remoteDomain/styles.css",
    "https://$remoteDomain/app.js",
    "https://$remoteDomain/agenda.json",
    "https://$remoteDomain/favicon.svg"
)

foreach ($u in $testUrls) {
    try {
        $res = Invoke-WebRequest -Uri $u -UseBasicParsing -TimeoutSec 10
        if ($res.StatusCode -eq 200) {
            Write-Output "[PASS 200 OK] $u"
        } else {
            Write-Warning "[WARN $($res.StatusCode)] $u"
        }
    } catch {
        Write-Warning "[CHECK] $u : $_"
    }
}

Write-Output "`n=== ZERO-LEAKAGE DEPLOYMENT COMPLETE ==="

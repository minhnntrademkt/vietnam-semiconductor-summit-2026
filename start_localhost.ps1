# PowerShell Simple Local Static File Web Server with Automatic Live-Reload (Ctrl+F5)
param (
    [int]$Port = 8080,
    [string]$Path = $PSScriptRoot
)

$mimeTypes = @{
    ".html" = "text/html; charset=utf-8"
    ".htm"  = "text/html; charset=utf-8"
    ".css"  = "text/css; charset=utf-8"
    ".js"   = "application/javascript; charset=utf-8"
    ".json" = "application/json; charset=utf-8"
    ".png"  = "image/png"
    ".jpg"  = "image/jpeg"
    ".jpeg" = "image/jpeg"
    ".gif"  = "image/gif"
    ".svg"  = "image/svg+xml"
    ".webp" = "image/webp"
    ".ico"  = "image/x-icon"
    ".woff" = "font/woff"
    ".woff2"= "font/woff2"
    ".ttf"  = "font/ttf"
    ".mp4"  = "video/mp4"
}

$global:lastChange = [DateTime]::UtcNow.Ticks

# Set up FileSystemWatcher for instant file change detection
$watcher = New-Object System.IO.FileSystemWatcher
$watcher.Path = $Path
$watcher.IncludeSubdirectories = $true
$watcher.EnableRaisingEvents = $true
$watcher.Filter = "*.*"

$action = {
    $path = $Event.SourceEventArgs.FullPath
    if ($path -notmatch '[\/\\]\.git' -and $path -notmatch '[\/\\]\.system_generated') {
        $global:lastChange = [DateTime]::UtcNow.Ticks
    }
}

Register-ObjectEvent $watcher "Changed" -Action $action | Out-Null
Register-ObjectEvent $watcher "Created" -Action $action | Out-Null
Register-ObjectEvent $watcher "Renamed" -Action $action | Out-Null
Register-ObjectEvent $watcher "Deleted" -Action $action | Out-Null

$liveReloadScript = @"
<!-- LiveReload Auto-Refresh Script -->
<script>
(function() {
  let currentVer = null;
  setInterval(function() {
    fetch('/__reload_status?t=' + Date.now())
      .then(function(r) { return r.text(); })
      .then(function(ver) {
        if (currentVer !== null && ver !== currentVer) {
          console.log('[LiveReload] Change detected, reloading page...');
          window.location.reload(true);
        }
        currentVer = ver;
      })
      .catch(function(e) {});
  }, 600);
})();
</script>
"@

$listener = New-Object System.Net.HttpListener
$listener.Prefixes.Add("http://localhost:$Port/")
$listener.Prefixes.Add("http://127.0.0.1:$Port/")

try {
    $listener.Start()
    Write-Host "==================================================" -ForegroundColor Green
    Write-Host " Localhost server with Auto LiveReload started!" -ForegroundColor Green
    Write-Host " Root Directory: $Path" -ForegroundColor Cyan
    Write-Host " Server URL:      http://localhost:$Port/" -ForegroundColor Yellow
    Write-Host " IP URL:          http://127.0.0.1:$Port/" -ForegroundColor Yellow
    Write-Host " Auto LiveReload: ENABLED (Auto refreshes on edit)" -ForegroundColor Magenta
    Write-Host "==================================================" -ForegroundColor Green

    while ($listener.IsListening) {
        $context = $listener.GetContext()
        $request = $context.Request
        $response = $context.Response

        try {
            $rawUrl = [System.Uri]::UnescapeDataString($request.Url.AbsolutePath)
            
            # Special LiveReload Status Endpoint
            if ($rawUrl -eq "/__reload_status") {
                $statusBytes = [System.Text.Encoding]::UTF8.GetBytes($global:lastChange.ToString())
                $response.ContentType = "text/plain; charset=utf-8"
                $response.Headers.Add("Cache-Control", "no-cache, no-store, must-revalidate")
                $response.ContentLength64 = $statusBytes.Length
                $response.OutputStream.Write($statusBytes, 0, $statusBytes.Length)
                $response.StatusCode = 200
                continue
            }

            $relativePath = $rawUrl.TrimStart('/')
            
            if ([string]::IsNullOrWhiteSpace($relativePath)) {
                $localFilePath = Join-Path $Path "index.html"
            } else {
                $localFilePath = Join-Path $Path $relativePath
            }

            if (Test-Path -Path $localFilePath -PathType Container) {
                if (!$rawUrl.EndsWith("/")) {
                    $response.StatusCode = 301
                    $response.Headers.Add("Location", $rawUrl + "/" + ($request.Url.Query))
                    $response.Close()
                    continue
                }
                $localFilePath = Join-Path $localFilePath "index.html"
            }

            if (Test-Path -Path $localFilePath -PathType Leaf) {
                $ext = [System.IO.Path]::GetExtension($localFilePath).ToLower()
                $contentType = if ($mimeTypes.ContainsKey($ext)) { $mimeTypes[$ext] } else { "application/octet-stream" }
                
                $response.ContentType = $contentType
                $response.Headers.Add("Cache-Control", "no-cache, no-store, must-revalidate")

                if ($ext -eq ".html" -or $ext -eq ".htm") {
                    $htmlText = [System.IO.File]::ReadAllText($localFilePath, [System.Text.Encoding]::UTF8)
                    if ($htmlText -match "</body>") {
                        $htmlText = $htmlText -replace "</body>", "$liveReloadScript</body>"
                    } else {
                        $htmlText += $liveReloadScript
                    }
                    $htmlBytes = [System.Text.Encoding]::UTF8.GetBytes($htmlText)
                    $response.ContentLength64 = $htmlBytes.Length
                    $response.OutputStream.Write($htmlBytes, 0, $htmlBytes.Length)
                } else {
                    $fileStream = [System.IO.File]::OpenRead($localFilePath)
                    $response.ContentLength64 = $fileStream.Length
                    $fileStream.CopyTo($response.OutputStream)
                    $fileStream.Close()
                    $fileStream.Dispose()
                }

                $response.StatusCode = 200
                Write-Host "[200 OK] $rawUrl" -ForegroundColor Green
            } else {
                $response.StatusCode = 404
                $notFoundBytes = [System.Text.Encoding]::UTF8.GetBytes("404 Not Found: $rawUrl")
                $response.ContentType = "text/plain; charset=utf-8"
                $response.ContentLength64 = $notFoundBytes.Length
                $response.OutputStream.Write($notFoundBytes, 0, $notFoundBytes.Length)
                Write-Host "[404 Not Found] $rawUrl" -ForegroundColor Red
            }
        } catch {
            Write-Host "[Error handling request $rawUrl] $_" -ForegroundColor Red
        } finally {
            try { $response.OutputStream.Close() } catch {}
            try { $response.Close() } catch {}
        }
    }
} catch {
    Write-Host "Fatal Error: $_" -ForegroundColor Red
} finally {
    if ($listener.IsListening) {
        $listener.Stop()
        $listener.Close()
    }
    Unregister-Event -SourceIdentifier "Changed" -ErrorAction SilentlyContinue
    Unregister-Event -SourceIdentifier "Created" -ErrorAction SilentlyContinue
    Unregister-Event -SourceIdentifier "Renamed" -ErrorAction SilentlyContinue
    Unregister-Event -SourceIdentifier "Deleted" -ErrorAction SilentlyContinue
}

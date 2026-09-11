/**
 * ============================================================================
 * MARVELL TECHNOLOGY - THE 1ST VIETNAM SEMICONDUCTOR SUMMIT 2026
 * Google Apps Script Backend Automation Pipeline (Code.gs)
 * Language: 100% International Standard English
 * ============================================================================
 * 
 * QUICK SETUP GUIDE (3 STEPS):
 * 1. Create a new Google Sheet named: "Marvell_Semiconductor_Summit_2026_RSVP"
 * 2. Go to: Extensions -> Apps Script
 * 3. Paste this entire Code.gs source -> Click Save
 * 4. Click Deploy -> New deployment:
 *    - Type: Web app
 *    - Execute as: Me
 *    - Who has access: Anyone
 * 5. Copy the resulting Web App URL and paste it into GOOGLE_SHEET_WEBHOOK_URL in app.js
 */

const SHEET_NAME = "RSVP_Attendees";

// 1. WEBHOOK RECEIVER (doPost)
function doPost(e) {
  try {
    const ss = SpreadsheetApp.getActiveSpreadsheet();
    let sheet = ss.getSheetByName(SHEET_NAME);
    
    // Auto-create header row if sheet does not exist
    if (!sheet) {
      sheet = ss.insertSheet(SHEET_NAME);
      sheet.appendRow([
        "Timestamp",
        "Registration Code",
        "Full Name",
        "Email",
        "Phone",
        "Company / University",
        "Professional Role",
        "Delegate Tier",
        "Interests",
        "Approval Status",
        "Notes / Logistics"
      ]);
      sheet.getRange(1, 1, 1, 11).setFontWeight("bold").setBackground("#0072ce").setFontColor("#ffffff");
      sheet.setFrozenRows(1);
    }

    // Parse payload from client
    let data;
    if (e.postData && e.postData.contents) {
      data = JSON.parse(e.postData.contents);
    } else if (e.parameter) {
      data = e.parameter;
    } else {
      throw new Error("No data received");
    }

    const regCode = data.code || ("MRVL-VSS-" + Math.floor(100000 + Math.random() * 900000));
    const fullName = data.fullName || "";
    const email = data.email || "";
    const phone = data.phone || "";
    const company = data.company || "";
    const role = data.role || "";
    const tier = data.tier || "Industry & IC Designer";
    const interests = Array.isArray(data.interests) ? data.interests.join("; ") : (data.interests || "");
    const timestamp = new Date();

    // Append new attendee row
    sheet.appendRow([
      timestamp,
      regCode,
      fullName,
      email,
      phone,
      company,
      role,
      tier,
      interests,
      "PENDING_REVIEW",
      ""
    ]);

    // Send Email 1: Application Acknowledgment
    if (email) {
      sendEmail1_Acknowledgment({
        code: regCode,
        fullName: fullName,
        email: email,
        company: company,
        tier: tier
      });
    }

    return ContentService.createTextOutput(JSON.stringify({
      status: "success",
      message: "Registration recorded successfully",
      code: regCode
    })).setMimeType(ContentService.MimeType.JSON);

  } catch (error) {
    return ContentService.createTextOutput(JSON.stringify({
      status: "error",
      message: error.toString()
    })).setMimeType(ContentService.MimeType.JSON);
  }
}

// 2. GET TEST ENDPOINT
function doGet(e) {
  return ContentService.createTextOutput("Marvell Semiconductor Summit 2026 Webhook API is Live.")
    .setMimeType(ContentService.MimeType.TEXT);
}

// ============================================================================
// EMAIL 1: RSVP APPLICATION ACKNOWLEDGMENT
// ============================================================================
function sendEmail1_Acknowledgment(data) {
  const subject = `[Marvell Summit 2026] Registration Acknowledgment - ${data.code}`;
  
  const htmlBody = `
  <div style="font-family: 'Plus Jakarta Sans', -apple-system, sans-serif; background-color: #f8fafc; padding: 30px 15px; color: #1e293b;">
    <div style="max-width: 600px; margin: 0 auto; background-color: #ffffff; border: 1px solid #e2e8f0; border-radius: 12px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.06);">
      
      <!-- Top Brand Header -->
      <div style="background-color: #05070a; padding: 18px 24px; border-bottom: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center;">
        <span style="color: #ffffff; font-weight: 800; font-size: 13px; letter-spacing: 1px;">MARVELL TECHNOLOGY</span>
        <span style="color: #00b5e2; font-family: monospace; font-size: 11px;">CODE: ${data.code}</span>
      </div>

      <!-- Blue Banner -->
      <div style="background: linear-gradient(135deg, #0072ce 0%, #005fa3 100%); padding: 25px 24px; color: #ffffff;">
        <span style="background-color: rgba(255,255,255,0.2); font-size: 10px; font-weight: 700; text-transform: uppercase; padding: 4px 8px; border-radius: 6px; letter-spacing: 1px;">RSVP ACKNOWLEDGMENT</span>
        <h2 style="margin: 10px 0 0 0; font-size: 22px; font-weight: 800;">Your Attendance Request Has Been Received</h2>
        <p style="margin: 6px 0 0 0; font-size: 13px; color: #e6f1fa;">The 1st Vietnam Semiconductor Summit 2026 • Ho Chi Minh City</p>
      </div>

      <!-- Body -->
      <div style="padding: 24px; font-size: 14px; line-height: 1.6;">
        <p>Dear <strong>${data.fullName}</strong>,</p>
        <p>On behalf of <strong>Marvell Technology, Inc.</strong> and the Executive Committee of <strong>The 1st Vietnam Semiconductor Summit 2026</strong>, we confirm receipt of your delegate registration request.</p>

        <!-- Details Card -->
        <div style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px; margin: 20px 0;">
          <table style="width: 100%; font-size: 13px; border-collapse: collapse;">
            <tr>
              <td style="padding: 6px 0; color: #64748b; width: 40%;">Reference Code:</td>
              <td style="padding: 6px 0; font-weight: 700; font-family: monospace; color: #0072ce;">${data.code}</td>
            </tr>
            <tr>
              <td style="padding: 6px 0; color: #64748b;">Attendee Name:</td>
              <td style="padding: 6px 0; font-weight: 700; color: #0f172a;">${data.fullName}</td>
            </tr>
            <tr>
              <td style="padding: 6px 0; color: #64748b;">Organization:</td>
              <td style="padding: 6px 0; font-weight: 600; color: #0f172a;">${data.company}</td>
            </tr>
            <tr>
              <td style="padding: 6px 0; color: #64748b;">Requested Pass Tier:</td>
              <td style="padding: 6px 0; font-weight: 700; color: #0072ce;">${data.tier}</td>
            </tr>
          </table>
        </div>

        <!-- Warning status -->
        <div style="background-color: #fffbeb; border: 1px solid #fde68a; border-radius: 8px; padding: 14px; margin: 16px 0; font-size: 13px; color: #92400e;">
          <strong>Status: Under Review (Pending Vetting)</strong><br>
          Due to auditorium seating capacity limits, allocations are vetted by professional specialization. Official confirmation letters and check-in credentials are dispatched within <strong>48 business hours</strong>.
        </div>

        <p style="margin-top: 20px; font-size: 13px; color: #64748b;">For assistance, please contact the Summit Secretariat at: <a href="mailto:summit.vietnam@marvell.com" style="color: #0072ce;">summit.vietnam@marvell.com</a>.</p>
      </div>

      <!-- Footer -->
      <div style="background-color: #f1f5f9; padding: 16px 24px; text-align: center; font-size: 11px; color: #64748b; border-top: 1px solid #e2e8f0;">
        <p style="margin: 0; font-weight: 600;">The 1st Vietnam Semiconductor Summit 2026</p>
        <p style="margin: 4px 0 0 0;">© 2026 Marvell Technology, Inc. All rights reserved.</p>
      </div>

    </div>
  </div>
  `;

  GmailApp.sendEmail(data.email, subject, "", {
    htmlBody: htmlBody,
    name: "Marvell Semiconductor Summit 2026"
  });
}

// ============================================================================
// EMAIL 2: OFFICIAL EXECUTIVE INVITATION LETTER (APPROVED)
// ============================================================================
function sendEmail2_ApprovedInvitation(data) {
  const subject = `[Official Executive Invitation] Welcome to The 1st Vietnam Semiconductor Summit 2026 - ${data.code}`;
  
  const htmlBody = `
  <div style="font-family: 'Plus Jakarta Sans', -apple-system, sans-serif; background-color: #f8fafc; padding: 30px 15px; color: #1e293b;">
    <div style="max-width: 600px; margin: 0 auto; background-color: #ffffff; border: 1px solid #e2e8f0; border-radius: 12px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.06);">
      
      <!-- Top Brand Header -->
      <div style="background-color: #05070a; padding: 18px 24px; display: flex; justify-content: space-between; align-items: center;">
        <span style="color: #ffffff; font-weight: 800; font-size: 13px; letter-spacing: 1px;">MARVELL TECHNOLOGY</span>
        <span style="color: #10b981; font-family: monospace; font-size: 11px; font-weight: 700;">APPROVED</span>
      </div>

      <!-- Dark Tech Invitation Banner -->
      <div style="background-color: #0c1017; padding: 30px 24px; color: #ffffff; border-bottom: 2px solid #0072ce;">
        <span style="background-color: #0072ce; font-size: 10px; font-weight: 700; text-transform: uppercase; padding: 4px 8px; border-radius: 6px; letter-spacing: 1px;">OFFICIAL INVITATION</span>
        <h2 style="margin: 12px 0 0 0; font-size: 22px; font-weight: 800; color: #ffffff;">Welcome to the 1st Vietnam Semiconductor Summit 2026</h2>
        <p style="margin: 6px 0 0 0; font-size: 13px; color: #00b5e2; font-family: monospace;">Monday, Nov 23, 2026 (08:00 - 20:10 ICT) • Ho Chi Minh City</p>
      </div>

      <!-- Body -->
      <div style="padding: 24px; font-size: 14px; line-height: 1.6;">
        <p>Dear <strong>${data.fullName}</strong>,</p>
        <p>The Executive Organizing Committee of <strong>The 1st Vietnam Semiconductor Summit 2026</strong> and the Executive Leadership of <strong>Marvell Technology</strong> are honored to confirm that <strong>your attendance application has been approved</strong>.</p>

        <!-- Seat Allocation -->
        <div style="background-color: #eff6ff; border: 1px solid #bfdbfe; border-radius: 8px; padding: 16px; margin: 20px 0;">
          <table style="width: 100%; font-size: 13px; border-collapse: collapse;">
            <tr>
              <td style="padding: 6px 0; color: #1e40af; width: 40%; font-weight: 600;">Delegate Code:</td>
              <td style="padding: 6px 0; font-weight: 700; font-family: monospace; color: #0072ce;">${data.code}</td>
            </tr>
            <tr>
              <td style="padding: 6px 0; color: #1e40af; font-weight: 600;">Confirmed Pass:</td>
              <td style="padding: 6px 0; font-weight: 700; color: #0072ce;">${data.tier}</td>
            </tr>
            <tr>
              <td style="padding: 6px 0; color: #1e40af; font-weight: 600;">Date & Hours:</td>
              <td style="padding: 6px 0; font-weight: 600; color: #0f172a;">08:00 - 20:10 • Monday, Nov 23, 2026</td>
            </tr>
            <tr>
              <td style="padding: 6px 0; color: #1e40af; font-weight: 600;">Venue:</td>
              <td style="padding: 6px 0; font-weight: 600; color: #0f172a;">Grand Ballroom & Tech Tracks, HCMC</td>
            </tr>
          </table>
        </div>

        <p>Your personalized check-in E-Pass and QR code credentials are being dispatched in the subsequent notification. Please save your pass to facilitate reception entry.</p>
      </div>

      <!-- Footer -->
      <div style="background-color: #f1f5f9; padding: 16px 24px; text-align: center; font-size: 11px; color: #64748b;">
        <p style="margin: 0; font-weight: 600;">The 1st Vietnam Semiconductor Summit 2026</p>
        <p style="margin: 4px 0 0 0;">© 2026 Marvell Technology, Inc. All rights reserved.</p>
      </div>

    </div>
  </div>
  `;

  GmailApp.sendEmail(data.email, subject, "", {
    htmlBody: htmlBody,
    name: "Marvell Semiconductor Summit 2026"
  });
}

// ============================================================================
// EMAIL 3: DIGITAL E-PASS BADGE & CALENDAR .ICS
// ============================================================================
function sendEmail3_FinalEPass(data) {
  const subject = `[Digital E-Pass] Check-in QR Badge for The 1st Vietnam Semiconductor Summit 2026 - ${data.code}`;
  const qrUrl = `https://api.qrserver.com/v1/create-qr-code/?size=180x180&data=MRVL-VSS2026:${data.code}:${data.email}`;

  const htmlBody = `
  <div style="font-family: 'Plus Jakarta Sans', -apple-system, sans-serif; background-color: #f8fafc; padding: 30px 15px; color: #1e293b;">
    <div style="max-width: 600px; margin: 0 auto; background-color: #ffffff; border: 1px solid #e2e8f0; border-radius: 12px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.06);">
      
      <!-- Top Brand Header -->
      <div style="background-color: #05070a; padding: 18px 24px; display: flex; justify-content: space-between; align-items: center;">
        <span style="color: #ffffff; font-weight: 800; font-size: 13px; letter-spacing: 1px;">MARVELL TECHNOLOGY</span>
        <span style="color: #00b5e2; font-family: monospace; font-size: 11px; font-weight: 700;">OFFICIAL PASS</span>
      </div>

      <div style="padding: 24px;">
        <div style="text-align: center; margin-bottom: 20px;">
          <span style="color: #0072ce; font-size: 11px; font-weight: 800; text-transform: uppercase; letter-spacing: 1.5px;">OFFICIAL ATTENDEE CREDENTIAL</span>
          <h2 style="margin: 8px 0 0 0; font-size: 22px; font-weight: 800; color: #0f172a;">Digital E-Pass & Check-in QR</h2>
        </div>

        <!-- E-PASS CARD -->
        <div style="background-color: #0c1017; border: 1px solid #00b5e2; border-radius: 10px; padding: 24px; color: #ffffff;">
          <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #334155; padding-bottom: 12px; margin-bottom: 16px;">
            <div>
              <span style="font-size: 10px; color: #94a3b8; text-transform: uppercase; font-weight: 700;">DELEGATE CODE:</span>
              <span style="display: block; font-family: monospace; font-size: 18px; font-weight: 800; color: #00b5e2;">${data.code}</span>
            </div>
            <span style="background-color: #0072ce; color: #ffffff; font-size: 10px; font-weight: 700; padding: 4px 8px; border-radius: 6px; text-transform: uppercase;">${data.tier}</span>
          </div>

          <table style="width: 100%; font-size: 13px; margin-bottom: 20px; border-collapse: collapse;">
            <tr>
              <td style="padding: 4px 0; color: #94a3b8; width: 40%;">Delegate:</td>
              <td style="padding: 4px 0; font-weight: 700; color: #ffffff;">${data.fullName}</td>
            </tr>
            <tr>
              <td style="padding: 4px 0; color: #94a3b8;">Organization:</td>
              <td style="padding: 4px 0; font-weight: 600; color: #e2e8f0;">${data.company}</td>
            </tr>
            <tr>
              <td style="padding: 4px 0; color: #94a3b8;">Schedule:</td>
              <td style="padding: 4px 0; font-weight: 600; color: #ffffff;">Monday, Nov 23, 2026 (08:00 - 20:10)</td>
            </tr>
          </table>

          <!-- QR Box -->
          <div style="text-align: center; background-color: #ffffff; padding: 16px; border-radius: 8px; display: inline-block; margin: 0 auto; width: 180px;">
            <img src="${qrUrl}" alt="Check-in QR" style="width: 180px; height: 180px; display: block;" />
          </div>
          <p style="text-align: center; font-size: 11px; color: #94a3b8; margin: 10px 0 0 0; font-family: monospace;">Scan at Registration Reception Desk</p>
        </div>

        <!-- Logistics -->
        <div style="margin-top: 24px; padding: 16px; background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; font-size: 13px;">
          <strong>Important Delegate Notes:</strong>
          <ul style="margin: 8px 0 0 0; padding-left: 20px; color: #64748b;">
            <li>Registration desk opens at 07:30 AM.</li>
            <li>Dress code: Business Professional or Business Casual.</li>
          </ul>
        </div>
      </div>

      <!-- Footer -->
      <div style="background-color: #f1f5f9; padding: 16px 24px; text-align: center; font-size: 11px; color: #64748b;">
        <p style="margin: 0; font-weight: 600;">The 1st Vietnam Semiconductor Summit 2026</p>
        <p style="margin: 4px 0 0 0;">© 2026 Marvell Technology, Inc. All rights reserved.</p>
      </div>

    </div>
  </div>
  `;

  GmailApp.sendEmail(data.email, subject, "", {
    htmlBody: htmlBody,
    name: "Marvell Semiconductor Summit 2026"
  });
}

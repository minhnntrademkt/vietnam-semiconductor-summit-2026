# The 1st Vietnam Semiconductor Summit 2026 - Official Event Landing Page

Official enterprise event landing page for **The 1st Vietnam Semiconductor Summit 2026** hosted by **Marvell Technology, Inc. (NASDAQ: MRVL)**.

## 📌 Event Overview
- **Host Organization**: Marvell Technology, Inc. (NASDAQ: MRVL)
- **Event Date**: Monday, November 23, 2026 (08:00 - 20:10 ICT)
- **Venue**: Ho Chi Minh City, Vietnam (Grand Ballroom & Tech Tracks)
- **Admission Model**: 100% Free RSVP (Vetted Delegate Pass • Limited Capacity)
- **Language**: 100% International Standard English

---

## 📁 Repository Structure
```
vietnam-semiconductor-summit-2026/
├── index.html                       # Complete production landing page (12 sections + modals)
├── styles.css                       # Marvell Design System (Tokens, Glassmorphism, Kinetic CTA)
├── app.js                           # Interactive JS (Countdown, Agenda filtering, Bio & RSVP Modals, QR E-Pass, ICS)
├── agenda.json                      # 24-session timetable database
├── build_site.py                    # Automated HTML compiler and generator script
├── marvell-logo.svg                 # Official Marvell Technology SVG Vector Brand Asset
├── marvell-summit-email-review.html # 3-Step Email Funnel Review Dashboard (Desktop/Mobile preview)
├── Code.gs                          # Google Apps Script backend pipeline (Webhook & Gmail Automation)
├── PROJECT_SPEC.md                  # Technical specification & Marvell brand guidelines
└── README.md                        # Documentation & quick start guide
```

---

## 🚀 Key Features & Highlights
1. **Marvell Design System (B2B Enterprise Modern):**
   - Soft hierarchical radius system (`6px` buttons, `12px-14px` cards, `18px` modals).
   - Silicon Photonics glassmorphism (`backdrop-filter: blur(16px)`), cyan & lavender glowing accents.
   - High-contrast pure black tech canvas with kinetic arrow hover CTAs.
2. **Interactive Speaker Bio Modals:**
   - Detailed executive profiles, biographies, and scheduled sessions for all 12 key leaders and luminaries.
3. **Quick RSVP Modal:**
   - Seamless attendee registration accessible across all CTAs with 4 Delegate Pass Tiers:
     * *VIP Delegate (C-Level & Diplomatic)*
     * *Industry & IC Designer*
     * *Academia & Faculty*
     * *Talent & Elite Student*
4. **Digital E-Pass & Dynamic QR Code:**
   - Generates unique attendee code (`MRVL-VSS-XXXXXX`) and live check-in QR code.
   - Built-in "Add to Calendar" `.ics` file exporter and Google Calendar event generator.
5. **3-Step Automated Email Workflow Dashboard:**
   - Preview and review dashboard: [marvell-summit-email-review.html](marvell-summit-email-review.html)
   - Email 1: RSVP Application Acknowledgment
   - Email 2: Official Executive Invitation Letter (Approved)
   - Email 3: Digital E-Pass Badge & Check-in QR
6. **Backend Automation Ready:**
   - Production-ready [Code.gs](Code.gs) script for Google Sheets & Gmail API automation.

---

## 💻 Local Development & Preview
To run locally:
```bash
python -m http.server 3000
```
Then open your browser at:
- **Landing Page**: `http://localhost:3000/`
- **Email Review Dashboard**: `http://localhost:3000/marvell-summit-email-review.html`

---

## 🔗 Official Repository
- **GitHub**: [https://github.com/minhnntrademkt/vietnam-semiconductor-summit-2026.git](https://github.com/minhnntrademkt/vietnam-semiconductor-summit-2026.git)
- **License**: © 2026 Marvell Technology, Inc. All rights reserved.

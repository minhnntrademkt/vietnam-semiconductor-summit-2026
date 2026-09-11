// ==========================================================================
// MARVELL - THE 1ST VIETNAM SEMICONDUCTOR SUMMIT 2026
// Interactive Features: Countdown, Agenda Filter, Bio Modal, Quick RSVP, E-Pass & ICS
// Language: 100% International Standard English
// ==========================================================================

document.addEventListener('DOMContentLoaded', () => {
  initCountdown();
  initAgendaTabs();
  initSpeakerBioModal();
  initQuickRsvpModal();
  initRegistrationForm();
  initMobileNav();
  initSmoothScroll();
  initScrollProgress();
  initFaqAccordion();
});

// ==========================================================================
// 1. SPEAKER BIOS DATABASE (12 DIGNITARIES & LEADERS - 100% ENGLISH)
// ==========================================================================
const SPEAKER_BIOS = {
  'noam-mizrahi': {
    name: 'Noam Mizrahi',
    title: 'EVP & Chief Technology Officer (CTO)',
    org: 'Marvell Technology, Inc. (NASDAQ: MRVL)',
    tag: 'STRATEGIC KEYNOTE / IC DESIGN',
    avatarText: 'NM',
    colorClass: 'text-[#00b5e2] border-cyan-500/50 bg-blue-950/80',
    bio: 'Noam Mizrahi is Executive Vice President and Chief Technology Officer (CTO) at Marvell Technology. With over 25 years of engineering leadership, he orchestrates Marvell’s long-term technology vision, pioneering domain-specific compute architectures, advanced multi-die modular packaging (Chiplets), and optical interconnects (CPO) engineered for the accelerated AI cloud era.',
    sessions: [
      {
        time: '09:30 - 10:15',
        title: 'Keynote 1: IC Design - Advanced Silicon Architecture Trends & Vietnam\'s Semiconductor Future',
        room: 'Grand Ballroom (Plenary Hall)',
        category: 'Strategic Keynote'
      },
      {
        time: '14:00 - 15:30',
        title: 'Strategic High-Level Panel: Building Vietnam\'s National Semiconductor Value Chain 2026–2035',
        room: 'VIP Executive Plenary Hall',
        category: 'High-Level Panel'
      }
    ]
  },
  'sandeep-bharathi': {
    name: 'Sandeep Bharathi',
    title: 'President, Data Center Group (DCG)',
    org: 'Marvell Technology, Inc. (NASDAQ: MRVL)',
    tag: 'PANEL HOST / AI SILICON',
    avatarText: 'SB',
    colorClass: 'text-[#c8a3ef] border-purple-500/50 bg-purple-950/80',
    bio: 'Sandeep Bharathi leads Marvell’s Data Center Group, spearheading custom compute silicon, high-throughput cloud networking, and optical interconnect storage solutions. He plays a pivotal role in expanding Marvell’s engineering footprint and R&D centers across Ho Chi Minh City and Da Nang.',
    sessions: [
      {
        time: '14:00 - 15:30',
        title: 'Session Chair: Strategic Plenary on National Semiconductor Value Chain',
        room: 'VIP Executive Plenary Hall',
        category: 'High-Level Panel'
      },
      {
        time: '16:00 - 16:45',
        title: 'Technical Session: AI Semiconductor Infrastructure & Future Cloud Architectures',
        room: 'Tech Track A',
        category: 'Industry'
      }
    ]
  },
  'nguyen-van-duoc': {
    name: 'Mr. Nguyen Van Duoc',
    title: 'Chairman',
    org: 'Ho Chi Minh City People\'s Committee',
    tag: 'GUEST OF HONOR / GOVERNMENT',
    avatarText: 'NVD',
    colorClass: 'text-emerald-400 border-emerald-500/50 bg-emerald-950/80',
    bio: 'Chairman of Ho Chi Minh City People\'s Committee, spearheading the municipal initiative to transform HCMC into a regional center for high-tech innovation, IC design incubation, and microelectronics manufacturing. He champions special regulatory sandbox incentives, tax credits, and talent attraction funds for the semiconductor sector.',
    sessions: [
      {
        time: '08:30 - 09:00',
        title: 'Summit Inaugural Address: Ho Chi Minh City High-Tech & Semiconductor Strategy',
        room: 'Grand Ballroom (Plenary Hall)',
        category: 'Ceremony'
      },
      {
        time: '14:00 - 15:30',
        title: 'Strategic Plenary: Public-Private-Academic Partnership in Semiconductor Ecosystems',
        room: 'VIP Executive Plenary Hall',
        category: 'High-Level Panel'
      }
    ]
  },
  'melissa-brown': {
    name: 'Ms. Melissa A. Brown',
    title: 'U.S. Consul General in Ho Chi Minh City',
    org: 'U.S. Diplomatic Mission to Vietnam',
    tag: 'DIPLOMATIC MISSION / STRATEGIC PARTNER',
    avatarText: 'MB',
    colorClass: 'text-amber-400 border-amber-500/50 bg-amber-950/80',
    bio: 'Senior representative of the United States government in Southern Vietnam, driving forward the U.S.–Vietnam Comprehensive Strategic Partnership in critical emerging technologies, semiconductor supply chain resilience, and workforce capacity initiatives through the International Technology Security and Innovation (ITSI) Fund under the CHIPS and Science Act.',
    sessions: [
      {
        time: '09:00 - 09:20',
        title: 'Diplomatic Address: U.S.-Vietnam Strategic Alliance in Global Semiconductor Supply Chains',
        room: 'Grand Ballroom (Plenary Hall)',
        category: 'Keynote'
      },
      {
        time: '11:30 - 13:00',
        title: 'VIP Diplomatic Reception & Bilateral Business Networking Luncheon',
        room: 'VIP Executive Banquet Lounge',
        category: 'Networking'
      }
    ]
  },
  'nguyen-bich-yen': {
    name: 'Ms. Nguyen Bich-Yen',
    title: 'Senior Technical Fellow & Researcher',
    org: 'VSAP-LAB (Advanced Packaging Consortium)',
    tag: 'KEYNOTE 2 / ADVANCED PACKAGING',
    avatarText: 'NBY',
    colorClass: 'text-[#00b5e2] border-cyan-500/50 bg-blue-950/80',
    bio: 'Globally recognized pioneer in semiconductor heterogeneous integration with over 30 years of research experience in Silicon Valley and dozens of international patents. She leads research on 2.5D/3D advanced packaging architectures, wafer-level assembly, and Co-Packaged Optics (CPO) for high-density AI accelerators.',
    sessions: [
      {
        time: '10:30 - 11:15',
        title: 'Keynote 2: Advanced Packaging Technologies & Heterogeneous Integration (CPO)',
        room: 'Grand Ballroom (Plenary Hall)',
        category: 'Keynote'
      }
    ]
  },
  'hien-dao': {
    name: 'Ms. Hien Dao',
    title: 'Director of Assembly & Test Engineering',
    org: 'Intel Corporation Vietnam',
    tag: 'INDUSTRY / ATP MANUFACTURING',
    avatarText: 'HD',
    colorClass: 'text-[#00b5e2] border-cyan-500/50 bg-blue-950/80',
    bio: 'Seasoned manufacturing leader with over 18 years overseeing advanced silicon packaging and high-volume test manufacturing (ATP) at Intel Products Vietnam, helping establish the facility as one of the largest and most sophisticated backend manufacturing nodes in Intel’s worldwide network.',
    sessions: [
      {
        time: '13:30 - 14:15',
        title: 'High-Volume Semiconductor Assembly, Packaging & Global ATP Quality Standards',
        room: 'Tech Track A',
        category: 'Industry'
      }
    ]
  },
  'vo-phong': {
    name: 'Mr. Vo Phong',
    title: 'Director of Processor Microarchitecture',
    org: 'Ampere Computing Vietnam',
    tag: 'INDUSTRY / SERVER ARM CPU',
    avatarText: 'VP',
    colorClass: 'text-[#00b5e2] border-cyan-500/50 bg-blue-950/80',
    bio: 'Specialist in energy-efficient cloud-native server ARM microprocessors. He leads a core engineering team in Vietnam designing high-core-count compute engines (up to 192 cores) deployed across global hyperscale cloud infrastructures.',
    sessions: [
      {
        time: '14:30 - 15:15',
        title: 'Energy-Efficient ARM Server CPU Design & Compute Density Trends for AI Cloud',
        room: 'Tech Track A',
        category: 'Industry'
      }
    ]
  },
  'tran-dang-khoa': {
    name: 'Mr. Tran Dang Khoa',
    title: 'R&D Director, Automotive Microelectronics',
    org: 'Renesas Electronics Vietnam',
    tag: 'INDUSTRY / AUTOMOTIVE IC',
    avatarText: 'TDK',
    colorClass: 'text-[#00b5e2] border-cyan-500/50 bg-blue-950/80',
    bio: 'Automotive semiconductor architect focused on safety-critical MCU/SoC designs, ADAS vehicle control platforms, and ISO 26262 compliant architectures. He has spearheaded the expansion of Renesas R&D operations in Southern Vietnam for over 15 years.',
    sessions: [
      {
        time: '15:30 - 16:15',
        title: 'Automotive Microcontroller Architectures & Functional Safety for Autonomous EV Platforms',
        room: 'Tech Track B',
        category: 'Industry'
      }
    ]
  },
  'vo-thieu-nam': {
    name: 'Mr. Vo Thieu Nam',
    title: 'Senior Solutions Consultant, Wireless Silicon',
    org: 'Qualcomm Technologies Vietnam',
    tag: 'INDUSTRY / CONNECTIVITY 5G/6G',
    avatarText: 'VTN',
    colorClass: 'text-[#00b5e2] border-cyan-500/50 bg-blue-950/80',
    bio: 'Authority on RF Front-End microelectronics, ultra-wideband communications, 5G/6G modem architectures, and on-device Edge AI processing. He actively supports Vietnam’s IoT and telecommunications ecosystem through technical enablement programs.',
    sessions: [
      {
        time: '16:30 - 17:15',
        title: 'Next-Gen Mobile Connectivity Silicon: 5G Advanced, 6G Roadmaps & Wi-Fi 7 Front-End ICs',
        room: 'Tech Track B',
        category: 'Industry'
      }
    ]
  },
  'mai-thi-thanh-nguyen': {
    name: 'Assoc. Prof. Mai Thi Thanh Nguyen',
    title: 'Vice Head of Science & Tech / Senior Faculty',
    org: 'Vietnam National University, Ho Chi Minh City (VNU-HCMC)',
    tag: 'ACADEMIA / ECOSYSTEM & TALENT',
    avatarText: 'MTN',
    colorClass: 'text-emerald-400 border-emerald-500/50 bg-emerald-950/80',
    bio: 'Prominent scientist in MEMS and advanced semiconductor materials. She sits on the executive board for Vietnam’s National Semiconductor Human Resource Development Taskforce, aiming to train 50,000 engineers by 2030 across VNU-HCMC member universities.',
    sessions: [
      {
        time: '14:00 - 15:30',
        title: 'Strategic Plenary: Industry-University Tripartite Synergies in Talent Pipeline Readiness',
        room: 'VIP Executive Plenary Hall',
        category: 'High-Level Panel'
      }
    ]
  },
  'nguyen-hoang-trang': {
    name: 'Prof. Nguyen Hoang Trang',
    title: 'Dean of Electrical & Electronics / Director of IC Lab',
    org: 'Ho Chi Minh City University of Technology (HCMUT)',
    tag: 'ACADEMIA / DIGITAL IC DESIGN',
    avatarText: 'NHT',
    colorClass: 'text-emerald-400 border-emerald-500/50 bg-emerald-950/80',
    bio: 'Leading professor in digital IC design, FPGA architectures, and formal ASIC verification. His laboratory has trained multiple generations of elite silicon design engineers now working at Marvell, Intel, Qualcomm, and Renesas.',
    sessions: [
      {
        time: '11:15 - 12:00',
        title: 'Digital IC Design Curriculum & Research: Bridging Academia and Enterprise Demands',
        room: 'Tech Track A',
        category: 'Academia'
      }
    ]
  },
  'nguyen-pham-loan': {
    name: 'Prof. Nguyen Pham Loan',
    title: 'Director, School of Electronics & Telecommunications',
    org: 'Hanoi University of Science and Technology (HUST)',
    tag: 'ACADEMIA / ANALOG & RF IC',
    avatarText: 'NPL',
    colorClass: 'text-emerald-400 border-emerald-500/50 bg-emerald-950/80',
    bio: 'Eminent researcher in analog/mixed-signal integrated circuits and high-frequency microwave communications (RFIC). He represents premier technological universities in Northern Vietnam fostering national research alignment with Southern innovation hubs.',
    sessions: [
      {
        time: '15:00 - 15:45',
        title: 'Analog & Microwave Mixed-Signal IC Design for High-Throughput Wireless Telecommunications',
        room: 'Tech Track B',
        category: 'Academia'
      }
    ]
  }
};

// ==========================================================================
// 2. COUNTDOWN TIMER TO NOV 23, 2026
// ==========================================================================
function initCountdown() {
  const summitDate = new Date('2026-11-23T08:00:00+07:00').getTime();
  
  const daysEl = document.getElementById('count-days');
  const hoursEl = document.getElementById('count-hours');
  const minsEl = document.getElementById('count-mins');
  const secsEl = document.getElementById('count-secs');
  
  if (!daysEl || !hoursEl || !minsEl || !secsEl) return;

  function update() {
    const now = new Date().getTime();
    const distance = summitDate - now;

    if (distance < 0) {
      daysEl.innerText = '00';
      hoursEl.innerText = '00';
      minsEl.innerText = '00';
      secsEl.innerText = '00';
      return;
    }

    const days = Math.floor(distance / (1000 * 60 * 60 * 24));
    const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((distance % (1000 * 60)) / 1000);

    daysEl.innerText = String(days).padStart(2, '0');
    hoursEl.innerText = String(hours).padStart(2, '0');
    minsEl.innerText = String(minutes).padStart(2, '0');
    secsEl.innerText = String(seconds).padStart(2, '0');
  }

  update();
  setInterval(update, 1000);
}

// ==========================================================================
// 3. AGENDA TABS & FILTERING
// ==========================================================================
function initAgendaTabs() {
  const tabButtons = document.querySelectorAll('.agenda-tab-btn');
  const filterPills = document.querySelectorAll('.agenda-filter-pill');
  const agendaCards = document.querySelectorAll('.agenda-item-card');

  let currentSession = 'all';
  let currentCategory = 'all';

  function applyFilters() {
    agendaCards.forEach(card => {
      const cardSession = card.getAttribute('data-session');
      const cardCategory = card.getAttribute('data-category');

      const sessionMatch = (currentSession === 'all') || (cardSession === currentSession);
      const categoryMatch = (currentCategory === 'all') || (cardCategory === currentCategory);

      if (sessionMatch && categoryMatch) {
        card.style.display = 'flex';
        card.classList.remove('hidden');
      } else {
        card.style.display = 'none';
        card.classList.add('hidden');
      }
    });
  }

  tabButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      tabButtons.forEach(b => {
        b.classList.remove('active', 'bg-slate-900', 'text-white', 'shadow-sm');
        b.classList.add('text-slate-600');
      });
      btn.classList.add('active', 'bg-slate-900', 'text-white', 'shadow-sm');
      btn.classList.remove('text-slate-600');

      currentSession = btn.getAttribute('data-session');
      applyFilters();
    });
  });

  filterPills.forEach(pill => {
    pill.addEventListener('click', () => {
      filterPills.forEach(p => {
        p.classList.remove('active', 'border-[#0072ce]', 'text-[#0072ce]', 'bg-blue-50', 'font-semibold');
        p.classList.add('border-slate-300', 'text-slate-600');
      });
      pill.classList.add('active', 'border-[#0072ce]', 'text-[#0072ce]', 'bg-blue-50', 'font-semibold');
      pill.classList.remove('border-slate-300', 'text-slate-600');

      currentCategory = pill.getAttribute('data-category');
      applyFilters();
    });
  });
}

// ==========================================================================
// 4. POP-UP 1: SPEAKER BIO MODAL
// ==========================================================================
function initSpeakerBioModal() {
  const modal = document.getElementById('speaker-bio-modal');
  const closeBtn = document.getElementById('speaker-modal-close');
  const rsvpBtn = document.getElementById('speaker-modal-rsvp-btn');
  const cards = document.querySelectorAll('.speaker-card');

  if (!modal) return;

  function openSpeakerBio(speakerId) {
    const speaker = SPEAKER_BIOS[speakerId];
    if (!speaker) return;

    document.getElementById('speaker-modal-name').innerText = speaker.name;
    document.getElementById('speaker-modal-title').innerText = speaker.title;
    document.getElementById('speaker-modal-org').innerText = speaker.org;
    document.getElementById('speaker-modal-tag').innerText = speaker.tag;
    document.getElementById('speaker-modal-avatar').innerText = speaker.avatarText;
    document.getElementById('speaker-modal-bio').innerText = speaker.bio;

    // Render sessions
    const sessionsContainer = document.getElementById('speaker-modal-sessions');
    sessionsContainer.innerHTML = '';
    speaker.sessions.forEach(sess => {
      const sessEl = document.createElement('div');
      sessEl.className = 'p-3.5 rounded-xl bg-[#101726] border border-slate-800 flex flex-col sm:flex-row sm:items-center justify-between gap-2';
      sessEl.innerHTML = `
        <div>
          <span class="text-[10px] font-mono text-[#00b5e2] font-bold block">${sess.time} • ${sess.room}</span>
          <span class="text-xs font-semibold text-white mt-0.5 block">${sess.title}</span>
        </div>
        <span class="text-[10px] uppercase font-bold text-slate-400 bg-slate-800/80 px-2 py-0.5 rounded border border-slate-700 self-start sm:self-auto">${sess.category}</span>
      `;
      sessionsContainer.appendChild(sessEl);
    });

    modal.classList.remove('hidden');
    modal.classList.add('flex');
    document.body.style.overflow = 'hidden';
  }

  cards.forEach(card => {
    card.addEventListener('click', () => {
      const speakerId = card.getAttribute('data-speaker-id');
      if (speakerId) {
        openSpeakerBio(speakerId);
      }
    });
  });

  function closeSpeakerModal() {
    modal.classList.add('hidden');
    modal.classList.remove('flex');
    document.body.style.overflow = 'auto';
  }

  if (closeBtn) {
    closeBtn.addEventListener('click', closeSpeakerModal);
  }

  modal.addEventListener('click', (e) => {
    if (e.target === modal) closeSpeakerModal();
  });

  if (rsvpBtn) {
    rsvpBtn.addEventListener('click', () => {
      closeSpeakerModal();
      openQuickRsvpModal();
    });
  }

  window.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && !modal.classList.contains('hidden')) {
      closeSpeakerModal();
    }
  });
}

// ==========================================================================
// 5. POP-UP 2: QUICK RSVP REGISTRATION MODAL
// ==========================================================================
function openQuickRsvpModal(defaultTier) {
  const modal = document.getElementById('quick-rsvp-modal');
  if (!modal) return;

  if (defaultTier) {
    const radio = modal.querySelector(`input[name="modal_tier"][value*="${defaultTier}"]`);
    if (radio) radio.checked = true;
  }

  modal.classList.remove('hidden');
  modal.classList.add('flex');
  document.body.style.overflow = 'hidden';
}

function closeQuickRsvpModal() {
  const modal = document.getElementById('quick-rsvp-modal');
  if (!modal) return;
  modal.classList.add('hidden');
  modal.classList.remove('flex');
  document.body.style.overflow = 'auto';
}

function initQuickRsvpModal() {
  const modal = document.getElementById('quick-rsvp-modal');
  const closeBtn = document.getElementById('quick-rsvp-close');
  const form = document.getElementById('quick-rsvp-form');
  const triggerBtns = document.querySelectorAll('.open-rsvp-modal-btn');

  if (!modal) return;

  triggerBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      openQuickRsvpModal();
    });
  });

  if (closeBtn) {
    closeBtn.addEventListener('click', closeQuickRsvpModal);
  }

  modal.addEventListener('click', (e) => {
    if (e.target === modal) closeQuickRsvpModal();
  });

  window.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && !modal.classList.contains('hidden')) {
      closeQuickRsvpModal();
    }
  });

  if (form) {
    form.addEventListener('submit', (e) => {
      e.preventDefault();

      const fullName = document.getElementById('modal-fullname').value.trim();
      const email = document.getElementById('modal-email').value.trim();
      const phone = document.getElementById('modal-phone').value.trim();
      const company = document.getElementById('modal-company').value.trim();
      const role = document.getElementById('modal-role').value.trim();

      const tierRadio = form.querySelector('input[name="modal_tier"]:checked');
      const tier = tierRadio ? tierRadio.value : 'Industry & IC Designer';

      const interests = [];
      form.querySelectorAll('input[name="modal_interests"]:checked').forEach(cb => {
        interests.push(cb.value);
      });

      if (!fullName || !email || !phone || !company || !role) {
        alert('Please complete all required fields marked with (*)');
        return;
      }

      // Email validation
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!emailRegex.test(email)) {
        alert('Please enter a valid business or academic email address.');
        return;
      }

      // Generate Registration Code
      const regCode = 'MRVL-VSS-' + Math.floor(100000 + Math.random() * 900000);

      const attendee = {
        code: regCode,
        fullName,
        email,
        phone,
        company,
        role,
        tier,
        interests,
        registeredAt: new Date().toISOString()
      };

      // Save to localStorage
      const saved = JSON.parse(localStorage.getItem('mrvl_attendees') || '[]');
      saved.push(attendee);
      localStorage.setItem('mrvl_attendees', JSON.stringify(saved));

      // Close RSVP Modal & show Ticket Pass
      closeQuickRsvpModal();
      form.reset();
      showTicketModal(attendee);
    });
  }
}

// ==========================================================================
// 6. IN-PAGE REGISTRATION FORM & TICKET MODAL HANDLER
// ==========================================================================
function showTicketModal(attendee) {
  const modal = document.getElementById('ticket-modal');
  if (!modal) return;

  document.getElementById('ticket-code').innerText = attendee.code;
  document.getElementById('ticket-name').innerText = attendee.fullName;
  document.getElementById('ticket-email').innerText = attendee.email;
  document.getElementById('ticket-company').innerText = attendee.company;
  document.getElementById('ticket-role').innerText = attendee.role;

  const tierBadge = document.getElementById('ticket-tier-badge');
  if (tierBadge) {
    tierBadge.innerText = attendee.tier ? attendee.tier.toUpperCase() : 'DELEGATE PASS';
  }

  // Generate Dynamic Real QR Code
  const qrImg = document.getElementById('ticket-qr-img');
  if (qrImg) {
    const qrData = encodeURIComponent(`MRVL-VSS2026:${attendee.code}:${attendee.fullName}:${attendee.email}`);
    qrImg.src = `https://api.qrserver.com/v1/create-qr-code/?size=160x160&data=${qrData}`;
  }

  // Setup Add-to-Calendar Button
  const calBtn = document.getElementById('add-calendar-btn');
  if (calBtn) {
    calBtn.onclick = () => {
      exportSummitIcs(attendee);
    };
  }

  modal.classList.remove('hidden');
  modal.classList.add('flex');
  document.body.style.overflow = 'hidden';
}

function initRegistrationForm() {
  const form = document.getElementById('summit-register-form');
  const modal = document.getElementById('ticket-modal');
  const closeBtn = document.getElementById('modal-close-btn');
  const downloadBtn = document.getElementById('download-ticket-btn');

  if (!form || !modal) return;

  form.addEventListener('submit', (e) => {
    e.preventDefault();

    const fullName = document.getElementById('reg-fullname').value.trim();
    const email = document.getElementById('reg-email').value.trim();
    const phone = document.getElementById('reg-phone').value.trim();
    const company = document.getElementById('reg-company').value.trim();
    const role = document.getElementById('reg-role').value;

    const tierRadio = form.querySelector('input[name="reg_tier"]:checked');
    const tier = tierRadio ? tierRadio.value : 'Industry & IC Designer';

    const interests = [];
    form.querySelectorAll('input[name="interests"]:checked').forEach(cb => {
      interests.push(cb.value);
    });

    if (!fullName || !email || !phone || !company) {
      alert('Please complete all required fields marked with (*)');
      return;
    }

    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
      alert('Please enter a valid email address.');
      return;
    }

    const regCode = 'MRVL-VSS-' + Math.floor(100000 + Math.random() * 900000);

    const attendee = {
      code: regCode,
      fullName,
      email,
      phone,
      company,
      role,
      tier,
      interests,
      registeredAt: new Date().toISOString()
    };

    const saved = JSON.parse(localStorage.getItem('mrvl_attendees') || '[]');
    saved.push(attendee);
    localStorage.setItem('mrvl_attendees', JSON.stringify(saved));

    form.reset();
    showTicketModal(attendee);
  });

  function closeTicketModal() {
    modal.classList.add('hidden');
    modal.classList.remove('flex');
    document.body.style.overflow = 'auto';
  }

  if (closeBtn) {
    closeBtn.addEventListener('click', closeTicketModal);
  }

  modal.addEventListener('click', (e) => {
    if (e.target === modal) closeTicketModal();
  });

  window.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && !modal.classList.contains('hidden')) {
      closeTicketModal();
    }
  });

  if (downloadBtn) {
    downloadBtn.addEventListener('click', () => {
      window.print();
    });
  }
}

// ==========================================================================
// 7. CALENDAR ICS EXPORT & GOOGLE CALENDAR LINK
// ==========================================================================
function exportSummitIcs(attendee) {
  const icsContent = [
    'BEGIN:VCALENDAR',
    'VERSION:2.0',
    'PRODID:-//Marvell Technology//Vietnam Semiconductor Summit 2026//EN',
    'CALSCALE:GREGORIAN',
    'METHOD:PUBLISH',
    'BEGIN:VEVENT',
    'UID:MRVL-VSS-2026-' + attendee.code + '@marvell.com',
    'DTSTAMP:20260911T000000Z',
    'DTSTART:20261123T010000Z', // 08:00 ICT = 01:00 UTC
    'DTEND:20261123T131000Z',   // 20:10 ICT = 13:10 UTC
    'SUMMARY:The 1st Vietnam Semiconductor Summit 2026 | Marvell Technology',
    'DESCRIPTION:Inaugural Vietnam Semiconductor Summit hosted by Marvell Technology, Inc.\\nRegistration Code: ' + attendee.code + '\\nDelegate: ' + attendee.fullName + '\\nPass Tier: ' + attendee.tier,
    'LOCATION:Ho Chi Minh City, Vietnam',
    'STATUS:CONFIRMED',
    'ORGANIZER;CN=Marvell Technology:MAILTO:events@marvell.com',
    'END:VEVENT',
    'END:VCALENDAR'
  ].join('\r\n');

  const blob = new Blob([icsContent], { type: 'text/calendar;charset=utf-8' });
  const link = document.createElement('a');
  link.href = window.URL.createObjectURL(blob);
  link.setAttribute('download', `Marvell_Semiconductor_Summit_2026_${attendee.code}.ics`);
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
}

// ==========================================================================
// 8. MOBILE NAVIGATION
// ==========================================================================
function initMobileNav() {
  const menuBtn = document.getElementById('mobile-menu-btn');
  const mobileMenu = document.getElementById('mobile-nav-menu');
  const closeMenuBtn = document.getElementById('mobile-menu-close');
  const menuLinks = document.querySelectorAll('.mobile-link');

  if (!menuBtn || !mobileMenu) return;

  menuBtn.addEventListener('click', () => {
    mobileMenu.classList.remove('hidden');
  });

  if (closeMenuBtn) {
    closeMenuBtn.addEventListener('click', () => {
      mobileMenu.classList.add('hidden');
    });
  }

  menuLinks.forEach(link => {
    link.addEventListener('click', () => {
      mobileMenu.classList.add('hidden');
    });
  });
}

// ==========================================================================
// 9. SMOOTH SCROLL FOR JUMP LINKS
// ==========================================================================
function initSmoothScroll() {
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      const targetId = this.getAttribute('href');
      if (targetId === '#') return;
      
      if (this.classList.contains('open-rsvp-modal-btn')) return;

      const targetEl = document.querySelector(targetId);
      if (targetEl) {
        e.preventDefault();
        targetEl.scrollIntoView({
          behavior: 'smooth',
          block: 'start'
        });
      }
    });
  });
}

// ==========================================================================
// 10. READING SCROLL PROGRESS BAR
// ==========================================================================
function initScrollProgress() {
  const progressBar = document.getElementById('scroll-progress-bar');
  if (!progressBar) return;

  window.addEventListener('scroll', () => {
    const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
    const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    const scrolled = height > 0 ? (winScroll / height) * 100 : 0;
    progressBar.style.width = scrolled + '%';
  });
}

// ==========================================================================
// 11. INTERACTIVE FAQ ACCORDION
// ==========================================================================
function initFaqAccordion() {
  const faqItems = document.querySelectorAll('.faq-accordion-item');
  if (!faqItems.length) return;

  faqItems.forEach(item => {
    const header = item.querySelector('.faq-accordion-header');
    if (!header) return;

    header.addEventListener('click', () => {
      const isActive = item.classList.contains('active');

      faqItems.forEach(otherItem => {
        otherItem.classList.remove('active');
      });

      if (!isActive) {
        item.classList.add('active');
      }
    });
  });
}

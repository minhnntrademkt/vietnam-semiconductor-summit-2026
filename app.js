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
  initSmartHeader();
  initBackToTop();
});

// ==========================================================================
// 1. SPEAKER BIOS DATABASE (12 DIGNITARIES & LEADERS - 100% ENGLISH)
// ==========================================================================
const SPEAKER_BIOS = {
  'le-quang-dam': {
    name: 'Dr. Le Quang Dam',
    title: 'General Director',
    org: 'Marvell Technology Vietnam Co., Ltd.',
    tag: 'STRATEGIC KEYNOTE 1 / HOST LEADERSHIP',
    photo: 'images/speakers/le-quang-dam.jpg?v=20260922_0900',
    avatarText: 'QD',
    colorClass: 'text-[#00b5e2] border-cyan-500/50 bg-blue-950/80',
    bio: 'Quang-Dam (QD) Le is the General Director of Marvell Technology Vietnam, bringing over three decades of engineering leadership, technical depth, and global vision to the semiconductor industry. Since joining Marvell in 2011, QD has held key executive roles—including Technical Director, Associate Vice President, and Vice President—before taking on his current position leading the company’s operations and strategic growth in Vietnam.\n\nQD began his career as an algorithm designer specializing in Digital Signal Processing (DSP) IPs at Miranda Technologies and Gennum Corporation. He later joined ATI Technologies (acquired by AMD) as Senior Manager, directing multi-regional DSP engineering teams across Canada, India, China, and Germany. Prior to Marvell, he served as a Senior Principal Scientist at Broadcom. An active contributor to the field, QD holds several worldwide patents and has authored numerous technical papers.\n\nQD holds a Bachelor of Science from Ho Chi Minh City University of Science (HCMUS), followed by a Master’s in Physics and a Doctorate in Signal Processing with a focus on Artificial Intelligence from Canada. Grounded in his technical foundation, QD remains deeply passionate about advancing system architecture, signal processing, and AI technologies.',
    sessions: [
      {
        time: '09:00 - 09:10',
        title: 'Opening Remarks (with Mr. Noam Mizrahi)',
        room: 'Plenary Hall',
        category: 'Opening Speech'
      },
      {
        time: '09:30 - 10:10',
        title: 'Marvell Semiconductor Leadership & Vietnam Vision',
        room: 'Plenary Hall',
        category: 'Strategic Keynote'
      },
      {
        time: '16:55 - 17:05',
        title: 'Closing Strategic Remarks (with Mr. Noam Mizrahi)',
        room: 'Plenary Hall',
        category: 'Closing Ceremony'
      }
    ]
  },
  'noam-mizrahi': {
    name: 'Mr. Noam Mizrahi',
    title: 'Executive VP & Corporate Chief Technology Officer (CTO)',
    org: 'Marvell Technology, Inc. (NASDAQ: MRVL)',
    tag: 'PANEL HOST / SUMMIT CO-HOST',
    photo: 'images/speakers/noam-mizrahi.jpg',
    avatarText: 'NM',
    colorClass: 'text-[#00b5e2] border-cyan-500/50 bg-blue-950/80',
    bio: 'Noam Mizrahi is Executive Vice President and Chief Technology Officer (CTO) at Marvell Technology. With over 25 years of engineering leadership, he orchestrates Marvell’s long-term technology vision, pioneering domain-specific compute architectures, advanced multi-die modular packaging (Chiplets), and optical interconnects (CPO) engineered for the accelerated AI cloud era.',
    sessions: [
      {
        time: '09:00 - 09:10',
        title: 'Opening Remarks (with Dr. Le Quang Dam)',
        room: 'Plenary Hall',
        category: 'Ceremony'
      },
      {
        time: '16:15 - 16:55',
        title: 'Strategic Plenary Panel: Building Vietnam\'s National Semiconductor Value Chain (Panel Host & Moderator)',
        room: 'Plenary Hall',
        category: 'High-Level Panel'
      },
      {
        time: '16:55 - 17:05',
        title: 'Closing Strategic Remarks (with Dr. Le Quang Dam)',
        room: 'Plenary Hall',
        category: 'Closing Ceremony'
      }
    ]
  },
  'nguyen-van-duoc': {
    name: 'Mr. Nguyen Van Duoc',
    title: 'Chairman',
    org: 'Ho Chi Minh City People\'s Committee',
    tag: 'GUEST OF HONOR / GOVERNMENT',
    photo: 'images/speakers/nguyen-van-duoc.jpg',
    avatarText: 'NVD',
    colorClass: 'text-emerald-400 border-emerald-500/50 bg-emerald-950/80',
    bio: 'Chairman of Ho Chi Minh City People\'s Committee (2026–2031 tenure), spearheading municipal initiatives to position HCMC as a regional powerhouse for IC design incubation, semiconductor R&D, and high-tech innovation.',
    sessions: [
      {
        time: '09:10 - 09:20',
        title: 'Summit Inaugural Address: Strategy for HCMC High-Tech & Silicon Ecosystem',
        room: 'Plenary Hall',
        category: 'Opening Speech'
      }
    ]
  },
  'melissa-brown': {
    name: 'Ms. Melissa A. Brown',
    title: 'U.S. Consul General in Ho Chi Minh City',
    org: 'U.S. Diplomatic Mission to Vietnam',
    tag: 'DIPLOMATIC MISSION / STRATEGIC PARTNER',
    photo: 'images/speakers/melissa-brown.jpg',
    avatarText: 'MB',
    colorClass: 'text-amber-400 border-amber-500/50 bg-amber-950/80',
    bio: 'Senior representative of the United States government in Southern Vietnam, driving forward the U.S.–Vietnam Comprehensive Strategic Partnership in semiconductor supply chain resilience and advanced technology workforce initiatives.',
    sessions: [
      {
        time: '09:20 - 09:30',
        title: 'Diplomatic Address: U.S. - Vietnam Comprehensive Strategic Partnership',
        room: 'Plenary Hall',
        category: 'Opening Speech'
      }
    ]
  },
  'nguyen-bich-yen': {
    name: 'Ms. Bich-Yen Nguyen',
    title: 'Senior Fellow (IEEE Fellow) & Co-Founder',
    org: 'VSAP-LAB / Soitec',
    tag: 'STRATEGIC KEYNOTE 2 / ADVANCED PACKAGING',
    photo: 'images/speakers/bich-yen-nguyen.jpg',
    avatarText: 'BYN',
    colorClass: 'text-[#00b5e2] border-cyan-500/50 bg-blue-950/80',
    bio: 'Bich-Yen Nguyen is a distinguished Vietnamese electronics engineer recognized for pioneering contributions to advanced materials and integrated circuit technologies. She earned a bachelor’s degree in Chemical Engineering from The University of Texas at Austin in 1977. Beginning her career at Motorola in 1980, she contributed to CMOS and MIGFET development and later held a leadership role in the Crolles Alliance. In 2007, she joined Soitec as a Senior Fellow, advancing silicon-on-insulator (SOI) technologies widely adopted in smartphones and other applications. Her honors include Motorola’s Dan Noble Fellow distinction, the 2004 National Women in Technology Lifetime Achievement Award, IEEE Fellow elevation in 2020, and the 2024 IEEE Frederik Philips Award. In 2025, she co-founded VSAP Lab, launching Vietnam’s first advanced semiconductor packaging lab-fab project. She holds more than 230 patents worldwide and has authored over 350 scientific publications on semiconductor processes, devices, integration, and integrated circuits.',
    sessions: [
      {
        time: '13:50 - 14:30',
        title: 'From Assembly to Advanced Packaging Integration: Strategic Ascent in the Global Semiconductor Value Chain',
        room: 'Plenary Hall',
        category: 'Strategic Keynote'
      }
    ],
    abstract: 'The semiconductor industry is entering a new era where performance gains are driven not only by transistor scaling, but increasingly by advanced packaging, chiplets, heterogeneous integration, materials innovation, and system-level co-design. This shift is redefining value creation in the semiconductor ecosystem and opening strategic opportunities for countries that can position themselves in integration, packaging, and system-level manufacturing.\n\nVietnam is well positioned to benefit from this transition. With a growing electronics manufacturing base, an expanding assembly and test ecosystem, a competitive workforce, and increasing participation from global technology companies, Vietnam is emerging as a credible node in global semiconductor production networks. The strategic imperative is therefore not mere entry, but upward mobility—moving from manufacturing participation toward higher-value activities in advanced packaging, design support, and system integration.\n\nThis plenary outlines a practical pathway for Vietnam’s semiconductor development—from assembly and testing toward advanced packaging, system-in-package (SiP), and heterogeneous integration—supported by capability building, workforce development, and stronger local supplier ecosystems. A key focus is the complementarity between Vietnam and Japan: Japan’s strengths in materials, precision equipment, manufacturing quality, and process expertise align with Vietnam’s scale, talent base, and industrial growth, enabling collaboration in technology transfer, training, and supply chain resilience.\n\nThe core message is clear: Vietnam’s opportunity is not to replicate the entire semiconductor value chain, but to strategically position itself in the fastest-growing, highest-value segments. By building on its manufacturing foundation and deepening collaboration with trusted partners in Asia such as Japan, Singapore, Vietnam can accelerate its transition toward a high-value, innovation-driven role in the global semiconductor ecosystem.'
  },
  'tran-dac-khoa': {
    name: 'Mr. Tran Dac Khoa',
    title: 'General Director',
    org: 'Renesas Design Vietnam Co., Ltd.',
    tag: 'INDUSTRY / AUTOMOTIVE IC & SDV',
    photo: 'images/speakers/khoa-tran.jpg',
    avatarText: 'TDK',
    colorClass: 'text-[#00b5e2] border-cyan-500/50 bg-blue-950/80',
    bio: 'Tran Dac Khoa, General Director of Renesas Design Vietnam, joined the company in 2005 as part of its first generation of engineers. He holds a bachelor’s degree in Electronics–Telecommunications from Ho Chi Minh City University of Technology (HCMUT) and brings over 20 years of semiconductor design experience. With deep expertise in System-on-Chip (SoC) hardware, he has contributed to major automotive projects and presented at A-SSCC 2008 in Japan. As the first Vietnamese General Director, he has expanded Renesas Vietnam’s role as a vital global R&D hub while actively fostering local engineering talent through university partnerships.',
    sessions: [
      {
        time: '14:30 - 14:55',
        title: 'Advance the Development of System-on-Chip Architectures for Software-Defined Vehicles',
        room: 'Plenary Hall',
        category: 'Industry Presentation'
      }
    ],
    abstract: 'The automotive industry is moving from distributed electronic control units to centralized and zonal compute architectures, enabling powerful central processors to support infotainment, Advanced Driver Assistance Systems (ADAS), gateway, and vehicle control workloads on a shared platform. This shift accelerates software-defined vehicles (SDVs), improves safety, and promotes software reuse across vehicle generations. Renesas’ scalable monolithic R-Car SoC integrates multi-die chiplet technology to provide a flexible, software-upgradable platform for ADAS, cockpit, infotainment, and cross-domain computing. With a common architecture, it helps centralize ECU layouts, streamline vehicle development, and future-proof designs across multiple vehicle classes. Its open development platform also combines open-source software with partner intellectual property, supporting continuous updates and enhanced environmental response capabilities required for increasingly autonomous vehicles.'
  },
  'hoang-trang': {
    name: 'Assoc. Prof. Trang Hoang, Ph.D.',
    title: 'Head of Examination & QA Office, Senior IC Design Faculty',
    org: 'Ho Chi Minh City University of Technology (HCMUT), VNU-HCM',
    tag: 'ACADEMIA / QUANTUM & AI IC DESIGN',
    photo: 'images/speakers/hoang-trang.jpg?v=20260922_0900',
    avatarText: 'TH',
    colorClass: 'text-emerald-400 border-emerald-500/50 bg-emerald-950/80',
    bio: 'Trang Hoang is an Associate Professor and Head of the Examination and Quality Assurance Office at Ho Chi Minh City University of Technology (HCMUT), VNU-HCM. He received his Ph.D. in Microelectronics from Université Joseph Fourier and CEA-LETI, France. Working on AI and quantum computing for IC design, he has led ten research projects (three national-level), published over 110 papers, edited 2 IEEE Press–Wiley books, 8 textbooks, and obtained 2 U.S. patents and 4 Vietnamese patents. He chaired the development of HCMUT\'s IC design programs. An IEEE Senior Member and Executive Committee member of the Ho Chi Minh City Semiconductor Industry Association (HSIA), he received the 2025 Hitachi Global Foundation Asia Innovation Award and VNU-HCM Outstanding Publication Awards (2024, 2025).',
    sessions: [
      {
        time: '14:55 - 15:20',
        title: 'Toward Quantum–AI-Driven IC Design: Research at HCMUT, VNU-HCM',
        room: 'Plenary Hall',
        category: 'Academia & Research'
      }
    ],
    abstract: 'Integrated circuit design remains time-consuming, expert-dependent and simulation-intensive, while many AI solutions reported so far are tailored to specific circuits. This talk presents how our group at Ho Chi Minh City University of Technology (HCMUT) develops AI and quantum computing methods for IC design within a general simulation-in-the-loop framework that couples learning and optimization algorithms with industrial circuit simulators, designed to scale from simple circuits to multi-block designs. Examples include improved swarm and evolutionary optimizers for analog circuit sizing, multi-agent reinforcement learning for low-dropout regulators and delta-sigma modulators, and quantum evolutionary algorithms embedded in the design flow, covered by a U.S. patent. We then outline our next steps: hybrid quantum–classical learning, neural-network models for IC design, and extending these methods toward fabrication, in line with Vietnam\'s strategic priorities in semiconductors, AI and quantum technologies. The talk also introduces HCMUT, VNU-HCM.'
  },
  'loan-nguyen': {
    name: 'Ms. Loan Nguyen',
    title: 'Co-Founder & Chief Executive Officer (CEO)',
    org: 'Connexus',
    tag: 'INDUSTRY STARTUP / SILICON OWNERSHIP',
    photo: 'images/speakers/loan-nguyen.jpg?v=20260922_0900',
    avatarText: 'LN',
    colorClass: 'text-[#00b5e2] border-cyan-500/50 bg-blue-950/80',
    bio: 'Loan Nguyen holds a Master’s in Economics from ESCP Business School, Paris. With more than 18 years of executive experience, she has built her career at the intersection of corporate governance, growth strategy, digital transformation, and technology-driven business management, holding C-suite and leadership roles at Bamboo Capital Group, Philip Morris International, and The HEINEKEN Company.\n\nAs Co-Founder & CEO of Connexus, she channels cross-industry executive experience to drive innovation, operational excellence, and growth in the semiconductor and AI industries. She leads Connexus’s mission to turn Vietnamese engineering talent into globally relevant, owned technology, from AI accelerator chips to AI-powered automation platforms for SoC design.',
    sessions: [
      {
        time: '15:20 - 15:45',
        title: 'Vietnam\'s Semiconductor Moment: From Talent to Ownership',
        room: 'Plenary Hall',
        category: 'Industry Presentation'
      }
    ],
    abstract: 'Vietnam has spent two decades building world-class semiconductor engineering talent, but talent alone doesn\'t make an industry. The real question is: what are we going to build with it? Can a Vietnamese company move beyond design services and actually own IP, own products, own the upside?\n\nThis talk explores why the answer is increasingly yes, and why AI is making that transition possible faster than ever. As AI reshapes chip design itself, new tools and approaches are lowering the barriers to creating original silicon, opening opportunities for smaller, ambitious teams to compete on technology and products, not just scale.\n\nFrom semiconductor IP and AI accelerator chips to AI-powered SoC design automation, the presentation examines what Vietnam’s next generation of engineers can build. The Connexus journey offers one example: turning Vietnamese engineering talent into owned, globally relevant technology, built in Vietnam, for the world.'
  },
  'nguyen-quang-khanh': {
    name: 'Mr. Nguyen Quang Khanh',
    title: 'General Factory Director (Engineering & Operation)',
    org: 'Intel Products Vietnam (IPV)',
    tag: 'INDUSTRY / IC FABRICATION & ATP',
    photo: '',
    avatarText: '',
    colorClass: 'text-[#00b5e2] border-cyan-500/50 bg-blue-950/80',
    bio: '',
    sessions: [
      {
        time: '11:30 - 11:55',
        title: 'IC Fabrication & ATP Engineering in Global Supply Chain',
        room: 'Plenary Hall',
        category: 'Industry Presentation'
      }
    ]
  },
  'phong-vo': {
    name: 'Mr. Vo Phong',
    title: 'General Director',
    org: 'Ampere Computing Vietnam',
    tag: 'INDUSTRY / CLOUD ARM CPU',
    photo: 'images/speakers/phong-vo.jpg',
    avatarText: 'PV',
    colorClass: 'text-[#00b5e2] border-cyan-500/50 bg-blue-950/80',
    bio: 'General Director of Ampere Computing Vietnam, leading engineering operations for energy-efficient, high-core-count ARM server microprocessors powering hyperscale cloud datacenters globally.',
    sessions: [
      {
        time: '10:10 - 10:35',
        title: 'Next-Generation Arm Server Silicon & Cloud Workloads',
        room: 'Plenary Hall',
        category: 'Industry Presentation'
      }
    ]
  },
  'pham-nguyen-thanh-loan': {
    name: 'Assoc. Prof. Dr. Pham Nguyen Thanh Loan',
    title: 'Head of IC Design & Embedded Systems Laboratory',
    org: 'Hanoi University of Science and Technology (HUST - SEEE)',
    tag: 'ACADEMIA / ANALOG & RF IC',
    photo: 'images/speakers/pham-nguyen-thanh-loan.jpg',
    avatarText: 'PTL',
    colorClass: 'text-emerald-400 border-emerald-500/50 bg-emerald-950/80',
    bio: 'Head of the IC Design and Embedded Systems Laboratory at the School of Electrical & Electronic Engineering (SEEE), HUST. She is a foremost researcher in analog and mixed-signal microelectronics, leading national collaborative research in high-frequency wireless communications.',
    sessions: [
      {
        time: '10:35 - 11:00',
        title: 'Analog IC Design & Mixed-Signal IC Research',
        room: 'Plenary Hall',
        category: 'Academia & Research'
      }
    ]
  },
  'thieu-phuong-nam': {
    name: 'Mr. Vo Thieu Nam',
    title: 'General Director',
    org: 'Qualcomm Vietnam, Cambodia & Laos',
    tag: 'INDUSTRY / CONNECTIVITY & EDGE AI',
    photo: 'images/speakers/thieu-phuong-nam.jpg',
    avatarText: 'VTN',
    colorClass: 'text-[#00b5e2] border-cyan-500/50 bg-blue-950/80',
    bio: 'General Director of Qualcomm Vietnam, Cambodia & Laos, directing Qualcomm’s business, R&D alliances, and engineering initiatives in edge AI silicon, 5G/6G wireless communications, and IoT platforms.',
    sessions: [
      {
        time: '11:55 - 12:20',
        title: 'Next-Gen Mobile Connectivity Silicon & Edge AI',
        room: 'Plenary Hall',
        category: 'Industry Presentation'
      }
    ]
  },
  'nguyen-thi-thanh-mai': {
    name: 'Prof. Dr. Nguyen Thi Thanh Mai',
    title: 'President',
    org: 'Vietnam National University, Ho Chi Minh City (VNU-HCM)',
    tag: 'ACADEMIA / WORKFORCE STRATEGY',
    photo: 'images/speakers/nguyen-thi-thanh-mai.jpg',
    avatarText: 'NTM',
    colorClass: 'text-emerald-400 border-emerald-500/50 bg-emerald-950/80',
    bio: 'President of VNU-HCM and eminent scholar, directing strategic talent initiatives to fulfill Vietnam’s national target of developing 50,000 semiconductor engineers by 2030 through university-enterprise alliances with Marvell and global industry partners.',
    sessions: [
      {
        time: '16:15 - 16:55',
        title: 'Strategic Plenary Panel: Building Vietnam\'s National Semiconductor Value Chain',
        room: 'Plenary Hall',
        category: 'High-Level Panel'
      }
    ]
  },
  'nguyen-ky-phung': {
    name: 'Dr. Nguyen Ky Phung',
    title: 'Vice Chairman',
    org: 'Saigon Hi-Tech Park Authority (SHTP)',
    tag: 'DISTINGUISHED PANELIST / SHTP',
    photo: '',
    avatarText: '',
    colorClass: 'text-[#00b5e2] border-cyan-500/50 bg-blue-950/80',
    bio: '',
    sessions: [
      {
        time: '16:15 - 16:55',
        title: 'Strategic Plenary Panel: Building Vietnam\'s National Semiconductor Value Chain',
        room: 'Plenary Hall',
        category: 'High-Level Panel'
      }
    ]
  }
};

// Aliases for backwards-compatibility
SPEAKER_BIOS['qd'] = SPEAKER_BIOS['le-quang-dam'];
SPEAKER_BIOS['vo-phong'] = SPEAKER_BIOS['phong-vo'];
SPEAKER_BIOS['tran-dac-khoa'] = SPEAKER_BIOS['tran-dac-khoa'];
SPEAKER_BIOS['khoa-tran'] = SPEAKER_BIOS['tran-dac-khoa'];
SPEAKER_BIOS['tran-dang-khoa'] = SPEAKER_BIOS['tran-dac-khoa'];
SPEAKER_BIOS['vo-thieu-nam'] = SPEAKER_BIOS['thieu-phuong-nam'];
SPEAKER_BIOS['nguyen-hoang-trang'] = SPEAKER_BIOS['hoang-trang'];
SPEAKER_BIOS['nguyen-loan'] = SPEAKER_BIOS['loan-nguyen'];
SPEAKER_BIOS['pham-loan'] = SPEAKER_BIOS['loan-nguyen'];
SPEAKER_BIOS['mai-thi-thanh-nguyen'] = SPEAKER_BIOS['nguyen-thi-thanh-mai'];
SPEAKER_BIOS['ky-phung'] = SPEAKER_BIOS['nguyen-ky-phung'];

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
      const categoryMatch = (currentCategory === 'all') || (cardCategory === currentCategory) || (currentCategory === 'keynote' && (cardCategory === 'opening' || cardCategory === 'closing'));

      if (sessionMatch && categoryMatch) {
        card.style.display = '';
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
        p.classList.remove('active', 'border-[#0072ce]', 'text-[#0072ce]', 'bg-blue-50', 'font-semibold', 'shadow-sm');
        p.classList.add('border-slate-200', 'bg-white', 'text-slate-600');
      });
      pill.classList.add('active', 'border-[#0072ce]', 'text-[#0072ce]', 'bg-blue-50', 'font-semibold', 'shadow-sm');
      pill.classList.remove('border-slate-200', 'bg-white', 'text-slate-600');

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
    const tagEl = document.getElementById('speaker-modal-tag');
    if (tagEl) tagEl.innerText = speaker.tag || '';
    
    const avatarEl = document.getElementById('speaker-modal-avatar');
    const imgEl = document.getElementById('speaker-modal-img');
    if (speaker.avatarText) {
      avatarEl.innerText = speaker.avatarText;
    } else {
      avatarEl.innerHTML = `<svg class="w-16 h-16 text-slate-400 opacity-60" fill="currentColor" viewBox="0 0 24 24"><path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"/></svg>`;
    }

    if (speaker.photo) {
      if (imgEl) {
        imgEl.src = speaker.photo;
        imgEl.alt = speaker.name;
        imgEl.classList.remove('hidden');
      }
      avatarEl.classList.add('hidden');
    } else {
      if (imgEl) {
        imgEl.src = '';
        imgEl.classList.add('hidden');
      }
      avatarEl.classList.remove('hidden');
    }

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

    if (speaker.abstract) {
      const absContainer = document.createElement('div');
      absContainer.className = 'mt-3 p-4 rounded-xl bg-[#0a0e17] border border-cyan-500/20';
      absContainer.innerHTML = `
        <span class="text-[11px] font-bold text-[#00b5e2] uppercase tracking-wider block mb-1.5 flex items-center gap-1.5">
          <svg class="w-3.5 h-3.5 text-[#00b5e2]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>
          Presentation Abstract
        </span>
        <div class="text-xs text-slate-300 leading-relaxed max-h-48 overflow-y-auto pr-1">
          <p>${speaker.abstract.replace(/\n\n/g, '</p><p class="mt-2">').replace(/\n/g, '<br>')}</p>
        </div>
      `;
      sessionsContainer.appendChild(absContainer);
    }

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

// ==========================================================================
// 12. SMART HEADER AUTO-HIDE ON SCROLL DOWN & SHOW ON SCROLL UP
// ==========================================================================
function initSmartHeader() {
  const header = document.getElementById('main-header');
  if (!header) return;

  let lastScrollY = window.pageYOffset || document.documentElement.scrollTop;
  const threshold = 80;

  window.addEventListener('scroll', () => {
    const currentScrollY = window.pageYOffset || document.documentElement.scrollTop;
    
    // Always show near top
    if (currentScrollY <= threshold) {
      header.classList.remove('-translate-y-full');
      lastScrollY = currentScrollY;
      return;
    }

    // Scroll down -> hide
    if (currentScrollY > lastScrollY && currentScrollY > threshold) {
      header.classList.add('-translate-y-full');
    } else {
      // Scroll up -> show
      header.classList.remove('-translate-y-full');
    }

    lastScrollY = currentScrollY;
  }, { passive: true });
}

// ==========================================================================
// 13. BACK TO TOP BUTTON
// ==========================================================================
function initBackToTop() {
  const backToTopBtn = document.getElementById('back-to-top-btn');
  if (!backToTopBtn) return;

  window.addEventListener('scroll', () => {
    const currentScrollY = window.pageYOffset || document.documentElement.scrollTop;
    if (currentScrollY > 300) {
      backToTopBtn.classList.remove('opacity-0', 'pointer-events-none', 'translate-y-4');
      backToTopBtn.classList.add('opacity-100', 'pointer-events-auto', 'translate-y-0');
    } else {
      backToTopBtn.classList.add('opacity-0', 'pointer-events-none', 'translate-y-4');
      backToTopBtn.classList.remove('opacity-100', 'pointer-events-auto', 'translate-y-0');
    }
  }, { passive: true });

  backToTopBtn.addEventListener('click', () => {
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  });
}


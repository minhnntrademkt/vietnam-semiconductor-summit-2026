# -*- coding: utf-8 -*-
"""
The 1st Vietnam Semiconductor Summit 2026 - Site Generator
Host Organization: Marvell Technology, Inc. (NASDAQ: MRVL)
Language: 100% International Standard English
Design System: Marvell Design System (Hierarchical Radius, Ambient Shadows, Glassmorphism)
"""
import json
import os

base_dir = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(base_dir, 'agenda.json'), 'r', encoding='utf-8') as f:
    agenda_data = json.load(f)

agenda_cards_html = []
for item in agenda_data:
    session = item['session']
    category = item['category']
    tag_label = category.upper()
    
    if category == 'keynote':
        tag_label = 'STRATEGIC KEYNOTE'
        tag_class = 'bg-blue-50 text-blue-700 border border-blue-200'
    elif category == 'industry':
        tag_label = 'INDUSTRY PRESENTATION'
        tag_class = 'bg-cyan-50 text-cyan-800 border border-cyan-200'
    elif category == 'academia':
        tag_label = 'ACADEMIA & RESEARCH'
        tag_class = 'bg-emerald-50 text-emerald-800 border border-emerald-200'
    elif category == 'networking':
        tag_label = 'NETWORKING & BANQUET'
        tag_class = 'bg-amber-50 text-amber-800 border border-amber-200'
    elif category == 'panel':
        tag_label = 'HIGH-LEVEL PANEL'
        tag_class = 'bg-purple-50 text-purple-800 border border-purple-200'
    else:
        tag_label = 'CEREMONY & RECEPTION'
        tag_class = 'bg-slate-100 text-slate-700 border border-slate-200'

    notes_html = ""
    if item['notes']:
        notes_html = f'''
        <div class="mt-2.5 text-xs text-slate-600 flex items-start gap-2 bg-slate-50/80 p-3 rounded-lg border border-slate-200/80">
          <svg class="w-4 h-4 text-[#0072ce] shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
          <span class="whitespace-pre-line leading-relaxed font-medium">{item['notes']}</span>
        </div>
        '''

    agenda_cards_html.append(f'''
    <div class="agenda-item-card flex flex-col md:flex-row md:items-center justify-between p-5 sm:p-6 rounded-xl bg-white border border-slate-200 hover:border-[#0072ce] hover:shadow-lg transition-all duration-300 gap-4" data-session="{session}" data-category="{category}">
      <div class="flex items-start gap-4 flex-1">
        <div class="shrink-0 w-32 bg-slate-50 border border-slate-200 rounded-lg px-3.5 py-2.5 text-center">
          <span class="block font-mono text-sm font-bold text-[#0072ce]">{item['from']} - {item['to']}</span>
          <span class="text-[11px] text-slate-500 font-mono">({item['duration'][:5]})</span>
        </div>
        <div class="flex-1">
          <div class="flex flex-wrap items-center gap-2 mb-2">
            <span class="text-[10px] font-bold tracking-wider uppercase px-2.5 py-0.5 rounded-md {tag_class}">{tag_label}</span>
          </div>
          <h4 class="text-base font-bold text-slate-900 leading-snug">{item['description']}</h4>
          {notes_html}
        </div>
      </div>
    </div>
    ''')

agenda_items_rendered = '\n'.join(agenda_cards_html)

MARVELL_SVG_PATH = '''M425.9,98.4l-33.7,53.9l-33.3-53.9H344v91h14.9v-58.6c0-1.1,0-2.2-0.1-3.3s-0.1-2.2-0.3-3.5c0.7,1.9,1.8,4,3.1,6l24.2,38.9
	h12l24-38.9c0.6-1,1.2-1.9,1.9-2.9s1.3-2,1.9-3.1c-0.1,1.2-0.2,2.4-0.3,3.5c-0.1,1.1-0.1,2.2-0.1,3.3v58.6h14.7v-91L425.9,98.4
	L425.9,98.4z M471.8,189.4l29.3-71.5c0.2-0.7,0.5-1.5,0.8-2.3c0.3-0.8,0.6-1.7,0.8-2.8c0.2,1.1,0.5,2,0.8,2.8
	c0.3,0.8,0.6,1.6,0.8,2.3l16,38.9H486l8.9,13.3h30.8l8,19.3h15.7l-38.4-91h-16l-38.4,91H471.8L471.8,189.4z M701.1,189.4l37-91h-16
	L696,167c-0.8,2.3-1.7,5-2.5,8c-0.8-3-1.7-5.7-2.5-8l-26-68.6h-16.7l37,91H701.1L701.1,189.4z M842.1,98.4v91h59.3v-13.5h-44.4V98.4
	H842.1L842.1,98.4z M919.5,98.4v91h59.9v-13.5h-45V98.4H919.5L919.5,98.4z M769.9,111.9h47.7V98.4h-62.4v91h63.3v-13.5h-48.6V111.9
	L769.9,111.9z M637.2,125.7c0-8.5-2.6-15.2-7.9-20c-5.3-4.8-14.1-7.3-26.5-7.3h-37.1v91h14.9v-77.5h22.8c12.2,0,18.4,5,18.4,15.1
	c0,10.8-6.6,16.2-19.8,16.2h-12l-8.5,13.1h20.2l25.1,33.1h18L617.2,153C630.5,148.2,637.2,139.1,637.2,125.7L637.2,125.7
	L637.2,125.7z M811.2,137h-40.4l9.1,13.5h31.3L811.2,137L811.2,137z M111.9,111.1l30.1,30.8c0.7,0.7,1.4,1.1,2,1.1
	c0.6,0,1.3-0.4,2-1.1l30.1-30.8c0.7-0.7,1.1-1.4,1.1-2c0-1-0.5-1.4-1.6-1.4h-63.1c-1.1,0-1.6,0.5-1.6,1.4
	C110.8,109.7,111.2,110.4,111.9,111.1L111.9,111.1z M288,1.6c0-1.1-0.5-1.6-1.5-1.6c-0.6,0-1.2,0.3-1.8,0.9l-24.7,25v236l0,0
	l24.7,25.2c0.6,0.6,1.2,0.9,1.8,0.9c1,0,1.5-0.5,1.5-1.6V1.6z M0,286.4c0,1.1,0.5,1.6,1.5,1.6c0.6,0,1.2-0.3,1.8-0.9l24.7-25.2l0,0
	v-236L3.3,0.9C2.7,0.3,2,0,1.5,0C0.5,0,0,0.5,0,1.6V286.4z M64.2,62.8h159.7L246.3,40c0.6-0.6,0.9-1.2,0.9-1.8c0-1-0.5-1.5-1.6-1.5
	H42.4c-1.1,0-1.6,0.5-1.6,1.5c0,0.6,0.3,1.2,0.9,1.8L64.2,62.8z M41.7,248c-0.6,0.6-0.9,1.2-0.9,1.8c0,1,0.5,1.4,1.6,1.4h203.1
	c1.1,0,1.6-0.5,1.6-1.4c0-0.6-0.3-1.2-0.9-1.8l-22.4-22.8H64.2L41.7,248z M211.8,213c0.6,0.6,1.2,0.9,1.8,0.9c1,0,1.4-0.5,1.4-1.6
	l0,0V75.7c0-1.1-0.5-1.6-1.4-1.6c-0.6,0-1.2,0.3-1.8,0.9l-23.4,23.8v90.5L211.8,213z M99.6,189.2V98.8L76.2,75
	c-0.6-0.6-1.2-0.9-1.8-0.9c-1,0-1.4,0.6-1.4,1.6v136.6l0,0c0,1.1,0.5,1.6,1.4,1.6c0.6,0,1.2-0.3,1.8-0.9L99.6,189.2z M978.8,98.4
	v1.7h4.2v9.8h1.9v-9.8h4.2v-1.7H978.8z M1001.8,98.4l-4.3,6.8l-4.2-6.8h-1.9v11.5h1.9v-7.4c0-0.1,0-0.3,0-0.4c0-0.1,0-0.3,0-0.4
	c0.1,0.2,0.2,0.5,0.4,0.8l3.1,4.9h1.5l3-4.9c0.1-0.1,0.2-0.2,0.2-0.4s0.2-0.2,0.2-0.4c0,0.2,0,0.3,0,0.4c0,0.1,0,0.3,0,0.4v7.4h1.9
	V98.4H1001.8L1001.8,98.4z'''

def get_marvell_logo(css_class="h-7 w-auto", fill_color="#0072ce"):
    return f'<svg class="{css_class}" viewBox="0 0 1004 288" fill="{fill_color}" aria-label="Marvell Technology Logo"><path d="{MARVELL_SVG_PATH}"/></svg>'

marvell_logo_header = get_marvell_logo("h-6 sm:h-7 w-auto", "#0072ce")
marvell_logo_footer = get_marvell_logo("h-6 w-auto", "#0072ce")
marvell_logo_ticket = get_marvell_logo("h-5 w-auto", "#00b5e2")
marvell_logo_partner = get_marvell_logo("h-7 w-auto", "#0072ce")
marvell_logo_host_card = get_marvell_logo("h-9 sm:h-10 w-auto", "#0072ce")

html_content = f'''<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>The 1st Vietnam Semiconductor Summit 2026 | Marvell Technology</title>
  <meta name="description" content="Inaugural Vietnam Semiconductor Summit hosted by Marvell Technology, Inc. Uniting Government leadership, global semiconductor corporations, and premier research universities. 100% Free RSVP.">
  
  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      theme: {{
        extend: {{
          colors: {{
            mrvll: {{
              blue: '#0072ce',
              blueDark: '#005fa3',
              cyan: '#00b5e2',
              lavender: '#c8a3ef',
              dark: '#05070a',
              cardDark: '#101726'
            }}
          }},
          fontFamily: {{
            sans: ['"Plus Jakarta Sans"', 'Inter', 'system-ui', 'sans-serif']
          }}
        }}
      }}
    }}
  </script>
  
  <!-- Google Fonts: Plus Jakarta Sans & Inter -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  
  <!-- Marvell Official Favicon & Brand Identity -->
  <link rel="icon" type="image/svg+xml" href="marvell-logo.svg">
  
  <!-- Marvell Custom Design Tokens -->
  <link rel="stylesheet" href="styles.css">
</head>
<body class="bg-white text-slate-900 antialiased selection:bg-[#0072ce] selection:text-white">

  <!-- Top Scroll Reading Progress Bar -->
  <div id="scroll-progress-bar"></div>

  <!-- =========================================================================
       1. TOP BAR & NAVIGATION (STICKY HEADER - MARVELL CRISP WHITE)
       ========================================================================= -->
  <header class="sticky top-0 z-50 bg-white/95 backdrop-blur-md border-b border-slate-200 shadow-sm transition-all">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-20 flex items-center justify-between">
      
      <!-- Brand Logo & Summit Title -->
      <a href="#" class="flex items-center gap-3.5 group">
        <div class="flex items-center">
          <!-- Marvell Brand Mark Official Vector -->
          {marvell_logo_header}
        </div>
        <div class="h-6 w-px bg-slate-300"></div>
        <div class="flex flex-col">
          <span class="text-xs font-extrabold tracking-wider text-slate-900 uppercase">Vietnam Semiconductor Summit</span>
          <span class="text-[10px] text-[#0072ce] tracking-widest font-mono font-bold">2026 INAUGURAL EDITION</span>
        </div>
      </a>

      <!-- Desktop Nav Links -->
      <nav class="hidden lg:flex items-center gap-7 text-sm font-semibold text-slate-700">
        <a href="#about" class="hover:text-[#0072ce] transition-colors">About Summit</a>
        <a href="#speakers" class="hover:text-[#0072ce] transition-colors">Speakers</a>
        <a href="#panel" class="hover:text-[#0072ce] transition-colors">Strategic Panel</a>
        <a href="#agenda" class="hover:text-[#0072ce] transition-colors">Full Agenda</a>
        <a href="#partners" class="hover:text-[#0072ce] transition-colors">Partners</a>
        <a href="#faq" class="hover:text-[#0072ce] transition-colors">FAQ</a>
      </nav>

      <!-- CTA Register Button (Marvell Black Kinetic Button with Soft Radius) -->
      <div class="hidden sm:flex items-center gap-4">
        <a href="#register" class="mrvll-btn-black open-rsvp-modal-btn">
          <span>REGISTER FOR FREE</span>
          <svg class="btn-arrow w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
        </a>
      </div>

      <!-- Mobile Hamburger Button -->
      <button id="mobile-menu-btn" class="lg:hidden p-2 text-slate-800 hover:text-black">
        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16m-7 6h7"/></svg>
      </button>
    </div>
  </header>

  <!-- Mobile Drawer Menu -->
  <div id="mobile-nav-menu" class="fixed inset-0 z-50 bg-white/98 backdrop-blur-lg hidden flex-col p-6 lg:hidden border-b border-slate-200">
    <div class="flex items-center justify-between mb-8 pb-4 border-b border-slate-200">
      <span class="text-sm font-bold tracking-wider text-slate-900">NAVIGATION MENU</span>
      <button id="mobile-menu-close" class="p-2 text-slate-600 hover:text-black">
        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
      </button>
    </div>
    <div class="flex flex-col gap-5 text-lg font-semibold text-slate-800">
      <a href="#about" class="mobile-link hover:text-[#0072ce]">About Summit</a>
      <a href="#speakers" class="mobile-link hover:text-[#0072ce]">Distinguished Speakers</a>
      <a href="#panel" class="mobile-link hover:text-[#0072ce]">Strategic Panel</a>
      <a href="#agenda" class="mobile-link hover:text-[#0072ce]">Detailed Agenda</a>
      <a href="#partners" class="mobile-link hover:text-[#0072ce]">Ecosystem & Partners</a>
      <a href="#faq" class="mobile-link hover:text-[#0072ce]">FAQ</a>
    </div>
    <div class="mt-auto pt-6 border-t border-slate-200">
      <a href="#register" class="mobile-link mrvll-btn-black w-full justify-center open-rsvp-modal-btn">
        <span>REGISTER FOR FREE</span>
        <svg class="btn-arrow w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
      </a>
    </div>
  </div>

  <!-- =========================================================================
       2. HERO SECTION (HIGH-CONTRAST PURE BLACK TECH SILICON GLOW)
       ========================================================================= -->
  <section class="relative bg-[#05070a] text-white pt-24 pb-20 lg:pt-32 lg:pb-28 overflow-hidden border-b border-slate-800">
    <!-- Ambient Chip Grid & Glow -->
    <div class="absolute inset-0 bg-hero-grid opacity-30 pointer-events-none"></div>
    <div class="absolute -top-32 -left-32 w-96 h-96 bg-[#0072ce]/20 rounded-full blur-3xl pointer-events-none"></div>
    <div class="absolute top-1/2 -right-32 w-96 h-96 bg-[#c8a3ef]/15 rounded-full blur-3xl pointer-events-none"></div>
    
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10 text-center">
      
      <!-- Top Host Badge -->
      <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-blue-950/70 border border-blue-500/40 text-xs font-bold text-[#00b5e2] tracking-wider uppercase mb-8 shadow-[0_0_15px_rgba(0,181,226,0.2)]">
        <span class="w-2 h-2 rounded-full bg-[#00b5e2] animate-pulse"></span>
        MARVELL TECHNOLOGY PRESENTS • INAUGURAL EDITION
      </div>

      <!-- Main Headline -->
      <h1 class="text-4xl sm:text-5xl lg:text-6xl font-extrabold tracking-tight text-white max-w-5xl mx-auto leading-tight sm:leading-none">
        The 1st Vietnam Semiconductor Summit 2026
      </h1>

      <!-- Strategic Subtitle -->
      <p class="mt-6 text-base sm:text-lg lg:text-xl text-slate-300 max-w-3xl mx-auto font-normal leading-relaxed">
        Pioneering the Next Era of Semiconductor Innovation, Advanced Optical Packaging (CPO) & AI Silicon Infrastructure in Vietnam.
      </p>

      <!-- Key Metadata Cards (Modern Rounded 14px & Translucent Border) -->
      <div class="mt-10 max-w-4xl mx-auto grid grid-cols-1 sm:grid-cols-3 gap-4 text-left">
        
        <div class="p-5 rounded-xl bg-[#101726]/80 border border-slate-800/80 flex items-center gap-3.5 backdrop-blur-md shadow-md">
          <div class="w-11 h-11 rounded-lg bg-blue-600/15 border border-blue-500/30 flex items-center justify-center text-[#00b5e2] shrink-0">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg>
          </div>
          <div>
            <span class="block text-[11px] text-slate-400 uppercase tracking-wider font-semibold">Event Date</span>
            <span class="text-sm font-bold text-white">Mon, Nov 23, 2026</span>
            <span class="text-[10px] text-slate-400 block font-mono">08:00 - 20:10 ICT</span>
          </div>
        </div>

        <div class="p-5 rounded-xl bg-[#101726]/80 border border-slate-800/80 flex items-center gap-3.5 backdrop-blur-md shadow-md">
          <div class="w-11 h-11 rounded-lg bg-purple-600/15 border border-purple-500/30 flex items-center justify-center text-[#c8a3ef] shrink-0">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"/></svg>
          </div>
          <div>
            <span class="block text-[11px] text-slate-400 uppercase tracking-wider font-semibold">Venue</span>
            <span class="text-sm font-bold text-white">Ho Chi Minh City</span>
            <span class="text-[10px] text-slate-400 block">Grand Ballroom & Tech Tracks</span>
          </div>
        </div>

        <div class="p-5 rounded-xl bg-[#101726]/80 border border-slate-800/80 flex items-center gap-3.5 backdrop-blur-md shadow-md">
          <div class="w-11 h-11 rounded-lg bg-emerald-600/15 border border-emerald-500/30 flex items-center justify-center text-emerald-400 shrink-0">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 5v2m0 4v2m0 4v2M5 5a2 2 0 00-2 2v3a2 2 0 110 4v3a2 2 0 002 2h14a2 2 0 002-2v-3a2 2 0 110-4V7a2 2 0 00-2-2H5z"/></svg>
          </div>
          <div>
            <span class="block text-[11px] text-slate-400 uppercase tracking-wider font-semibold">Registration</span>
            <span class="text-sm font-bold text-emerald-400">100% Free RSVP</span>
            <span class="text-[10px] text-slate-400 block">Limited Capacity • Vetted</span>
          </div>
        </div>
      </div>

      <!-- Countdown Timer Box -->
      <div class="mt-10 max-w-lg mx-auto bg-[#090d16]/90 p-6 rounded-xl border border-slate-800/80 shadow-2xl backdrop-blur-lg">
        <span class="block text-xs font-semibold uppercase tracking-widest text-slate-400 mb-3.5">COUNTDOWN TO THE SUMMIT OPENING</span>
        <div class="grid grid-cols-4 gap-3 text-center">
          <div class="bg-[#101726] p-3.5 rounded-lg border border-slate-800">
            <span id="count-days" class="block font-mono text-2xl sm:text-3xl font-extrabold text-[#00b5e2]">--</span>
            <span class="text-[10px] text-slate-400 uppercase font-semibold">Days</span>
          </div>
          <div class="bg-[#101726] p-3.5 rounded-lg border border-slate-800">
            <span id="count-hours" class="block font-mono text-2xl sm:text-3xl font-extrabold text-white">--</span>
            <span class="text-[10px] text-slate-400 uppercase font-semibold">Hours</span>
          </div>
          <div class="bg-[#101726] p-3.5 rounded-lg border border-slate-800">
            <span id="count-mins" class="block font-mono text-2xl sm:text-3xl font-extrabold text-white">--</span>
            <span class="text-[10px] text-slate-400 uppercase font-semibold">Minutes</span>
          </div>
          <div class="bg-[#101726] p-3.5 rounded-lg border border-slate-800">
            <span id="count-secs" class="block font-mono text-2xl sm:text-3xl font-extrabold text-slate-400">--</span>
            <span class="text-[10px] text-slate-400 uppercase font-semibold">Seconds</span>
          </div>
        </div>
      </div>

      <!-- Hero Action Buttons -->
      <div class="mt-10 flex flex-col sm:flex-row items-center justify-center gap-4">
        <a href="#register" class="mrvll-btn-white w-full sm:w-auto justify-center text-sm py-4 px-8 open-rsvp-modal-btn">
          <span>SECURE YOUR SEAT (FREE RSVP)</span>
          <svg class="btn-arrow w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
        </a>
        <a href="#agenda" class="mrvll-btn-outline-white w-full sm:w-auto justify-center text-sm py-4 px-8">
          <span>EXPLORE 24 SESSIONS</span>
          <svg class="btn-arrow w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M19 9l-7 7-7-7"/></svg>
        </a>
      </div>

    </div>
  </section>

  <!-- =========================================================================
       3. METRICS / STATS BAR (CRISP WHITE CORPORATE CLEAN)
       ========================================================================= -->
  <section class="bg-white border-b border-slate-200 py-14">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-2 md:grid-cols-4 gap-8 text-center divide-y md:divide-y-0 md:divide-x divide-slate-200">
        <div class="pt-4 md:pt-0">
          <span class="block text-4xl sm:text-5xl font-extrabold text-[#0072ce] tracking-tight">500+</span>
          <span class="text-xs sm:text-sm font-bold text-slate-800 uppercase tracking-wider mt-2 block">Executive Delegates</span>
          <p class="text-xs text-slate-500 mt-1">C-Level Leaders, Engineers & Scholars</p>
        </div>
        <div class="pt-4 md:pt-0">
          <span class="block text-4xl sm:text-5xl font-extrabold text-slate-900 tracking-tight">24</span>
          <span class="text-xs sm:text-sm font-bold text-slate-800 uppercase tracking-wider mt-2 block">In-Depth Sessions</span>
          <p class="text-xs text-slate-500 mt-1">Keynotes, Tech Tracks & High-Level Panel</p>
        </div>
        <div class="pt-4 md:pt-0">
          <span class="block text-4xl sm:text-5xl font-extrabold text-[#00b5e2] tracking-tight">15+</span>
          <span class="text-xs sm:text-sm font-bold text-slate-800 uppercase tracking-wider mt-2 block">Global Chipmakers & Labs</span>
          <p class="text-xs text-slate-500 mt-1">Marvell, Intel, Qualcomm, Renesas, Ampere</p>
        </div>
        <div class="pt-4 md:pt-0">
          <span class="block text-4xl sm:text-5xl font-extrabold text-purple-700 tracking-tight">1</span>
          <span class="text-xs sm:text-sm font-bold text-slate-800 uppercase tracking-wider mt-2 block">National Strategic Vision</span>
          <p class="text-xs text-slate-500 mt-1">Government, Enterprise & Academia Helix</p>
        </div>
      </div>
    </div>
  </section>

  <!-- =========================================================================
       4. ABOUT THE SUMMIT & 4 PILLARS (LIGHT BACKGROUND #f8fafc)
       ========================================================================= -->
  <section id="about" class="py-20 lg:py-28 bg-[#f8fafc] border-b border-slate-200">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center max-w-3xl mx-auto mb-16">
        <span class="text-xs font-bold tracking-widest text-[#0072ce] uppercase">ABOUT THE INAUGURAL SUMMIT</span>
        <h2 class="text-3xl sm:text-4xl font-extrabold text-slate-900 mt-2 mb-4">Shaping Vietnam's Semiconductor Triple-Helix Ecosystem</h2>
        <p class="text-slate-600 text-sm sm:text-base leading-relaxed">
          Hosted by Marvell Technology, Inc., this premier event convenes high-level Government authorities, global semiconductor multinationals, and top universities to build an autonomous, world-class microelectronics supply chain.
        </p>
      </div>

      <!-- 4 Strategic Pillars Cards -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        
        <div class="mrvll-light-card p-7 rounded-xl bg-white flex flex-col justify-between">
          <div>
            <div class="w-12 h-12 rounded-lg bg-blue-50 border border-blue-200 flex items-center justify-center text-[#0072ce] mb-5">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"/></svg>
            </div>
            <span class="text-[10px] font-bold tracking-widest text-[#0072ce] uppercase">PILLAR 01</span>
            <h3 class="text-lg font-bold text-slate-900 mt-1 mb-2.5">Government & Policy Vision</h3>
            <p class="text-xs text-slate-600 leading-relaxed">Direct strategic insights from Ho Chi Minh City leadership and U.S. Diplomatic Mission on tax incentives, preferential high-tech zones, and national funding.</p>
          </div>
        </div>

        <div class="mrvll-light-card p-7 rounded-xl bg-white flex flex-col justify-between">
          <div>
            <div class="w-12 h-12 rounded-lg bg-cyan-50 border border-cyan-200 flex items-center justify-center text-[#00b5e2] mb-5">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 3v2m6-2v2M9 19v2m6-2v2M5 9H3m2 6H3m18-6h-2m2 6h-2M7 19h10a2 2 0 002-2V7a2 2 0 00-2-2H7a2 2 0 00-2 2v10a2 2 0 002 2zM9 9h6v6H9V9z"/></svg>
            </div>
            <span class="text-[10px] font-bold tracking-widest text-[#00b5e2] uppercase">PILLAR 02</span>
            <h3 class="text-lg font-bold text-slate-900 mt-1 mb-2.5">Advanced Packaging & CPO</h3>
            <p class="text-xs text-slate-600 leading-relaxed">Pioneering Co-Packaged Optics (CPO) architectures, 2.5D/3D Heterogeneous Integration, and high-speed optical interconnects for next-gen silicon.</p>
          </div>
        </div>

        <div class="mrvll-light-card p-7 rounded-xl bg-white flex flex-col justify-between">
          <div>
            <div class="w-12 h-12 rounded-lg bg-purple-50 border border-purple-200 flex items-center justify-center text-[#c8a3ef] mb-5">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/></svg>
            </div>
            <span class="text-[10px] font-bold tracking-widest text-purple-600 uppercase">PILLAR 03</span>
            <h3 class="text-lg font-bold text-slate-900 mt-1 mb-2.5">AI Silicon & Cloud Infrastructure</h3>
            <p class="text-xs text-slate-600 leading-relaxed">Enterprise-grade custom computing architectures, high-density server processors, and ultra-low latency optical fabrics for AI cloud data centers.</p>
          </div>
        </div>

        <div class="mrvll-light-card p-7 rounded-xl bg-white flex flex-col justify-between">
          <div>
            <div class="w-12 h-12 rounded-lg bg-emerald-50 border border-emerald-200 flex items-center justify-center text-emerald-600 mb-5">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l9-5-9-5-9 5 9 5z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0012 20.055a11.952 11.952 0 00-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14z"/></svg>
            </div>
            <span class="text-[10px] font-bold tracking-widest text-emerald-600 uppercase">PILLAR 04</span>
            <h3 class="text-lg font-bold text-slate-900 mt-1 mb-2.5">Talent & Academic R&D</h3>
            <p class="text-xs text-slate-600 leading-relaxed">Cultivating Vietnam's goal of 50,000 semiconductor engineers by 2030 through joint university R&D laboratories, EDA tool sponsorships, and fellowship programs.</p>
          </div>
        </div>

      </div>

    </div>
  </section>

  <!-- =========================================================================
       4B. HOST SPOTLIGHT: MARVELL TECHNOLOGY (CENTER OF EXCELLENCE IN VIETNAM)
       ========================================================================= -->
  <section class="py-20 bg-white border-b border-slate-200">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="bg-gradient-to-br from-slate-900 via-[#0c1322] to-[#0a1b38] rounded-3xl p-8 sm:p-12 lg:p-16 border border-slate-800 shadow-2xl relative overflow-hidden text-left">
        <!-- Ambient Glow -->
        <div class="absolute -top-24 -right-24 w-96 h-96 bg-[#0072ce]/20 rounded-full blur-3xl pointer-events-none"></div>
        <div class="absolute -bottom-24 -left-24 w-96 h-96 bg-[#00b5e2]/15 rounded-full blur-3xl pointer-events-none"></div>

        <div class="relative z-10">
          <div class="flex flex-col lg:flex-row lg:items-center justify-between gap-8 pb-10 border-b border-slate-800/80">
            <div>
              <div class="flex items-center gap-3 mb-4">
                <span class="px-3 py-1 rounded-md bg-blue-950/80 border border-blue-500/40 text-[11px] font-extrabold uppercase tracking-widest text-[#00b5e2]">
                  SUMMIT HOST & LEAD ARCHITECT
                </span>
                <span class="text-slate-400 text-xs font-mono">NASDAQ: MRVL</span>
              </div>
              <h2 class="text-3xl sm:text-4xl font-extrabold text-white tracking-tight">
                Marvell Technology: Powering Global Data Infrastructure
              </h2>
              <p class="text-slate-300 text-sm sm:text-base mt-3 max-w-3xl leading-relaxed">
                For over three decades, Marvell has engineered essential technology that moves, stores, processes, and securely protects the world's data. In Vietnam, Marvell has built a world-class semiconductor R&D powerhouse dedicated to high-speed optical interconnects and AI silicon.
              </p>
            </div>
            <div class="shrink-0 p-5 bg-white rounded-2xl shadow-lg border border-slate-200/20 max-w-[220px]">
              {marvell_logo_host_card}
              <span class="block text-[10px] text-slate-500 font-bold uppercase tracking-wider text-center mt-2.5">
                Essential Technology, Done Right.
              </span>
            </div>
          </div>

          <!-- 3 Feature Pillars of Marvell Vietnam -->
          <div class="grid grid-cols-1 md:grid-cols-3 gap-6 pt-10">
            
            <div class="p-6 rounded-2xl bg-[#101726]/80 border border-slate-800 backdrop-blur-sm">
              <div class="w-10 h-10 rounded-xl bg-blue-600/20 border border-blue-500/40 flex items-center justify-center text-[#00b5e2] mb-4">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"/></svg>
              </div>
              <h3 class="text-base font-bold text-white mb-2">Dual R&D Centers of Excellence</h3>
              <p class="text-xs text-slate-400 leading-relaxed">
                Anchored by the flagship design center in <strong>Ho Chi Minh City</strong> (Tan Thuan EPZ, District 7) and newly expanded facilities in <strong>Da Nang</strong>, forming one of Marvell's top 4 strategic design engineering hubs globally.
              </p>
            </div>

            <div class="p-6 rounded-2xl bg-[#101726]/80 border border-slate-800 backdrop-blur-sm">
              <div class="w-10 h-10 rounded-xl bg-cyan-600/20 border border-cyan-500/40 flex items-center justify-center text-[#00b5e2] mb-4">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 3v2m6-2v2M9 19v2m6-2v2M5 9H3m2 6H3m18-6h-2m2 6h-2M7 19h10a2 2 0 002-2V7a2 2 0 00-2-2H7a2 2 0 00-2 2v10a2 2 0 002 2zM9 9h6v6H9V9z"/></svg>
              </div>
              <h3 class="text-base font-bold text-white mb-2">Pioneering CPO & Optical Silicon</h3>
              <p class="text-xs text-slate-400 leading-relaxed">
                Vietnamese engineering teams contribute directly to Marvell's industry-leading <strong>Co-Packaged Optics (CPO)</strong>, PAM4 Optical DSPs, PCIe Gen 6/7 Retimers, and custom accelerated compute silicon for hyperscale AI data centers.
              </p>
            </div>

            <div class="p-6 rounded-2xl bg-[#101726]/80 border border-slate-800 backdrop-blur-sm">
              <div class="w-10 h-10 rounded-xl bg-purple-600/20 border border-purple-500/40 flex items-center justify-center text-[#c8a3ef] mb-4">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"/></svg>
              </div>
              <h3 class="text-base font-bold text-white mb-2">400+ Engineers & Academic Alliances</h3>
              <p class="text-xs text-slate-400 leading-relaxed">
                Over 400 specialized IC design engineers expanding toward 500+, supported by comprehensive university lab sponsorships, EDA software grants, and graduate fellowships with VNU-HCM, HCMUT, and HUST.
              </p>
            </div>

          </div>

          <!-- Bottom Action Links -->
          <div class="mt-8 pt-6 border-t border-slate-800/80 flex flex-wrap items-center justify-between gap-4 text-xs">
            <span class="text-slate-400">
              Host Headquarters: <strong>Marvell Technology Vietnam Co., Ltd.</strong> • E-Town Central, Ho Chi Minh City & Da Nang
            </span>
            <div class="flex items-center gap-4">
              <a href="https://www.marvell.com/company/careers.html" target="_blank" class="text-[#00b5e2] hover:underline font-semibold flex items-center gap-1">
                <span>Explore IC Design Careers at Marvell Vietnam</span>
                <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"/></svg>
              </a>
              <a href="https://www.marvell.com" target="_blank" class="text-slate-300 hover:text-white font-semibold flex items-center gap-1">
                <span>Corporate Website (marvell.com)</span>
                <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
              </a>
            </div>
          </div>

        </div>
      </div>

    </div>
  </section>

  <!-- =========================================================================
       5. FEATURED DIGNITARIES & SPEAKERS (CONTRAST DARK TECH CANVAS)
       ========================================================================= -->
  <section id="speakers" class="py-20 lg:py-28 bg-[#05070a] border-b border-slate-800">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center max-w-3xl mx-auto mb-16">
        <span class="text-xs font-bold tracking-widest text-[#00b5e2] uppercase">DISTINGUISHED SPEAKERS & GUESTS OF HONOR</span>
        <h2 class="text-3xl sm:text-4xl font-extrabold text-white mt-2 mb-4">World-Class Tech Leaders & Architects</h2>
        <p class="text-slate-400 text-sm sm:text-base">Strategic keynotes and deep technical insights from industry architects shaping the global semiconductor frontier.</p>
      </div>

      <!-- TIER 1: KEYNOTES & ORGANIZER LEADERSHIP -->
      <div class="mb-14">
        <h3 class="text-xs font-bold uppercase tracking-widest text-slate-400 mb-6 flex items-center gap-3">
          <span>GOVERNMENT LEADERS & STRATEGIC KEYNOTES</span>
          <div class="flex-1 h-px bg-slate-800"></div>
        </h3>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          
          <!-- Noam Mizrahi -->
          <div class="mrvll-dark-card speaker-card cursor-pointer group p-7 rounded-xl flex flex-col justify-between border-t-2 border-t-[#0072ce] bg-[#101726]" data-speaker-id="noam-mizrahi">
            <div>
              <div class="w-16 h-16 rounded-xl bg-blue-900/40 border border-blue-500/50 flex items-center justify-center text-xl font-bold text-[#00b5e2] mb-4 shadow-[0_0_20px_rgba(0,114,206,0.3)] group-hover:scale-105 transition-transform">
                NM
              </div>
              <span class="text-[10px] font-bold tracking-wider uppercase text-blue-400 bg-blue-950/60 px-2.5 py-0.5 rounded border border-blue-500/20">KEYNOTE 1</span>
              <h4 class="text-lg font-bold text-white mt-2 group-hover:text-[#00b5e2] transition-colors">Noam Mizrahi</h4>
              <p class="text-xs font-semibold text-[#00b5e2] mt-0.5">EVP & Chief Technology Officer (CTO)</p>
              <p class="text-xs text-slate-400 mt-2 font-medium">Marvell Technology, Inc.</p>
            </div>
            <div class="mt-4 pt-3 border-t border-slate-800 text-[11px] text-slate-400">
              Topic: <em>IC Design - Advanced Silicon Architecture Trends</em>
              <div class="mt-2 text-[11px] text-[#00b5e2] flex items-center gap-1 font-semibold group-hover:underline">
                <span>View Bio & Sessions</span>
                <svg class="w-3.5 h-3.5 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
              </div>
            </div>
          </div>

          <!-- Sandeep Bharathi -->
          <div class="mrvll-dark-card speaker-card cursor-pointer group p-7 rounded-xl flex flex-col justify-between border-t-2 border-t-[#c8a3ef] bg-[#101726]" data-speaker-id="sandeep-bharathi">
            <div>
              <div class="w-16 h-16 rounded-xl bg-purple-900/40 border border-purple-500/50 flex items-center justify-center text-xl font-bold text-[#c8a3ef] mb-4 shadow-[0_0_20px_rgba(200,163,239,0.3)] group-hover:scale-105 transition-transform">
                SB
              </div>
              <span class="text-[10px] font-bold tracking-wider uppercase text-purple-400 bg-purple-950/60 px-2.5 py-0.5 rounded border border-purple-500/20">PANEL HOST</span>
              <h4 class="text-lg font-bold text-white mt-2 group-hover:text-[#c8a3ef] transition-colors">Sandeep Bharathi</h4>
              <p class="text-xs font-semibold text-[#c8a3ef] mt-0.5">President, Data Center Group (DCG)</p>
              <p class="text-xs text-slate-400 mt-2 font-medium">Marvell Technology, Inc.</p>
            </div>
            <div class="mt-4 pt-3 border-t border-slate-800 text-[11px] text-slate-400">
              Moderator: <em>National Strategic Semiconductor Panel</em>
              <div class="mt-2 text-[11px] text-[#c8a3ef] flex items-center gap-1 font-semibold group-hover:underline">
                <span>View Bio & Sessions</span>
                <svg class="w-3.5 h-3.5 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
              </div>
            </div>
          </div>

          <!-- Nguyen Van Duoc -->
          <div class="mrvll-dark-card speaker-card cursor-pointer group p-7 rounded-xl flex flex-col justify-between border-t-2 border-t-emerald-500 bg-[#101726]" data-speaker-id="nguyen-van-duoc">
            <div>
              <div class="w-16 h-16 rounded-xl bg-emerald-900/40 border border-emerald-500/50 flex items-center justify-center text-xl font-bold text-emerald-400 mb-4 shadow-[0_0_20px_rgba(16,185,129,0.3)] group-hover:scale-105 transition-transform">
                NVD
              </div>
              <span class="text-[10px] font-bold tracking-wider uppercase text-emerald-400 bg-emerald-950/60 px-2.5 py-0.5 rounded border border-emerald-500/20">GUEST OF HONOR</span>
              <h4 class="text-lg font-bold text-white mt-2 group-hover:text-emerald-400 transition-colors">Mr. Nguyen Van Duoc</h4>
              <p class="text-xs font-semibold text-emerald-400 mt-0.5">Chairman</p>
              <p class="text-xs text-slate-400 mt-2 font-medium">Ho Chi Minh City People's Committee</p>
            </div>
            <div class="mt-4 pt-3 border-t border-slate-800 text-[11px] text-slate-400">
              Address: <em>Strategy for HCMC High-Tech & Silicon Ecosystem</em>
              <div class="mt-2 text-[11px] text-emerald-400 flex items-center gap-1 font-semibold group-hover:underline">
                <span>View Bio & Sessions</span>
                <svg class="w-3.5 h-3.5 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
              </div>
            </div>
          </div>

          <!-- Melissa A. Brown -->
          <div class="mrvll-dark-card speaker-card cursor-pointer group p-7 rounded-xl flex flex-col justify-between border-t-2 border-t-amber-500 bg-[#101726]" data-speaker-id="melissa-brown">
            <div>
              <div class="w-16 h-16 rounded-xl bg-amber-900/40 border border-amber-500/50 flex items-center justify-center text-xl font-bold text-amber-400 mb-4 shadow-[0_0_20px_rgba(245,158,11,0.3)] group-hover:scale-105 transition-transform">
                MB
              </div>
              <span class="text-[10px] font-bold tracking-wider uppercase text-amber-400 bg-amber-950/60 px-2.5 py-0.5 rounded border border-amber-500/20">DIPLOMATIC MISSION</span>
              <h4 class="text-lg font-bold text-white mt-2 group-hover:text-amber-400 transition-colors">Ms. Melissa A. Brown</h4>
              <p class="text-xs font-semibold text-amber-400 mt-0.5">U.S. Consul General</p>
              <p class="text-xs text-slate-400 mt-2 font-medium">U.S. Consulate General in Ho Chi Minh City</p>
            </div>
            <div class="mt-4 pt-3 border-t border-slate-800 text-[11px] text-slate-400">
              Address: <em>U.S. - Vietnam Comprehensive Strategic Partnership</em>
              <div class="mt-2 text-[11px] text-amber-400 flex items-center gap-1 font-semibold group-hover:underline">
                <span>View Bio & Sessions</span>
                <svg class="w-3.5 h-3.5 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
              </div>
            </div>
          </div>

        </div>
      </div>

      <!-- TIER 2: INDUSTRY & ACADEMIA LEADERS -->
      <div>
        <h3 class="text-xs font-bold uppercase tracking-widest text-slate-400 mb-6 flex items-center gap-3">
          <span>CORPORATE ARCHITECTS & ACADEMIC LUMINARIES</span>
          <div class="flex-1 h-px bg-slate-800"></div>
        </h3>

        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
          
          <div class="speaker-card cursor-pointer group p-5 rounded-xl bg-[#101726] border border-slate-800 hover:border-[#00b5e2] transition-all" data-speaker-id="nguyen-bich-yen">
            <div class="flex items-center justify-between">
              <h4 class="text-sm font-bold text-white group-hover:text-[#00b5e2] transition-colors">Ms. Nguyen Bich-Yen</h4>
              <svg class="w-3.5 h-3.5 text-slate-500 group-hover:text-[#00b5e2] group-hover:translate-x-0.5 transition-all" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
            </div>
            <span class="text-xs text-[#00b5e2] block font-medium">VSAP-LAB</span>
            <p class="text-[11px] text-slate-400 mt-1">Keynote 2: Advanced Packaging & CPO</p>
          </div>

          <div class="speaker-card cursor-pointer group p-5 rounded-xl bg-[#101726] border border-slate-800 hover:border-[#00b5e2] transition-all" data-speaker-id="hien-dao">
            <div class="flex items-center justify-between">
              <h4 class="text-sm font-bold text-white group-hover:text-[#00b5e2] transition-colors">Ms. Hien Dao</h4>
              <svg class="w-3.5 h-3.5 text-slate-500 group-hover:text-[#00b5e2] group-hover:translate-x-0.5 transition-all" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
            </div>
            <span class="text-xs text-[#00b5e2] block font-medium">Intel Corporation</span>
            <p class="text-[11px] text-slate-400 mt-1">Silicon Fabrication & ATP Protocols</p>
          </div>

          <div class="speaker-card cursor-pointer group p-5 rounded-xl bg-[#101726] border border-slate-800 hover:border-[#00b5e2] transition-all" data-speaker-id="vo-phong">
            <div class="flex items-center justify-between">
              <h4 class="text-sm font-bold text-white group-hover:text-[#00b5e2] transition-colors">Mr. Vo Phong</h4>
              <svg class="w-3.5 h-3.5 text-slate-500 group-hover:text-[#00b5e2] group-hover:translate-x-0.5 transition-all" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
            </div>
            <span class="text-xs text-[#00b5e2] block font-medium">Ampere Computing</span>
            <p class="text-[11px] text-slate-400 mt-1">ARM Server Microarchitecture Design</p>
          </div>

          <div class="speaker-card cursor-pointer group p-5 rounded-xl bg-[#101726] border border-slate-800 hover:border-[#00b5e2] transition-all" data-speaker-id="tran-dang-khoa">
            <div class="flex items-center justify-between">
              <h4 class="text-sm font-bold text-white group-hover:text-[#00b5e2] transition-colors">Mr. Tran Dang Khoa</h4>
              <svg class="w-3.5 h-3.5 text-slate-500 group-hover:text-[#00b5e2] group-hover:translate-x-0.5 transition-all" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
            </div>
            <span class="text-xs text-[#00b5e2] block font-medium">Renesas Electronics</span>
            <p class="text-[11px] text-slate-400 mt-1">Automotive MCU & Embedded Systems</p>
          </div>

          <div class="speaker-card cursor-pointer group p-5 rounded-xl bg-[#101726] border border-slate-800 hover:border-[#00b5e2] transition-all" data-speaker-id="vo-thieu-nam">
            <div class="flex items-center justify-between">
              <h4 class="text-sm font-bold text-white group-hover:text-[#00b5e2] transition-colors">Mr. Vo Thieu Nam</h4>
              <svg class="w-3.5 h-3.5 text-slate-500 group-hover:text-[#00b5e2] group-hover:translate-x-0.5 transition-all" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
            </div>
            <span class="text-xs text-[#00b5e2] block font-medium">Qualcomm</span>
            <p class="text-[11px] text-slate-400 mt-1">5G/6G RF & Connectivity Silicon</p>
          </div>

          <div class="speaker-card cursor-pointer group p-5 rounded-xl bg-[#101726] border border-slate-800 hover:border-emerald-500 transition-all" data-speaker-id="mai-thi-thanh-nguyen">
            <div class="flex items-center justify-between">
              <h4 class="text-sm font-bold text-white group-hover:text-emerald-400 transition-colors">Assoc. Prof. Mai Thi Thanh Nguyen</h4>
              <svg class="w-3.5 h-3.5 text-slate-500 group-hover:text-emerald-400 group-hover:translate-x-0.5 transition-all" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
            </div>
            <span class="text-xs text-emerald-400 block font-medium">VNU-HCMC</span>
            <p class="text-[11px] text-slate-400 mt-1">Council Chair & Strategic Panelist</p>
          </div>

          <div class="speaker-card cursor-pointer group p-5 rounded-xl bg-[#101726] border border-slate-800 hover:border-emerald-500 transition-all" data-speaker-id="nguyen-hoang-trang">
            <div class="flex items-center justify-between">
              <h4 class="text-sm font-bold text-white group-hover:text-emerald-400 transition-colors">Prof. Nguyen Hoang Trang</h4>
              <svg class="w-3.5 h-3.5 text-slate-500 group-hover:text-emerald-400 group-hover:translate-x-0.5 transition-all" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
            </div>
            <span class="text-xs text-emerald-400 block font-medium">HCMUT (Bach Khoa HCMC)</span>
            <p class="text-[11px] text-slate-400 mt-1">Digital IC Design & ASIC Verification</p>
          </div>

          <div class="speaker-card cursor-pointer group p-5 rounded-xl bg-[#101726] border border-slate-800 hover:border-emerald-500 transition-all" data-speaker-id="nguyen-pham-loan">
            <div class="flex items-center justify-between">
              <h4 class="text-sm font-bold text-white group-hover:text-emerald-400 transition-colors">Prof. Nguyen Pham Loan</h4>
              <svg class="w-3.5 h-3.5 text-slate-500 group-hover:text-emerald-400 group-hover:translate-x-0.5 transition-all" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
            </div>
            <span class="text-xs text-emerald-400 block font-medium">HUST (Bach Khoa Hanoi)</span>
            <p class="text-[11px] text-slate-400 mt-1">Analog & RF Mixed-Signal IC</p>
          </div>

        </div>
      </div>

    </div>
  </section>

  <!-- =========================================================================
       6. SPECIAL FEATURE: STRATEGIC HIGH-LEVEL PANEL DISCUSSION
       ========================================================================= -->
  <section id="panel" class="py-20 bg-gradient-to-b from-[#05070a] to-[#0c1017] text-white border-b border-slate-800 relative">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="bg-gradient-to-r from-blue-950/40 via-purple-950/30 to-slate-900/50 p-8 sm:p-12 rounded-2xl border border-blue-500/30 shadow-2xl backdrop-blur-xl">
        <div class="max-w-3xl">
          <span class="inline-block px-3 py-1 rounded-full bg-blue-500/20 text-[#00b5e2] text-xs font-bold uppercase tracking-widest mb-4 border border-blue-500/30">
            HIGH-LEVEL STRATEGIC PLENARY
          </span>
          <h2 class="text-2xl sm:text-4xl font-extrabold text-white leading-tight">
            Building Vietnam's National Semiconductor Value Chain 2026–2035
          </h2>
          <p class="text-slate-300 text-sm sm:text-base mt-4 leading-relaxed">
            A milestone roundtable uniting Government policymakers, multinational semiconductor titans, and top university presidents to establish actionable frameworks for IC design incentives, packaging infrastructure, and workforce readiness.
          </p>

          <div class="mt-8 grid grid-cols-1 sm:grid-cols-3 gap-4 pt-6 border-t border-slate-800/80 text-xs">
            <div>
              <span class="text-slate-400 block uppercase font-bold">Time & Venue</span>
              <span class="font-mono text-cyan-300 font-bold text-sm">14:00 - 15:30 • VIP Hall</span>
            </div>
            <div>
              <span class="text-slate-400 block uppercase font-bold">Session Chair</span>
              <span class="text-white font-semibold">Sandeep Bharathi (Marvell DCG)</span>
            </div>
            <div>
              <span class="text-slate-400 block uppercase font-bold">Key Focus</span>
              <span class="text-emerald-400 font-semibold">Tax, IP Protection & 50K Engineers</span>
            </div>
          </div>
        </div>
      </div>

    </div>
  </section>

  <!-- =========================================================================
       7. INTERACTIVE AGENDA SECTION (CRISP LIGHT THEME - MAXIMUM READABILITY)
       ========================================================================= -->
  <section id="agenda" class="py-20 lg:py-28 bg-[#ffffff] border-b border-slate-200">
    <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center mb-12">
        <span class="text-xs font-bold tracking-widest text-[#0072ce] uppercase">OFFICIAL SUMMIT TIMETABLE</span>
        <h2 class="text-3xl sm:text-4xl font-extrabold text-slate-900 mt-2">Comprehensive 24-Session Agenda</h2>
        <p class="text-slate-600 text-sm mt-2 max-w-xl mx-auto">Monday, November 23, 2026. Filter sessions by time block or domain track.</p>
      </div>

      <!-- Session Track Tabs -->
      <div class="flex flex-wrap items-center justify-center gap-2 mb-8 bg-slate-100 p-1.5 rounded-xl max-w-xl mx-auto">
        <button class="agenda-tab-btn active px-4 py-2 text-xs font-bold rounded-lg bg-slate-900 text-white shadow-sm transition-all" data-session="all">All Sessions (24)</button>
        <button class="agenda-tab-btn px-4 py-2 text-xs font-bold rounded-lg text-slate-600 hover:text-slate-900 transition-all" data-session="morning">Morning Strategic Track</button>
        <button class="agenda-tab-btn px-4 py-2 text-xs font-bold rounded-lg text-slate-600 hover:text-slate-900 transition-all" data-session="afternoon">Afternoon Technical Tracks</button>
      </div>

      <!-- Category Filter Pills -->
      <div class="flex flex-wrap items-center justify-center gap-2 mb-10 text-xs">
        <button class="agenda-filter-pill active px-3.5 py-1.5 rounded-full border border-[#0072ce] bg-blue-50 text-[#0072ce] font-semibold transition-colors" data-category="all">All Tracks</button>
        <button class="agenda-filter-pill px-3.5 py-1.5 rounded-full border border-slate-300 text-slate-600 hover:border-slate-400 transition-colors" data-category="keynote">Keynotes</button>
        <button class="agenda-filter-pill px-3.5 py-1.5 rounded-full border border-slate-300 text-slate-600 hover:border-slate-400 transition-colors" data-category="industry">Industry</button>
        <button class="agenda-filter-pill px-3.5 py-1.5 rounded-full border border-slate-300 text-slate-600 hover:border-slate-400 transition-colors" data-category="academia">Academia</button>
        <button class="agenda-filter-pill px-3.5 py-1.5 rounded-full border border-slate-300 text-slate-600 hover:border-slate-400 transition-colors" data-category="panel">Strategic Panel</button>
        <button class="agenda-filter-pill px-3.5 py-1.5 rounded-full border border-slate-300 text-slate-600 hover:border-slate-400 transition-colors" data-category="networking">Networking</button>
      </div>

      <!-- Rendered Agenda Item Cards -->
      <div class="space-y-4">
        {agenda_items_rendered}
      </div>

    </div>
  </section>

  <!-- =========================================================================
       8. PARTNERS & ECOSYSTEM LOGO MARQUEE
       ========================================================================= -->
  <section id="partners" class="py-20 bg-slate-50 border-b border-slate-200">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
      
      <span class="text-xs font-bold tracking-widest text-[#0072ce] uppercase">SUMMIT HOST & STRATEGIC ECOSYSTEM ALLIANCE</span>
      <h2 class="text-3xl font-extrabold text-slate-900 mt-2 mb-10">Uniting Global Chipmakers & Premier Academia</h2>

      <!-- Lead Host & Organizer Spotlight Box -->
      <div class="max-w-3xl mx-auto mb-12 p-6 sm:p-8 rounded-2xl bg-white border-2 border-[#0072ce]/20 shadow-md flex flex-col sm:flex-row items-center justify-between gap-6 text-left">
        <div class="flex flex-col sm:flex-row items-center gap-5 text-center sm:text-left">
          <div class="p-3.5 bg-blue-50/80 rounded-xl border border-blue-200 shrink-0">
            {marvell_logo_partner}
          </div>
          <div>
            <span class="inline-block text-[10px] font-extrabold uppercase px-2.5 py-0.5 rounded bg-blue-950 text-[#00b5e2] tracking-wider mb-1">
              HOST & CONVENING ORGANIZER
            </span>
            <h3 class="text-lg font-bold text-slate-900">Marvell Technology, Inc. (NASDAQ: MRVL)</h3>
            <p class="text-xs text-slate-500 mt-0.5">Dual R&D Centers of Excellence: Ho Chi Minh City & Da Nang</p>
          </div>
        </div>
        <a href="https://www.marvell.com" target="_blank" class="mrvll-btn-primary text-xs shrink-0 py-3">
          <span>ABOUT MARVELL</span>
          <svg class="btn-arrow w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
        </a>
      </div>

      <!-- Strategic Industry & Academic Partners Grid -->
      <div class="text-xs font-bold uppercase tracking-widest text-slate-500 mb-6">GLOBAL SEMICONDUCTOR PARTNERS & PREMIER UNIVERSITIES</div>
      <div class="max-w-5xl mx-auto grid grid-cols-2 sm:grid-cols-4 lg:grid-cols-7 gap-3.5 items-center justify-center">
        <div class="p-4 bg-white rounded-xl border border-slate-200 text-center font-extrabold text-slate-800 text-sm shadow-sm hover:border-[#0072ce] hover:text-[#0072ce] transition-colors">INTEL</div>
        <div class="p-4 bg-white rounded-xl border border-slate-200 text-center font-extrabold text-slate-800 text-sm shadow-sm hover:border-[#0072ce] hover:text-[#0072ce] transition-colors">QUALCOMM</div>
        <div class="p-4 bg-white rounded-xl border border-slate-200 text-center font-extrabold text-slate-800 text-sm shadow-sm hover:border-[#0072ce] hover:text-[#0072ce] transition-colors">RENESAS</div>
        <div class="p-4 bg-white rounded-xl border border-slate-200 text-center font-extrabold text-slate-800 text-sm shadow-sm hover:border-[#0072ce] hover:text-[#0072ce] transition-colors">AMPERE</div>
        <div class="p-4 bg-white rounded-xl border border-slate-200 text-center font-extrabold text-slate-800 text-sm shadow-sm hover:border-[#0072ce] hover:text-[#0072ce] transition-colors">VSAP-LAB</div>
        <div class="p-4 bg-white rounded-xl border border-slate-200 text-center font-extrabold text-slate-800 text-sm shadow-sm hover:border-[#0072ce] hover:text-[#0072ce] transition-colors">VNU-HCM</div>
        <div class="p-4 bg-white rounded-xl border border-slate-200 text-center font-extrabold text-slate-800 text-sm shadow-sm hover:border-[#0072ce] hover:text-[#0072ce] transition-colors">HUST</div>
      </div>

    </div>
  </section>

  <!-- =========================================================================
       9. REGISTRATION FORM (FREE RSVP - CLEAN B2B LIGHT THEME)
       ========================================================================= -->
  <section id="register" class="py-20 lg:py-28 bg-[#f8fafc] border-b border-slate-200 relative">
    <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center mb-12">
        <span class="text-xs font-bold tracking-widest text-[#0072ce] uppercase">100% FREE ATTENDEE REGISTRATION</span>
        <h2 class="text-3xl sm:text-4xl font-extrabold text-slate-900 mt-2">Reserve Your Seat at Vietnam Semiconductor Summit 2026</h2>
        <p class="text-slate-600 text-sm mt-2 max-w-xl mx-auto">Auditorium seating is strictly limited. Complete the form below to receive your official invitation letter and digital check-in E-Pass.</p>
      </div>

      <div class="bg-white p-8 sm:p-10 rounded-2xl border border-slate-200/90 shadow-xl">
        <form id="summit-register-form" class="space-y-6">
          
          <!-- Pass Tier Selector -->
          <div>
            <label class="block text-xs font-bold uppercase tracking-wider text-slate-700 mb-2.5">Select Your Delegate Category / Pass Tier *</label>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
              <label class="flex items-start gap-2.5 p-3.5 rounded-xl border border-slate-300 bg-slate-50 cursor-pointer hover:border-[#0072ce] transition-colors has-[:checked]:border-[#0072ce] has-[:checked]:bg-blue-50/50 has-[:checked]:ring-1 has-[:checked]:ring-[#0072ce]">
                <input type="radio" name="reg_tier" value="VIP Delegate (C-Level & Diplomatic)" class="mt-0.5 text-[#0072ce] focus:ring-0">
                <div>
                  <span class="font-bold text-slate-900 block">VIP Delegate</span>
                  <span class="text-[11px] text-slate-500">C-Level, Government Leaders, VIP Lounge & Gala Banquet</span>
                </div>
              </label>
              <label class="flex items-start gap-2.5 p-3.5 rounded-xl border border-slate-300 bg-slate-50 cursor-pointer hover:border-[#0072ce] transition-colors has-[:checked]:border-[#0072ce] has-[:checked]:bg-blue-50/50 has-[:checked]:ring-1 has-[:checked]:ring-[#0072ce]">
                <input type="radio" name="reg_tier" value="Industry & IC Designer" checked class="mt-0.5 text-[#0072ce] focus:ring-0">
                <div>
                  <span class="font-bold text-slate-900 block">Industry & IC Designer</span>
                  <span class="text-[11px] text-slate-500">Practicing Silicon Engineers, Access to all 24 Technical Sessions</span>
                </div>
              </label>
              <label class="flex items-start gap-2.5 p-3.5 rounded-xl border border-slate-300 bg-slate-50 cursor-pointer hover:border-[#0072ce] transition-colors has-[:checked]:border-[#0072ce] has-[:checked]:bg-blue-50/50 has-[:checked]:ring-1 has-[:checked]:ring-[#0072ce]">
                <input type="radio" name="reg_tier" value="Academia & Faculty (Universities & Labs)" class="mt-0.5 text-[#0072ce] focus:ring-0">
                <div>
                  <span class="font-bold text-slate-900 block">Academia & Faculty</span>
                  <span class="text-[11px] text-slate-500">Professors, Researchers, Academic R&D Collaboration Tracks</span>
                </div>
              </label>
              <label class="flex items-start gap-2.5 p-3.5 rounded-xl border border-slate-300 bg-slate-50 cursor-pointer hover:border-[#0072ce] transition-colors has-[:checked]:border-[#0072ce] has-[:checked]:bg-blue-50/50 has-[:checked]:ring-1 has-[:checked]:ring-[#0072ce]">
                <input type="radio" name="reg_tier" value="Talent & Elite Student" class="mt-0.5 text-[#0072ce] focus:ring-0">
                <div>
                  <span class="font-bold text-slate-900 block">Talent & Student</span>
                  <span class="text-[11px] text-slate-500">Sponsored Passes, Marvell R&D Career Opportunities</span>
                </div>
              </label>
            </div>
          </div>

          <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
            <div>
              <label for="reg-fullname" class="block text-xs font-bold uppercase tracking-wider text-slate-700 mb-2">Full Name *</label>
              <input type="text" id="reg-fullname" required placeholder="e.g. Dr. Alex Johnson" class="w-full px-4 py-3 bg-white border border-slate-300 rounded-lg text-slate-900 placeholder:text-slate-400 text-sm focus:outline-none focus:border-[#0072ce] focus:ring-1 focus:ring-[#0072ce] transition-colors">
            </div>

            <div>
              <label for="reg-email" class="block text-xs font-bold uppercase tracking-wider text-slate-700 mb-2">Work / Academic Email *</label>
              <input type="email" id="reg-email" required placeholder="alex@company.com" class="w-full px-4 py-3 bg-white border border-slate-300 rounded-lg text-slate-900 placeholder:text-slate-400 text-sm focus:outline-none focus:border-[#0072ce] focus:ring-1 focus:ring-[#0072ce] transition-colors">
            </div>
          </div>

          <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
            <div>
              <label for="reg-phone" class="block text-xs font-bold uppercase tracking-wider text-slate-700 mb-2">Phone Number *</label>
              <input type="tel" id="reg-phone" required placeholder="+84 901 234 567" class="w-full px-4 py-3 bg-white border border-slate-300 rounded-lg text-slate-900 placeholder:text-slate-400 text-sm focus:outline-none focus:border-[#0072ce] focus:ring-1 focus:ring-[#0072ce] transition-colors">
            </div>

            <div>
              <label for="reg-company" class="block text-xs font-bold uppercase tracking-wider text-slate-700 mb-2">Organization / Enterprise / University *</label>
              <input type="text" id="reg-company" required placeholder="e.g. Synopsys / VNU-HCM" class="w-full px-4 py-3 bg-white border border-slate-300 rounded-lg text-slate-900 placeholder:text-slate-400 text-sm focus:outline-none focus:border-[#0072ce] focus:ring-1 focus:ring-[#0072ce] transition-colors">
            </div>
          </div>

          <div>
            <label for="reg-role" class="block text-xs font-bold uppercase tracking-wider text-slate-700 mb-2">Professional Position / Specialization *</label>
            <select id="reg-role" class="w-full px-4 py-3 bg-white border border-slate-300 rounded-lg text-slate-900 text-sm focus:outline-none focus:border-[#0072ce] focus:ring-1 focus:ring-[#0072ce] transition-colors">
              <option value="IC Design Engineer (Analog / Digital)">IC Design Engineer (Analog / Digital)</option>
              <option value="Hardware / Firmware Engineer">Hardware / Firmware Engineer</option>
              <option value="C-Level / Corporate Executive">C-Level / Corporate Executive</option>
              <option value="Professor / University Faculty / Researcher">Professor / University Faculty / Researcher</option>
              <option value="Microelectronics / EE Student">Microelectronics / EE Student</option>
              <option value="Government Official / Diplomat">Government Official / Diplomat</option>
              <option value="Other">Other</option>
            </select>
          </div>

          <div>
            <label class="block text-xs font-bold uppercase tracking-wider text-slate-700 mb-3">Primary Areas of Interest at the Summit *</label>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs text-slate-700">
              <label class="flex items-center gap-2.5 p-3.5 rounded-lg bg-slate-50 border border-slate-200 cursor-pointer hover:border-slate-400 transition-colors">
                <input type="checkbox" name="interests" value="IC Design (Analog/Digital)" checked class="rounded text-[#0072ce] focus:ring-0">
                <span>Integrated Circuit Design (Analog & Digital)</span>
              </label>
              <label class="flex items-center gap-2.5 p-3.5 rounded-lg bg-slate-50 border border-slate-200 cursor-pointer hover:border-slate-400 transition-colors">
                <input type="checkbox" name="interests" value="Advanced Packaging & CPO" class="rounded text-[#0072ce] focus:ring-0">
                <span>Advanced Packaging & Co-Packaged Optics (CPO)</span>
              </label>
              <label class="flex items-center gap-2.5 p-3.5 rounded-lg bg-slate-50 border border-slate-200 cursor-pointer hover:border-slate-400 transition-colors">
                <input type="checkbox" name="interests" value="AI Cloud Infrastructure" class="rounded text-[#0072ce] focus:ring-0">
                <span>AI Infrastructure & Data Center Silicon</span>
              </label>
              <label class="flex items-center gap-2.5 p-3.5 rounded-lg bg-slate-50 border border-slate-200 cursor-pointer hover:border-slate-400 transition-colors">
                <input type="checkbox" name="interests" value="Marvell Vietnam R&D Collaboration" class="rounded text-[#0072ce] focus:ring-0">
                <span>R&D Collaboration with Marvell Vietnam</span>
              </label>
            </div>
          </div>

          <div class="pt-4">
            <button type="submit" class="mrvll-btn-primary w-full justify-center text-sm py-4">
              <span>CONFIRM REGISTRATION (FREE RSVP)</span>
              <svg class="btn-arrow w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
            </button>
            <p class="text-[11px] text-slate-500 text-center mt-3">
              By registering, you agree to <a href="https://www.marvell.com/privacy-statement.html" target="_blank" class="text-[#0072ce] hover:underline font-medium">Marvell's Privacy Statement</a>. Your information is protected under strict enterprise standards.
            </p>
          </div>

        </form>
      </div>

    </div>
  </section>

  <!-- =========================================================================
       10. VENUE & INTERACTIVE FAQ ACCORDION
       ========================================================================= -->
  <section id="faq" class="py-20 bg-white border-b border-slate-200">
    <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center mb-14">
        <span class="text-xs font-bold tracking-widest text-[#0072ce] uppercase">ATTENDEE SUPPORT & FAQ</span>
        <h2 class="text-3xl sm:text-4xl font-extrabold text-slate-900 mt-2">Frequently Asked Questions</h2>
      </div>

      <div class="space-y-4">
        
        <!-- Accordion Item 1 (Default Active) -->
        <div class="faq-accordion-item active">
          <button class="faq-accordion-header">
            <span class="text-base font-bold text-slate-900">Is attendance free of charge?</span>
            <svg class="faq-accordion-chevron w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M19 9l-7 7-7-7"/></svg>
          </button>
          <div class="faq-accordion-body">
            <p class="text-sm text-slate-600 leading-relaxed">
              Yes, <strong>The 1st Vietnam Semiconductor Summit 2026</strong> is 100% free for all verified registrants who receive an official invitation letter. Because auditorium seating is limited, registrations are vetted on a first-come, first-approved basis.
            </p>
          </div>
        </div>

        <!-- Accordion Item 2 -->
        <div class="faq-accordion-item">
          <button class="faq-accordion-header">
            <span class="text-base font-bold text-slate-900">When will I receive my invitation and QR Check-in badge?</span>
            <svg class="faq-accordion-chevron w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M19 9l-7 7-7-7"/></svg>
          </button>
          <div class="faq-accordion-body">
            <p class="text-sm text-slate-600 leading-relaxed">
              Upon submitting the online form, an instant digital acknowledgment E-Pass will be issued. The official executive invitation letter and high-resolution personalized Check-in QR badge will be delivered to your registered email within 48 business hours.
            </p>
          </div>
        </div>

        <!-- Accordion Item 3 -->
        <div class="faq-accordion-item">
          <button class="faq-accordion-header">
            <span class="text-base font-bold text-slate-900">What is the event dress code?</span>
            <svg class="faq-accordion-chevron w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M19 9l-7 7-7-7"/></svg>
          </button>
          <div class="faq-accordion-body">
            <p class="text-sm text-slate-600 leading-relaxed">
              The dress code is Business Professional or Business Casual. For university students, smart campus formal attire is encouraged.
            </p>
          </div>
        </div>

        <!-- Accordion Item 4 -->
        <div class="faq-accordion-item">
          <button class="faq-accordion-header">
            <span class="text-base font-bold text-slate-900">Will presentation slides and technical materials be available?</span>
            <svg class="faq-accordion-chevron w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M19 9l-7 7-7-7"/></svg>
          </button>
          <div class="faq-accordion-body">
            <p class="text-sm text-slate-600 leading-relaxed">
              Authorized keynote decks and session whitepapers will be distributed via email to all attending delegates following the summit proceedings.
            </p>
          </div>
        </div>

      </div>

    </div>
  </section>

  <!-- =========================================================================
       11. CORPORATE FOOTER (CRISP WHITE - OFFICIAL MARVELL FOOTER SPEC)
       ========================================================================= -->
  <footer class="bg-white py-14 border-t border-slate-200 text-xs text-slate-500">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="flex flex-col md:flex-row items-center justify-between gap-6 pb-8 border-b border-slate-200">
        <div class="flex items-center gap-4">
          {marvell_logo_footer}
          <div class="h-5 w-px bg-slate-300"></div>
          <div>
            <span class="text-slate-900 font-bold block text-xs">The 1st Vietnam Semiconductor Summit 2026</span>
            <span class="text-[10px] text-[#0072ce] font-mono font-semibold">Organized by Marvell Technology, Inc. (NASDAQ: MRVL)</span>
          </div>
        </div>

        <div class="flex flex-wrap items-center gap-6 font-semibold text-slate-600">
          <a href="https://www.marvell.com/company.html" target="_blank" class="hover:text-[#0072ce] transition-colors">About Marvell</a>
          <a href="https://www.marvell.com/products.html" target="_blank" class="hover:text-[#0072ce] transition-colors">Products & Silicon</a>
          <a href="https://www.marvell.com/company/careers.html" target="_blank" class="hover:text-[#0072ce] transition-colors">Careers at Marvell Vietnam</a>
          <a href="https://www.marvell.com/company/media-kit.html" target="_blank" class="hover:text-[#0072ce] transition-colors">Media Kit & Press</a>
          <a href="https://www.marvell.com/privacy-statement.html" target="_blank" class="hover:text-[#0072ce] transition-colors">Privacy Statement</a>
        </div>
      </div>

      <!-- Marvell Vietnam Footprint & Contact Grid -->
      <div class="py-8 grid grid-cols-1 md:grid-cols-3 gap-6 border-b border-slate-200/80 text-[11px] text-slate-600">
        <div>
          <span class="font-bold text-slate-900 uppercase block mb-1">Summit Host Secretariat</span>
          <p>Marvell Technology Organizing Committee</p>
          <p class="mt-1">Official Summit Email: <a href="mailto:vietnam-summit@marvell.com" class="text-[#0072ce] font-semibold underline">vietnam-summit@marvell.com</a></p>
        </div>
        <div>
          <span class="font-bold text-slate-900 uppercase block mb-1">Marvell Vietnam R&D (Ho Chi Minh City)</span>
          <p>Tan Thuan Export Processing Zone (EPZ) & E-Town Central</p>
          <p class="text-slate-500">Center of Excellence for Optical Interconnects & AI Silicon</p>
        </div>
        <div>
          <span class="font-bold text-slate-900 uppercase block mb-1">Marvell Vietnam R&D (Da Nang)</span>
          <p>Central Vietnam Semiconductor Design Center</p>
          <p class="text-slate-500">Custom Computing & High-Speed IC Engineering</p>
        </div>
      </div>

      <div class="pt-8 flex flex-col sm:flex-row items-center justify-between gap-4 text-center sm:text-left text-[11px]">
        <p>© 2026 Marvell Technology, Inc. All rights reserved. Essential technology, done right.</p>
        <p class="text-slate-500 font-mono">The 1st Vietnam Semiconductor Summit • Monday, November 23, 2026 • Ho Chi Minh City</p>
      </div>
    </div>
  </footer>

  <!-- =========================================================================
       POP-UP 1: SPEAKER BIO & SESSIONS MODAL (HIGH-TECH MARVELL CANVAS)
       ========================================================================= -->
  <div id="speaker-bio-modal" class="fixed inset-0 z-50 hidden modal-backdrop items-center justify-center p-4">
    <div class="modal-content-box bg-[#0c1017] max-w-2xl w-full rounded-2xl border border-cyan-500/40 p-6 sm:p-8 shadow-2xl relative text-left max-h-[90vh] flex flex-col">
      <!-- Close Button -->
      <button id="speaker-modal-close" class="absolute top-4 right-4 text-slate-400 hover:text-white p-2 rounded-lg hover:bg-white/10 transition-colors">
        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
      </button>

      <!-- Speaker Profile Header -->
      <div class="flex flex-col sm:flex-row items-start sm:items-center gap-5 pb-6 border-b border-slate-800 shrink-0">
        <div id="speaker-modal-avatar" class="w-16 h-16 sm:w-20 sm:h-20 rounded-xl bg-blue-950/80 border border-cyan-500/50 flex items-center justify-center text-2xl font-black text-[#00b5e2] shadow-[0_0_20px_rgba(0,181,226,0.3)] shrink-0">
          NM
        </div>
        <div class="pr-6">
          <div class="flex flex-wrap items-center gap-2 mb-1.5">
            <span id="speaker-modal-tag" class="text-[10px] font-extrabold tracking-wider uppercase px-2.5 py-0.5 rounded-md bg-blue-950/80 text-[#00b5e2] border border-blue-500/30">STRATEGIC KEYNOTE</span>
          </div>
          <h3 id="speaker-modal-name" class="text-2xl font-bold text-white">Noam Mizrahi</h3>
          <p id="speaker-modal-title" class="text-xs font-semibold text-[#00b5e2] mt-0.5">EVP & Chief Technology Officer (CTO)</p>
          <p id="speaker-modal-org" class="text-xs text-slate-400 font-medium">Marvell Technology, Inc.</p>
        </div>
      </div>

      <!-- Bio & Sessions Scrollable Body -->
      <div class="py-5 space-y-5 overflow-y-auto modal-scroll-y flex-1 pr-1">
        <div>
          <h4 class="text-xs font-bold uppercase tracking-widest text-slate-400 mb-2 flex items-center gap-2">
            <span class="w-1.5 h-1.5 rounded-full bg-[#00b5e2]"></span>
            <span>BIOGRAPHY & EXECUTIVE PROFILE</span>
          </h4>
          <p id="speaker-modal-bio" class="text-sm text-slate-300 leading-relaxed">...</p>
        </div>

        <div class="pt-2">
          <h4 class="text-xs font-bold uppercase tracking-widest text-slate-400 mb-2.5 flex items-center gap-2">
            <span class="w-1.5 h-1.5 rounded-full bg-[#c8a3ef]"></span>
            <span>SCHEDULED SESSIONS AT THE SUMMIT</span>
          </h4>
          <div id="speaker-modal-sessions" class="space-y-2.5">
            <!-- Dynamic session pills inserted by JS -->
          </div>
        </div>
      </div>

      <!-- Footer Actions -->
      <div class="pt-5 border-t border-slate-800 flex flex-col sm:flex-row items-center justify-between gap-4 shrink-0">
        <a href="#agenda" id="speaker-modal-agenda-link" class="text-xs font-bold text-[#00b5e2] hover:underline flex items-center gap-1.5">
          <span>View full timetable in Agenda</span>
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
        </a>
        <button id="speaker-modal-rsvp-btn" class="mrvll-btn-primary text-xs py-3 w-full sm:w-auto justify-center">
          <span>REGISTER TO ATTEND</span>
          <svg class="btn-arrow w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
        </button>
      </div>
    </div>
  </div>

  <!-- =========================================================================
       POP-UP 2: QUICK RSVP REGISTRATION MODAL
       ========================================================================= -->
  <div id="quick-rsvp-modal" class="fixed inset-0 z-50 hidden modal-backdrop items-center justify-center p-4">
    <div class="modal-content-box bg-white max-w-xl w-full rounded-2xl border border-slate-300 p-6 sm:p-8 shadow-2xl relative text-left max-h-[92vh] overflow-y-auto modal-scroll-y">
      <!-- Close Button -->
      <button id="quick-rsvp-close" class="absolute top-4 right-4 text-slate-400 hover:text-slate-800 p-2 rounded-lg hover:bg-slate-100 transition-colors">
        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
      </button>

      <div class="mb-5 pr-8">
        <div class="flex items-center gap-2 mb-1.5">
          <span class="w-2 h-2 rounded-full bg-[#0072ce] animate-pulse"></span>
          <span class="text-[11px] font-extrabold tracking-widest text-[#0072ce] uppercase font-mono">FREE RSVP • LIMITED CAPACITY</span>
        </div>
        <h3 class="text-2xl font-extrabold text-slate-900">Attend Vietnam Semiconductor Summit 2026</h3>
        <p class="text-xs text-slate-500 mt-1">Complete your details to secure your seat and receive your check-in E-Pass.</p>
      </div>

      <form id="quick-rsvp-form" class="space-y-4">
        <!-- 4 Pass Tiers Selector -->
        <div>
          <label class="block text-xs font-bold uppercase tracking-wider text-slate-700 mb-2">Select Delegate Tier *</label>
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-2.5 text-xs">
            <label class="flex items-start gap-2.5 p-3 rounded-xl border border-slate-300 bg-slate-50 cursor-pointer hover:border-[#0072ce] transition-colors has-[:checked]:border-[#0072ce] has-[:checked]:bg-blue-50/50 has-[:checked]:ring-1 has-[:checked]:ring-[#0072ce]">
              <input type="radio" name="modal_tier" value="VIP Delegate (C-Level & Diplomatic)" class="mt-0.5 text-[#0072ce] focus:ring-0">
              <div>
                <span class="font-bold text-slate-900 block">VIP Delegate</span>
                <span class="text-[11px] text-slate-500">C-Level, Government, Gala Dinner</span>
              </div>
            </label>
            <label class="flex items-start gap-2.5 p-3 rounded-xl border border-slate-300 bg-slate-50 cursor-pointer hover:border-[#0072ce] transition-colors has-[:checked]:border-[#0072ce] has-[:checked]:bg-blue-50/50 has-[:checked]:ring-1 has-[:checked]:ring-[#0072ce]">
              <input type="radio" name="modal_tier" value="Industry & IC Designer" checked class="mt-0.5 text-[#0072ce] focus:ring-0">
              <div>
                <span class="font-bold text-slate-900 block">Industry & IC Designer</span>
                <span class="text-[11px] text-slate-500">Silicon Engineers, 24 Tech Sessions</span>
              </div>
            </label>
            <label class="flex items-start gap-2.5 p-3 rounded-xl border border-slate-300 bg-slate-50 cursor-pointer hover:border-[#0072ce] transition-colors has-[:checked]:border-[#0072ce] has-[:checked]:bg-blue-50/50 has-[:checked]:ring-1 has-[:checked]:ring-[#0072ce]">
              <input type="radio" name="modal_tier" value="Academia & Faculty (Universities & Labs)" class="mt-0.5 text-[#0072ce] focus:ring-0">
              <div>
                <span class="font-bold text-slate-900 block">Academia & Faculty</span>
                <span class="text-[11px] text-slate-500">Professors, Academic Researchers</span>
              </div>
            </label>
            <label class="flex items-start gap-2.5 p-3 rounded-xl border border-slate-300 bg-slate-50 cursor-pointer hover:border-[#0072ce] transition-colors has-[:checked]:border-[#0072ce] has-[:checked]:bg-blue-50/50 has-[:checked]:ring-1 has-[:checked]:ring-[#0072ce]">
              <input type="radio" name="modal_tier" value="Talent & Elite Student" class="mt-0.5 text-[#0072ce] focus:ring-0">
              <div>
                <span class="font-bold text-slate-900 block">Talent & Student</span>
                <span class="text-[11px] text-slate-500">Sponsored Passes, Marvell R&D Track</span>
              </div>
            </label>
          </div>
        </div>

        <!-- Inputs -->
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
          <div>
            <label for="modal-fullname" class="block text-xs font-bold uppercase tracking-wider text-slate-700 mb-1">Full Name *</label>
            <input type="text" id="modal-fullname" required placeholder="Dr. Alex Johnson" class="w-full px-3.5 py-2.5 bg-white border border-slate-300 rounded-lg text-slate-900 placeholder:text-slate-400 text-sm focus:outline-none focus:border-[#0072ce] focus:ring-1 focus:ring-[#0072ce]">
          </div>
          <div>
            <label for="modal-email" class="block text-xs font-bold uppercase tracking-wider text-slate-700 mb-1">Work / Academic Email *</label>
            <input type="email" id="modal-email" required placeholder="alex@company.com" class="w-full px-3.5 py-2.5 bg-white border border-slate-300 rounded-lg text-slate-900 placeholder:text-slate-400 text-sm focus:outline-none focus:border-[#0072ce] focus:ring-1 focus:ring-[#0072ce]">
          </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
          <div>
            <label for="modal-phone" class="block text-xs font-bold uppercase tracking-wider text-slate-700 mb-1">Phone Number *</label>
            <input type="tel" id="modal-phone" required placeholder="+84 901 234 567" class="w-full px-3.5 py-2.5 bg-white border border-slate-300 rounded-lg text-slate-900 placeholder:text-slate-400 text-sm focus:outline-none focus:border-[#0072ce] focus:ring-1 focus:ring-[#0072ce]">
          </div>
          <div>
            <label for="modal-company" class="block text-xs font-bold uppercase tracking-wider text-slate-700 mb-1">Organization / Enterprise *</label>
            <input type="text" id="modal-company" required placeholder="Company or Institution" class="w-full px-3.5 py-2.5 bg-white border border-slate-300 rounded-lg text-slate-900 placeholder:text-slate-400 text-sm focus:outline-none focus:border-[#0072ce] focus:ring-1 focus:ring-[#0072ce]">
          </div>
        </div>

        <div>
          <label for="modal-role" class="block text-xs font-bold uppercase tracking-wider text-slate-700 mb-1">Professional Title *</label>
          <input type="text" id="modal-role" required placeholder="e.g. IC Design Architect / Principal Engineer" class="w-full px-3.5 py-2.5 bg-white border border-slate-300 rounded-lg text-slate-900 placeholder:text-slate-400 text-sm focus:outline-none focus:border-[#0072ce] focus:ring-1 focus:ring-[#0072ce]">
        </div>

        <div>
          <label class="block text-xs font-bold uppercase tracking-wider text-slate-700 mb-1.5">Primary Domain Interests *</label>
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs text-slate-700">
            <label class="flex items-center gap-2 p-2 rounded-lg bg-slate-50 border border-slate-200 cursor-pointer hover:border-slate-300">
              <input type="checkbox" name="modal_interests" value="IC Design (Analog/Digital)" checked class="rounded text-[#0072ce]">
              <span>IC Design (Analog & Digital)</span>
            </label>
            <label class="flex items-center gap-2 p-2 rounded-lg bg-slate-50 border border-slate-200 cursor-pointer hover:border-slate-300">
              <input type="checkbox" name="modal_interests" value="Advanced Packaging & CPO" class="rounded text-[#0072ce]">
              <span>Advanced Packaging & CPO</span>
            </label>
            <label class="flex items-center gap-2 p-2 rounded-lg bg-slate-50 border border-slate-200 cursor-pointer hover:border-slate-300">
              <input type="checkbox" name="modal_interests" value="AI Cloud Infrastructure" class="rounded text-[#0072ce]">
              <span>AI Cloud & Data Center</span>
            </label>
            <label class="flex items-center gap-2 p-2 rounded-lg bg-slate-50 border border-slate-200 cursor-pointer hover:border-slate-300">
              <input type="checkbox" name="modal_interests" value="Marvell R&D Partnership" class="rounded text-[#0072ce]">
              <span>R&D with Marvell Vietnam</span>
            </label>
          </div>
        </div>

        <div class="pt-2">
          <button type="submit" class="mrvll-btn-primary w-full justify-center text-xs py-3.5">
            <span>CONFIRM FREE REGISTRATION</span>
            <svg class="btn-arrow w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
          </button>
          <p class="text-[11px] text-slate-400 text-center mt-2.5">
            Information protected under <a href="https://www.marvell.com/privacy-statement.html" target="_blank" class="text-[#0072ce] underline">Marvell Privacy Statement</a>.
          </p>
        </div>
      </form>
    </div>
  </div>

  <!-- =========================================================================
       12. FREE REGISTRATION CONFIRMATION MODAL & TICKET PASS
       ========================================================================= -->
  <div id="ticket-modal" class="fixed inset-0 z-50 hidden modal-backdrop items-center justify-center p-4">
    <div class="modal-content-box bg-[#0c1017] max-w-lg w-full rounded-2xl border border-cyan-500/50 p-6 sm:p-8 shadow-2xl relative text-left">
      
      <!-- Close Button -->
      <button id="modal-close-btn" class="absolute top-4 right-4 text-slate-400 hover:text-white p-2 rounded-lg hover:bg-white/10 transition-colors">
        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
      </button>

      <!-- Badge -->
      <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-950/60 border border-emerald-500/30 text-emerald-400 text-xs font-bold uppercase tracking-wider mb-4">
        <span class="w-2 h-2 rounded-full bg-emerald-400 animate-ping"></span>
        REGISTRATION CONFIRMED • RSVP VALIDATED
      </div>

      <h3 class="text-2xl font-bold text-white mb-2">Digital Attendee Pass (E-Pass)</h3>
      <p class="text-xs text-slate-400 mb-6">Your registration code has been saved. Please present this QR code at the reception desk to claim your official summit badge.</p>

      <!-- Ticket Card Box -->
      <div class="bg-[#101726] border border-slate-700/80 rounded-xl p-5 relative overflow-hidden mb-6 shadow-xl">
        <div class="flex items-center justify-between pb-3 mb-3.5 border-b border-slate-800">
          <div class="flex items-center gap-2">
            {marvell_logo_ticket}
          </div>
          <span class="text-[9px] font-mono font-bold tracking-widest text-[#00b5e2] uppercase">OFFICIAL EXECUTIVE PASS</span>
        </div>

        <div class="flex items-center justify-between border-b border-slate-700 pb-3 mb-4">
          <div>
            <span class="text-[10px] text-slate-400 uppercase font-bold tracking-wider">REGISTRATION CODE</span>
            <span id="ticket-code" class="block font-mono text-base font-extrabold text-[#00b5e2]">MRVL-VSS-000000</span>
          </div>
          <span id="ticket-tier-badge" class="text-[10px] font-bold tracking-widest text-[#0072ce] bg-blue-950/80 px-2.5 py-1 rounded-md border border-blue-500/30 uppercase">INDUSTRY PASS</span>
        </div>

        <div class="grid grid-cols-2 gap-3 text-xs mb-4">
          <div>
            <span class="text-slate-400 block text-[10px] uppercase">Attendee Name:</span>
            <span id="ticket-name" class="font-bold text-white">--</span>
          </div>
          <div>
            <span class="text-slate-400 block text-[10px] uppercase">Email:</span>
            <span id="ticket-email" class="font-medium text-slate-300 truncate block">--</span>
          </div>
          <div>
            <span class="text-slate-400 block text-[10px] uppercase">Organization:</span>
            <span id="ticket-company" class="font-medium text-white truncate block">--</span>
          </div>
          <div>
            <span class="text-slate-400 block text-[10px] uppercase">Position:</span>
            <span id="ticket-role" class="font-medium text-slate-300 truncate block">--</span>
          </div>
        </div>

        <!-- Dynamic Real QR Code Visual -->
        <div class="pt-3 border-t border-slate-800 flex items-center justify-between">
          <div class="text-[10px] text-slate-400 font-mono">
            <span class="text-white font-bold">DATE: 23-NOV-2026 (08:00 - 20:10)</span><br>
            <span>VENUE: HO CHI MINH CITY</span><br>
            <span class="text-[#00b5e2]">STATUS: VALID TICKET</span>
          </div>
          <div class="w-16 h-16 bg-white p-1 rounded-lg flex items-center justify-center shrink-0 shadow-sm">
            <img id="ticket-qr-img" src="" alt="Check-in QR Code" class="w-full h-full object-contain">
          </div>
        </div>
      </div>

      <!-- Action Buttons -->
      <div class="flex flex-col sm:flex-row gap-3">
        <button id="download-ticket-btn" class="mrvll-btn-primary flex-1 justify-center text-xs py-3">
          <span>PRINT / SAVE TICKET (PDF)</span>
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 17h2a2 2 0 002-2v-4a2 2 0 00-2-2H5a2 2 0 00-2 2v4a2 2 0 002 2h2m2 4h6a2 2 0 002-2v-4a2 2 0 00-2-2H9a2 2 0 00-2 2v4h10z"/></svg>
        </button>
        <button id="add-calendar-btn" class="inline-flex items-center justify-center gap-2 bg-[#101726] border border-cyan-500/40 hover:border-cyan-400 text-[#00b5e2] text-xs font-bold uppercase tracking-wider py-3 px-4 rounded-lg transition-colors">
          <span>ADD TO CALENDAR (.ICS)</span>
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg>
        </button>
      </div>

    </div>
  </div>

  <!-- Main JavaScript File -->
  <script src="app.js"></script>
</body>
</html>
'''

out_path = os.path.join(base_dir, 'index.html')
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f'Successfully generated {out_path} in 100% English with modernized radius')

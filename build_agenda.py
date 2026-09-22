# -*- coding: utf-8 -*-
"""
Build script for dedicated Agenda page (agenda.html).
Compiles 24 sessions from agenda.json into a clean 2-column layout
with dedicated Speaker Cards (Avatar, Name, Title, Organization)
and Sponsor/Partner info.
"""
import json
import os

base_dir = r"d:\Landing Page\Landing Marvell"
json_path = os.path.join(base_dir, "agenda.json")
out_path = os.path.join(base_dir, "agenda.html")

with open(json_path, 'r', encoding='utf-8') as f:
    agenda_data = json.load(f)

agenda_cards_html = []
for item in agenda_data:
    session = item.get('session', 'morning')
    category = item.get('category', 'other')
    tag_label = category.upper()
    
    if category == 'keynote':
        tag_label = 'STRATEGIC KEYNOTE'
        tag_class = 'bg-blue-50 text-blue-700 border border-blue-200/80'
        spine_class = 'border-l-[5px] border-l-[#0072ce]'
        icon_color = 'text-[#0072ce]'
        badge_dot = '<span class="w-1.5 h-1.5 rounded-full bg-[#0072ce] animate-pulse"></span>'
    elif category == 'industry':
        tag_label = 'INDUSTRY PRESENTATION'
        tag_class = 'bg-cyan-50 text-cyan-800 border border-cyan-200/80'
        spine_class = 'border-l-[5px] border-l-[#00b5e2]'
        icon_color = 'text-[#00b5e2]'
        badge_dot = '<span class="w-1.5 h-1.5 rounded-full bg-[#00b5e2]"></span>'
    elif category == 'academia':
        tag_label = 'ACADEMIA & RESEARCH'
        tag_class = 'bg-emerald-50 text-emerald-800 border border-emerald-200/80'
        spine_class = 'border-l-[5px] border-l-emerald-500'
        icon_color = 'text-emerald-500'
        badge_dot = '<span class="w-1.5 h-1.5 rounded-full bg-emerald-500"></span>'
    elif category == 'networking':
        tag_label = 'NETWORKING & BANQUET'
        tag_class = 'bg-amber-50 text-amber-800 border border-amber-200/80'
        spine_class = 'border-l-[5px] border-l-amber-500'
        icon_color = 'text-amber-500'
        badge_dot = '<span class="w-1.5 h-1.5 rounded-full bg-amber-500"></span>'
    elif category == 'panel':
        tag_label = 'HIGH-LEVEL PANEL'
        tag_class = 'bg-purple-50 text-purple-800 border border-purple-200/80'
        spine_class = 'border-l-[5px] border-l-[#8b5cf6]'
        icon_color = 'text-[#8b5cf6]'
        badge_dot = '<span class="w-1.5 h-1.5 rounded-full bg-[#8b5cf6]"></span>'
    else:
        tag_label = 'CEREMONY & RECEPTION'
        tag_class = 'bg-slate-100 text-slate-700 border border-slate-200/80'
        spine_class = 'border-l-[5px] border-l-slate-400'
        icon_color = 'text-slate-500'
        badge_dot = '<span class="w-1.5 h-1.5 rounded-full bg-slate-400"></span>'

    # Speaker Module (Equal Sized & Structured Academic Rank)
    speaker_html = ""
    speaker = item.get('speaker')
    if speaker and isinstance(speaker, dict) and speaker.get('name'):
        prefix = speaker.get('prefix', '').strip()
        name = speaker.get('name', '').strip()
        title = speaker.get('title', '').strip()
        org = speaker.get('organization', '').strip()
        avatar = speaker.get('avatar', '').strip()

        # Split academic rank if present (e.g. Assoc. Prof. or Prof.)
        academic_tag = ""
        display_name = name
        if prefix.startswith("Assoc. Prof."):
            academic_tag = '<span class="text-[9px] font-extrabold text-slate-400 uppercase tracking-wider block leading-none mb-0.5">Assoc. Prof.</span>'
            rem_prefix = prefix.replace("Assoc. Prof.", "").strip()
            display_name = f"{rem_prefix} {name}".strip() if rem_prefix else name
        elif prefix.startswith("Prof."):
            academic_tag = '<span class="text-[9px] font-extrabold text-slate-400 uppercase tracking-wider block leading-none mb-0.5">Prof.</span>'
            rem_prefix = prefix.replace("Prof.", "").strip()
            display_name = f"{rem_prefix} {name}".strip() if rem_prefix else name
        else:
            display_name = f"{prefix} {name}".strip() if prefix else name

        title_html = f'<div class="text-[11px] font-semibold text-[#0072ce] leading-snug mt-0.5">{title}</div>' if title else ''
        # Organization name allows natural wrapping without losing letters
        org_html = f'<div class="text-[10px] text-slate-500 font-medium leading-snug mt-0.5">{org}</div>' if org else ''

        if avatar and os.path.exists(os.path.join(base_dir, avatar)):
            avatar_html = f'<img src="{avatar}" alt="{display_name}" class="w-11 h-11 rounded-full object-cover shrink-0 border border-blue-200 ring-1 ring-blue-50 shadow-sm">'
        else:
            avatar_html = '''<div class="w-11 h-11 rounded-full bg-gradient-to-b from-slate-50 to-blue-50/70 border border-slate-200/90 flex items-center justify-center shrink-0 shadow-sm text-slate-400"><svg class="w-5 h-5 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" /></svg></div>'''

        speaker_html = f'''
        <div class="w-full sm:w-[280px] min-h-[64px] py-2 px-2.5 flex items-center gap-2.5 rounded-xl bg-slate-50/90 border border-slate-200/80 shrink-0">
          {avatar_html}
          <div class="flex flex-col min-w-0 flex-1 justify-center">
            {academic_tag}
            <div class="text-[13px] font-bold text-slate-900 tracking-tight truncate">{display_name}</div>
            {title_html}
            {org_html}
          </div>
        </div>
        '''

    # Sponsor / Co-Host Module (2-Column Layout, Same Row, Matching Height)
    sponsor_html = ""
    sponsor = item.get('sponsor')
    if sponsor and isinstance(sponsor, dict) and sponsor.get('name'):
        s_name = sponsor.get('name', '').strip()
        s_logo = sponsor.get('logo', '').strip()

        logo_img_html = ""
        if s_logo and os.path.exists(os.path.join(base_dir, s_logo)):
            logo_img_html = f'<img src="{s_logo}" alt="{s_name}" class="h-6 max-h-7 w-auto object-contain shrink-0">'
        else:
            logo_img_html = f'<span class="text-xs font-black text-slate-800 tracking-wider uppercase">{s_name}</span>'

        sponsor_html = f'''
        <div class="inline-flex items-stretch rounded-xl border border-slate-200/90 bg-white shadow-sm shrink-0 min-h-[64px] self-stretch">
          <!-- Cột 1: Co-Host / Partner: (Canh giữa cột) -->
          <div class="px-2.5 py-2 bg-slate-50 border-r border-slate-200/80 flex items-center justify-center text-center shrink-0">
            <span class="text-[10px] font-bold tracking-wider uppercase text-slate-500 whitespace-nowrap">
              Co-Host / Partner:
            </span>
          </div>

          <!-- Cột 2: Logo (nền trong suốt) & Tên doanh nghiệp -->
          <div class="px-3 py-1.5 flex flex-col justify-center gap-1 bg-white">
            <div class="flex items-center">
              {logo_img_html}
            </div>
            <span class="text-[10px] font-bold text-slate-800 tracking-tight">{s_name}</span>
          </div>
        </div>
        '''

    # Combined Meta Row (Speaker & Co-Host on the same row)
    meta_row_html = ""
    if speaker_html or sponsor_html:
        meta_row_html = f'''
        <div class="mt-3 flex flex-wrap items-center gap-3">
          {speaker_html}
          {sponsor_html}
        </div>
        '''

    agenda_cards_html.append(f'''
    <div class="agenda-item-card group p-5 sm:p-6 rounded-2xl bg-white border border-slate-200/90 {spine_class} shadow-[0_2px_12px_rgba(0,0,0,0.03)] hover:shadow-[0_12px_30px_rgba(0,114,206,0.09)] hover:-translate-y-0.5 transition-all duration-200" data-session="{session}" data-category="{category}" data-session-id="{item['id']}">
      <div class="flex flex-col md:flex-row md:items-center justify-between gap-4 sm:gap-6">
        
        <!-- Left Column: Time & Category Key Badge (Vertically Centered, Right Bordered) -->
        <div class="shrink-0 md:w-64 flex flex-col items-start justify-center gap-2 pb-3 md:pb-0 border-b md:border-b-0 md:border-r border-slate-100 md:pr-6">
          <div class="flex items-center gap-2">
            <svg class="w-4 h-4 {icon_color} shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
            <span class="font-mono text-base font-extrabold text-slate-900 tracking-tight whitespace-nowrap">{item['from']} &ndash; {item['to']}</span>
          </div>
          <div class="inline-flex items-center gap-1.5 text-[10px] font-bold tracking-wider uppercase px-2.5 py-1 rounded-md {tag_class}">
            {badge_dot}
            <span>{tag_label}</span>
          </div>
        </div>

        <!-- Right Column: Title + Combined Meta Row (Speaker & Co-Host Side-by-Side) -->
        <div class="flex-1 min-w-0 flex flex-col justify-center">
          <h3 class="text-base sm:text-lg font-bold text-slate-900 leading-snug group-hover:text-[#0072ce] transition-colors">
            {item['description']}
          </h3>
          {meta_row_html}
        </div>

      </div>
    </div>
    ''')

cards_block = "\n".join(agenda_cards_html)

html = f'''<!DOCTYPE html>
<html lang="en" class="scroll-smooth" prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb#" itemscope itemtype="http://schema.org/WebPage">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Official Summit Timetable | The 1st Vietnam Semiconductor Summit 2026</title>
  
  <!-- Canonical & Standard SEO Meta Tags -->
  <link rel="canonical" href="https://minhnntrademkt.github.io/vietnam-semiconductor-summit-2026/agenda.html">
  <meta name="title" content="Official Summit Timetable | The 1st Vietnam Semiconductor Summit 2026">
  <meta name="description" content="Dedicated timetable and strategic agenda for The 1st Vietnam Semiconductor Summit 2026 hosted by Marvell Technology. Monday, November 23, 2026, Ho Chi Minh City, Vietnam.">
  <meta name="image" content="https://minhnntrademkt.github.io/vietnam-semiconductor-summit-2026/images/og-banner.jpg?v=20260914_1315">
  <meta name="thumbnail" content="https://minhnntrademkt.github.io/vietnam-semiconductor-summit-2026/images/og-banner.jpg?v=20260914_1315">

  <!-- Schema.org for Google & Zalo -->
  <meta itemprop="name" content="Official Summit Timetable | The 1st Vietnam Semiconductor Summit 2026">
  <meta itemprop="description" content="Dedicated timetable and strategic agenda for The 1st Vietnam Semiconductor Summit 2026 hosted by Marvell Technology. Monday, November 23, 2026, Ho Chi Minh City, Vietnam.">
  <meta itemprop="image" content="https://minhnntrademkt.github.io/vietnam-semiconductor-summit-2026/images/og-banner.jpg?v=20260914_1315">

  <!-- Open Graph / Facebook / LinkedIn / Zalo -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://minhnntrademkt.github.io/vietnam-semiconductor-summit-2026/agenda.html">
  <meta property="og:site_name" content="Vietnam Semiconductor Summit 2026">
  <meta property="og:locale" content="en_US">
  <meta property="og:title" content="Official Summit Timetable | The 1st Vietnam Semiconductor Summit 2026">
  <meta name="og:title" content="Official Summit Timetable | The 1st Vietnam Semiconductor Summit 2026">
  <meta property="og:description" content="Dedicated timetable and strategic agenda for The 1st Vietnam Semiconductor Summit 2026 hosted by Marvell Technology. Monday, November 23, 2026, Ho Chi Minh City, Vietnam.">
  <meta name="og:description" content="Dedicated timetable and strategic agenda for The 1st Vietnam Semiconductor Summit 2026 hosted by Marvell Technology. Monday, November 23, 2026, Ho Chi Minh City, Vietnam.">
  <meta property="og:image" content="https://minhnntrademkt.github.io/vietnam-semiconductor-summit-2026/images/og-banner.jpg?v=20260914_1315">
  <meta property="og:image:url" content="https://minhnntrademkt.github.io/vietnam-semiconductor-summit-2026/images/og-banner.jpg?v=20260914_1315">
  <meta property="og:image:secure_url" content="https://minhnntrademkt.github.io/vietnam-semiconductor-summit-2026/images/og-banner.jpg?v=20260914_1315">
  <meta name="og:image" content="https://minhnntrademkt.github.io/vietnam-semiconductor-summit-2026/images/og-banner.jpg?v=20260914_1315">
  <meta property="og:image:type" content="image/jpeg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="The 1st Vietnam Semiconductor Summit 2026 Official Banner">
  <link rel="image_src" href="https://minhnntrademkt.github.io/vietnam-semiconductor-summit-2026/images/og-banner.jpg?v=20260914_1315">

  <!-- Twitter / X Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Official Summit Timetable | The 1st Vietnam Semiconductor Summit 2026">
  <meta name="twitter:description" content="Dedicated timetable and strategic agenda for The 1st Vietnam Semiconductor Summit 2026 hosted by Marvell Technology. Monday, November 23, 2026, Ho Chi Minh City, Vietnam.">
  <meta name="twitter:image" content="https://minhnntrademkt.github.io/vietnam-semiconductor-summit-2026/images/og-banner.jpg?v=20260914_1315">
  
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
  
  <link rel="icon" type="image/svg+xml" href="favicon.svg">
  <link rel="alternate icon" href="favicon.svg">
  <link rel="stylesheet" href="styles.css?v=20260922_0805">

  <style>
    body {{
      font-family: 'Plus Jakarta Sans', Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
    }}
  </style>
</head>
<body class="bg-[#f8fafc] text-slate-800 antialiased min-h-screen flex flex-col">

  <!-- =========================================================================
       1. STAGING HEADER NAVBAR (OFFICIAL BLACK MARVELL LOGO)
       ========================================================================= -->
  <header class="sticky top-0 z-40 bg-white/95 backdrop-blur-md border-b border-slate-200">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between h-20">
        
        <!-- Brand Logo & Summit Title -->
        <a href="index.html" class="flex items-center gap-3 sm:gap-4 shrink-0 group">
          <div class="flex items-center shrink-0">
            <!-- Marvell Official Black Logo -->
            <img src="images/marvell-logo-black.png" alt="Marvell Technology Logo" class="h-8 sm:h-9 md:h-10 w-auto object-contain">
          </div>
          <div class="hidden sm:block h-6 w-px bg-slate-300 shrink-0"></div>
          <div class="hidden sm:flex flex-col">
            <span class="text-[13px] font-bold tracking-tight text-slate-900 group-hover:text-[#0072ce] transition-colors leading-snug">Vietnam Semiconductor Summit 2026</span>
            <span class="text-[10px] font-bold text-[#0072ce] uppercase tracking-wider">Official Agenda Staging Environment</span>
          </div>
        </a>

        <!-- Header Actions -->
        <div class="flex items-center gap-3">
          <a href="index.html" class="inline-flex items-center gap-2 px-3.5 py-2 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-700 text-xs font-bold transition-all">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"/></svg>
            <span>Back to Main Summit</span>
          </a>
          <a href="index.html#register" class="mrvll-btn-primary text-xs py-2 px-4 shadow-sm">
            <span>GET FREE RSVP</span>
          </a>
        </div>

      </div>
    </div>
  </header>

  <!-- =========================================================================
       2. SUB-HERO BANNER FOR AGENDA
       ========================================================================= -->
  <section class="relative bg-[#05070a] text-white py-14 lg:py-16 overflow-hidden border-b border-slate-800">
    <div class="absolute inset-0 bg-hero-grid opacity-15 pointer-events-none"></div>
    <div class="absolute -top-32 -left-32 w-96 h-96 bg-[#0072ce]/20 rounded-full blur-3xl pointer-events-none"></div>
    <div class="absolute top-1/2 -right-32 w-96 h-96 bg-[#00b5e2]/15 rounded-full blur-3xl pointer-events-none"></div>

    <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10 text-center">
      <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-blue-950/70 border border-blue-500/40 text-xs font-bold text-[#00b5e2] tracking-wider uppercase mb-4 shadow-[0_0_15px_rgba(0,181,226,0.2)]">
        <span class="w-2 h-2 rounded-full bg-[#00b5e2] animate-pulse"></span>
        MARVELL TECHNOLOGY PRESENTS • OFFICIAL TIMETABLE
      </div>
      <h1 class="text-3xl sm:text-4xl lg:text-5xl font-extrabold text-white tracking-tight">
        Official Summit Agenda & Timetable
      </h1>
      <p class="mt-4 text-sm sm:text-base text-slate-300 max-w-2xl mx-auto leading-relaxed">
        Monday, November 23, 2026 • Ho Chi Minh City, Vietnam. Full strategic congress timetable uniting Government leadership, industry pioneers, and academic research luminaries.
      </p>

      <!-- Search Box & Summary Bar -->
      <div class="mt-8 max-w-xl mx-auto flex flex-col sm:flex-row gap-2.5">
        <div class="relative flex-1">
          <svg class="w-4 h-4 text-slate-400 absolute left-3.5 top-1/2 -translate-y-1/2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
          <input type="text" id="agenda-search-input" placeholder="Search sessions, speakers, or topics (e.g. Noam, Intel, CPO)..." class="w-full pl-10 pr-4 py-2.5 rounded-lg bg-slate-900/90 border border-slate-700 text-xs text-white placeholder-slate-400 focus:outline-none focus:border-[#00b5e2] focus:ring-1 focus:ring-[#00b5e2]">
        </div>
        <button id="reset-filters-btn" class="px-4 py-2.5 rounded-lg bg-slate-800 hover:bg-slate-700 border border-slate-700 text-xs font-bold text-slate-300 transition-colors">
          Reset Filters
        </button>
      </div>

      <div class="mt-6 flex flex-wrap items-center justify-center gap-4 text-xs font-mono text-slate-400">
        <span class="flex items-center gap-1.5"><span class="w-2 h-2 rounded-full bg-[#0072ce]"></span> Technical & Strategic Tracks</span>
        <span class="flex items-center gap-1.5"><span class="w-2 h-2 rounded-full bg-[#00b5e2]"></span> 08:00 – 20:10 ICT</span>
        <span class="flex items-center gap-1.5"><span class="w-2 h-2 rounded-full bg-emerald-500"></span> Grand Ballroom & Tech Halls</span>
        <span class="flex items-center gap-1.5"><span class="w-2 h-2 rounded-full bg-purple-500"></span> 100% Free RSVP</span>
      </div>
    </div>
  </section>

  <!-- =========================================================================
       3. INTERACTIVE AGENDA CONTAINER WITH 2-COLUMN & SPEAKER CARDS
       ========================================================================= -->
  <main class="flex-1 py-12 lg:py-16 max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 w-full">
    
    <!-- Session Switcher Tabs -->
    <div class="flex flex-wrap items-center justify-center gap-2 mb-6 bg-slate-200/70 p-1.5 rounded-xl max-w-xl mx-auto border border-slate-300/60">
      <button class="agenda-tab-btn active px-4 py-2 text-xs font-bold rounded-lg bg-slate-900 text-white shadow-sm transition-all" data-session="all">All Sessions</button>
      <button class="agenda-tab-btn px-4 py-2 text-xs font-bold rounded-lg text-slate-600 hover:text-slate-900 transition-all" data-session="morning">Morning Sessions</button>
      <button class="agenda-tab-btn px-4 py-2 text-xs font-bold rounded-lg text-slate-600 hover:text-slate-900 transition-all" data-session="afternoon">Afternoon Sessions</button>
    </div>

    <!-- Category Filter Pills -->
    <div class="flex flex-wrap items-center justify-center gap-2 mb-8">
      <button class="agenda-filter-pill active inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full border border-[#0072ce] bg-blue-50 text-[#0072ce] font-semibold text-xs transition-all shadow-sm" data-category="all">
        <span class="w-2 h-2 rounded-full bg-[#0072ce]"></span>
        <span>All Sessions</span>
      </button>
      <button class="agenda-filter-pill inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full border border-slate-200 bg-white text-slate-600 hover:border-slate-300 hover:text-slate-900 text-xs font-medium transition-all" data-category="keynote">
        <span class="w-2 h-2 rounded-full bg-[#0072ce]"></span>
        <span>Keynotes</span>
      </button>
      <button class="agenda-filter-pill inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full border border-slate-200 bg-white text-slate-600 hover:border-slate-300 hover:text-slate-900 text-xs font-medium transition-all" data-category="industry">
        <span class="w-2 h-2 rounded-full bg-[#00b5e2]"></span>
        <span>Industry</span>
      </button>
      <button class="agenda-filter-pill inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full border border-slate-200 bg-white text-slate-600 hover:border-slate-300 hover:text-slate-900 text-xs font-medium transition-all" data-category="academia">
        <span class="w-2 h-2 rounded-full bg-emerald-500"></span>
        <span>Academia & Research</span>
      </button>
      <button class="agenda-filter-pill inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full border border-slate-200 bg-white text-slate-600 hover:border-slate-300 hover:text-slate-900 text-xs font-medium transition-all" data-category="panel">
        <span class="w-2 h-2 rounded-full bg-[#8b5cf6]"></span>
        <span>Strategic Panel</span>
      </button>
      <button class="agenda-filter-pill inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full border border-slate-200 bg-white text-slate-600 hover:border-slate-300 hover:text-slate-900 text-xs font-medium transition-all" data-category="networking">
        <span class="w-2 h-2 rounded-full bg-amber-500"></span>
        <span>Networking</span>
      </button>
    </div>

    <!-- Active Filter Counter -->
    <div class="flex items-center justify-between text-xs text-slate-500 mb-4 pb-2 border-b border-slate-200">
      <div>
        Showing <span id="visible-sessions-count" class="font-bold text-slate-900">{len(agenda_data)}</span> sessions
      </div>
      <div class="text-[11px] text-slate-400">
        Presentation & Speaker Focus
      </div>
    </div>

    <!-- Official Timetable Sessions List -->
    <div id="agenda-cards-container" class="space-y-3.5">
{cards_block}
    </div>

    <!-- Empty State if no sessions match filter -->
    <div id="no-sessions-found" class="hidden text-center py-16 bg-white rounded-2xl border border-slate-200">
      <svg class="w-12 h-12 text-slate-300 mx-auto mb-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9.172 16.172a4 4 0 015.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
      <h3 class="text-base font-bold text-slate-800">No sessions match your search</h3>
      <p class="text-xs text-slate-500 mt-1">Try resetting the session or category filters above.</p>
    </div>

  </main>

  <!-- =========================================================================
       4. CORPORATE FOOTER
       ========================================================================= -->
  <footer class="bg-white py-12 border-t border-slate-200 text-xs text-slate-500 mt-auto">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex flex-col sm:flex-row items-center justify-between gap-6 pb-6 border-b border-slate-200">
        <div class="flex items-center gap-4">
          <img src="images/marvell-logo-black.png" alt="Marvell Technology Logo" class="h-7 w-auto object-contain">
          <span class="text-slate-400 font-mono text-[11px]">| Semiconductor Summit 2026</span>
        </div>
        <div class="flex items-center gap-6">
          <a href="index.html" class="hover:text-slate-900 font-medium transition-colors">Main Summit</a>
          <a href="index.html#speakers" class="hover:text-slate-900 font-medium transition-colors">Speakers</a>
          <a href="index.html#panel" class="hover:text-slate-900 font-medium transition-colors">Strategic Panel</a>
          <a href="index.html#register" class="hover:text-slate-900 font-bold text-[#0072ce] transition-colors">RSVP Pass</a>
        </div>
      </div>

      <!-- Marvell Vietnam Footprint Grid -->
      <div class="py-6 grid grid-cols-1 md:grid-cols-3 gap-4 border-b border-slate-200/80 text-[11px] text-slate-600">
        <div>
          <span class="font-bold text-slate-900 uppercase block mb-1">Headquarters (ET6 Office)</span>
          <p class="font-semibold text-slate-800">Etown6 Tower</p>
          <p class="text-slate-500">364 Cong Hoa, Tan Binh Ward, Ho Chi Minh City</p>
        </div>
        <div>
          <span class="font-bold text-slate-900 uppercase block mb-1">R&D Center (UOA Office)</span>
          <p class="font-semibold text-slate-800">UOA Tower</p>
          <p class="text-slate-500">6 Tan Trao, Tan My Ward, District 7, Ho Chi Minh City</p>
        </div>
        <div>
          <span class="font-bold text-slate-900 uppercase block mb-1">R&D Center (SP2 Da Nang)</span>
          <p class="font-semibold text-slate-800">Software Park 2 (SP2)</p>
          <p class="text-slate-500">Thuan Phuoc Ward, Hai Chau District, Da Nang City</p>
        </div>
      </div>

      <div class="pt-6 flex flex-col sm:flex-row items-center justify-between gap-4 text-[11px] text-slate-400">
        <span>&copy; 2026 Marvell Technology, Inc. All rights reserved.</span>
        <span>The 1st Vietnam Semiconductor Summit &bull; Monday, November 23, 2026</span>
      </div>
    </div>
  </footer>

  <!-- =========================================================================
       5. INTERACTIVE FILTER & SEARCH SCRIPT
       ========================================================================= -->
  <script>
    document.addEventListener('DOMContentLoaded', () => {{
      const tabBtns = document.querySelectorAll('.agenda-tab-btn');
      const filterPills = document.querySelectorAll('.agenda-filter-pill');
      const cards = document.querySelectorAll('.agenda-item-card');
      const searchInput = document.getElementById('agenda-search-input');
      const resetBtn = document.getElementById('reset-filters-btn');
      const counterEl = document.getElementById('visible-sessions-count');
      const emptyState = document.getElementById('no-sessions-found');

      let currentSession = 'all';
      let currentCategory = 'all';
      let searchQuery = '';

      function applyFilters() {{
        let visibleCount = 0;

        cards.forEach(card => {{
          const cardSession = card.getAttribute('data-session');
          const cardCategory = card.getAttribute('data-category');
          const cardText = card.innerText.toLowerCase();

          const matchesSession = (currentSession === 'all' || cardSession === currentSession);
          const matchesCategory = (currentCategory === 'all' || cardCategory === currentCategory);
          const matchesSearch = (!searchQuery || cardText.includes(searchQuery));

          if (matchesSession && matchesCategory && matchesSearch) {{
            card.classList.remove('hidden');
            visibleCount++;
          }} else {{
            card.classList.add('hidden');
          }}
        }});

        if (counterEl) counterEl.textContent = visibleCount;
        if (emptyState) {{
          if (visibleCount === 0) {{
            emptyState.classList.remove('hidden');
          }} else {{
            emptyState.classList.add('hidden');
          }}
        }}
      }}

      // Tab Buttons
      tabBtns.forEach(btn => {{
        btn.addEventListener('click', () => {{
          tabBtns.forEach(b => {{
            b.classList.remove('active', 'bg-slate-900', 'text-white', 'shadow-sm');
            b.classList.add('text-slate-600');
          }});
          btn.classList.add('active', 'bg-slate-900', 'text-white', 'shadow-sm');
          btn.classList.remove('text-slate-600');
          currentSession = btn.getAttribute('data-session');
          applyFilters();
        }});
      }});

      // Category Filter Pills
      filterPills.forEach(pill => {{
        pill.addEventListener('click', () => {{
          filterPills.forEach(p => {{
            p.classList.remove('active', 'border-[#0072ce]', 'bg-blue-50', 'text-[#0072ce]', 'shadow-sm');
            p.classList.add('border-slate-200', 'bg-white', 'text-slate-600');
          }});
          pill.classList.add('active', 'border-[#0072ce]', 'bg-blue-50', 'text-[#0072ce]', 'shadow-sm');
          pill.classList.remove('border-slate-200', 'bg-white', 'text-slate-600');
          currentCategory = pill.getAttribute('data-category');
          applyFilters();
        }});
      }});

      // Search Input
      if (searchInput) {{
        searchInput.addEventListener('input', (e) => {{
          searchQuery = e.target.value.trim().toLowerCase();
          applyFilters();
        }});
      }}

      // Reset Button
      if (resetBtn) {{
        resetBtn.addEventListener('click', () => {{
          if (searchInput) searchInput.value = '';
          searchQuery = '';
          currentSession = 'all';
          currentCategory = 'all';
          
          tabBtns.forEach((b, idx) => {{
            if (idx === 0) {{
              b.classList.add('active', 'bg-slate-900', 'text-white', 'shadow-sm');
              b.classList.remove('text-slate-600');
            }} else {{
              b.classList.remove('active', 'bg-slate-900', 'text-white', 'shadow-sm');
              b.classList.add('text-slate-600');
            }}
          }});

          filterPills.forEach((p, idx) => {{
            if (idx === 0) {{
              p.classList.add('active', 'border-[#0072ce]', 'bg-blue-50', 'text-[#0072ce]', 'shadow-sm');
              p.classList.remove('border-slate-200', 'bg-white', 'text-slate-600');
            }} else {{
              p.classList.remove('active', 'border-[#0072ce]', 'bg-blue-50', 'text-[#0072ce]', 'shadow-sm');
              p.classList.add('border-slate-200', 'bg-white', 'text-slate-600');
            }}
          }});

          applyFilters();
        }});
      }}
    }});
  </script>
</body>
</html>
'''

with open(out_path, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Successfully generated {out_path} with 2-column layout and Speaker Cards!")

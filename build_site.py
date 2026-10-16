# -*- coding: utf-8 -*-
"""
Vietnam Semiconductor Summit 2026 - Site Generator
Host Organization: Marvell Technology, Inc. (NASDAQ: MRVL)
Language: 100% International Standard English
Design System: Marvell Marketing palette, sharp UI corners, accessible typography
"""
import json
import os

base_dir = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(base_dir, 'agenda.json'), 'r', encoding='utf-8') as f:
    agenda_data = json.load(f)

def get_speaker_id(speaker_dict):
    if not speaker_dict or not isinstance(speaker_dict, dict):
        return ""
    if speaker_dict.get('id'):
        return speaker_dict['id']
    avatar = speaker_dict.get('avatar', '').lower()
    name = speaker_dict.get('name', '').lower()
    if 'le-quang-dam' in avatar or 'quang dam' in name or 'quang-dam' in name:
        return 'le-quang-dam'
    elif 'noam' in avatar or 'noam' in name:
        return 'noam-mizrahi'
    elif 'van-duoc' in avatar or 'duoc' in name:
        return 'nguyen-van-duoc'
    elif 'melissa' in avatar or 'melissa' in name:
        return 'melissa-brown'
    elif 'khanh' in avatar or 'khanh' in name:
        return 'nguyen-quang-khanh'
    elif 'thanh-loan' in avatar or 'pham-nguyen' in name or 'pham' in name:
        return 'pham-nguyen-thanh-loan'
    elif 'hai' in avatar or 'hai' in name:
        return 'hai-hoang'
    elif 'thieu-phuong-nam' in avatar or 'thieu' in name or 'nam' in name:
        return 'thieu-phuong-nam'
    elif 'lam-trinh' in avatar or 'lam trinh' in name:
        return 'lam-trinh'
    elif 'bich-yen' in avatar or 'bich-yen' in name:
        return 'nguyen-bich-yen'
    elif 'khoa' in avatar or 'khoa' in name:
        return 'tran-dac-khoa'
    elif 'hoang-trang' in avatar or 'trang hoang' in name or 'hoang' in name:
        return 'hoang-trang'
    elif 'loan-nguyen' in avatar or 'loan' in name:
        return 'loan-nguyen'
    elif 'thanh-mai' in avatar or 'mai' in name:
        return 'nguyen-thi-thanh-mai'
    elif 'ky-phung' in avatar or 'phung' in name:
        return 'nguyen-ky-phung'
    elif 'thuat' in avatar or 'thuat' in name:
        return 'thuat-nguyen'
    return ""

def render_speaker_card(speaker_dict, is_moderator=False):
    if not speaker_dict or not isinstance(speaker_dict, dict) or not speaker_dict.get('name'):
        return ""
    prefix = speaker_dict.get('prefix', '').strip()
    name = speaker_dict.get('name', '').strip()
    title = speaker_dict.get('title', '').strip()
    org = speaker_dict.get('organization', '').strip()
    avatar = speaker_dict.get('avatar', '').strip()
    speaker_id = get_speaker_id(speaker_dict)

    is_mod = is_moderator or speaker_dict.get('is_moderator') or 'moderator' in title.lower()

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
    org_html = f'<div class="text-[10px] text-slate-500 font-medium leading-snug mt-0.5">{org}</div>' if org else ''

    avatar_clean = avatar.split('?')[0] if avatar else ''
    if avatar_clean and os.path.exists(os.path.join(base_dir, avatar_clean)):
        border_avatar = "border-2 border-[#0072ce]" if is_mod else "border border-blue-200 ring-1 ring-blue-50"
        avatar_core = f'<img src="{avatar}" alt="{display_name}" class="w-11 h-11 rounded-full object-cover object-top shrink-0 {border_avatar} shadow-sm" style="object-position: center top;">'
    else:
        border_style = "border-2 border-[#0072ce]" if is_mod else "border border-slate-200/80"
        avatar_core = f'''<div class="w-11 h-11 rounded-full {border_style} bg-slate-100 flex items-end justify-center shrink-0 overflow-hidden shadow-sm">
          <svg class="w-9 h-9 text-slate-400/60 translate-y-1" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
            <path d="M12 12c2.7 0 4.8-2.1 4.8-4.8S14.7 2.4 12 2.4 7.2 4.5 7.2 7.2 9.3 12 12 12zm0 2.4c-3.2 0-9.6 1.6-9.6 4.8v2.4h19.2v-2.4c0-3.2-6.4-4.8-9.6-4.8z"/>
          </svg>
        </div>'''

    if is_mod:
        avatar_html = f'''<div class="relative shrink-0 flex items-center justify-center">
        {avatar_core}
        <span class="absolute -bottom-1 left-1/2 -translate-x-1/2 px-1 py-[0.5px] rounded bg-[#0072ce] text-white text-[7.5px] font-extrabold tracking-wider uppercase leading-none shadow-xs whitespace-nowrap z-10 pointer-events-none">MODERATOR</span>
      </div>'''
    else:
        avatar_html = avatar_core

    data_attr = f'data-speaker-id="{speaker_id}"' if speaker_id else ''
    click_classes = "speaker-card cursor-pointer group/spk hover:border-[#0072ce] hover:bg-blue-50/70 hover:shadow-md hover:-translate-y-0.5 transition-all duration-200" if speaker_id else ""
    arrow_html = f'<svg class="w-3.5 h-3.5 text-slate-400 group-hover/spk:text-[#0072ce] group-hover/spk:translate-x-0.5 transition-all shrink-0 opacity-60 group-hover/spk:opacity-100" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>' if speaker_id else ""
    title_attr = f'title="Click to view {display_name} profile & presentation abstract"' if speaker_id else ""

    card_styling = "w-full sm:w-[285px] min-h-[64px] py-2 px-2.5 flex items-center gap-2.5 rounded-xl bg-slate-50/90 border border-slate-200/80 shrink-0"
    name_html = f'<div class="text-[13px] font-bold text-slate-900 group-hover/spk:text-[#0072ce] tracking-tight truncate transition-colors">{display_name}</div>'

    return f'''
    <div class="{click_classes} {card_styling}" {data_attr} {title_attr}>
      {avatar_html}
      <div class="flex flex-col min-w-0 flex-1 justify-center">
        {academic_tag}
        {name_html}
        {title_html}
        {org_html}
      </div>
      {arrow_html}
    </div>
    '''

agenda_cards_html = []
for item in agenda_data:
    session = item.get('session', 'morning')
    category = item.get('category', 'other')
    tag_label = category.upper()
    
    if category == 'opening':
        tag_label = 'OPENING SPEECH'
        tag_class = 'bg-blue-50 text-[#0072ce] border border-blue-200/80 font-bold'
        spine_class = 'border-l-[5px] border-l-[#0072ce]'
        icon_color = 'text-[#0072ce]'
        badge_dot = '<span class="w-1.5 h-1.5 rounded-full bg-[#0072ce] animate-pulse"></span>'
    elif category == 'closing':
        tag_label = 'CLOSING CEREMONY'
        tag_class = 'bg-blue-50 text-blue-800 border border-blue-200/80 font-bold'
        spine_class = 'border-l-[5px] border-l-blue-600'
        icon_color = 'text-blue-600'
        badge_dot = '<span class="w-1.5 h-1.5 rounded-full bg-blue-600"></span>'
    elif category == 'keynote':
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
        tag_class = 'bg-teal-50 text-teal-800 border border-teal-200/80'
        spine_class = 'border-l-[5px] border-l-teal-500'
        icon_color = 'text-teal-500'
        badge_dot = '<span class="w-1.5 h-1.5 rounded-full bg-teal-500"></span>'
    elif category == 'networking':
        tag_label = 'NETWORKING & BANQUET'
        tag_class = 'bg-yellow-50 text-yellow-800 border border-yellow-200/80'
        spine_class = 'border-l-[5px] border-l-yellow-500'
        icon_color = 'text-yellow-500'
        badge_dot = '<span class="w-1.5 h-1.5 rounded-full bg-yellow-500"></span>'
    elif category == 'panel':
        tag_label = 'HIGH-LEVEL PANEL'
        tag_class = 'bg-cyan-50 text-cyan-800 border border-cyan-200/80'
        spine_class = 'border-l-[5px] border-l-[#00c7b1]'
        icon_color = 'text-[#00c7b1]'
        badge_dot = '<span class="w-1.5 h-1.5 rounded-full bg-[#00c7b1]"></span>'
    else:
        tag_label = 'CEREMONY & RECEPTION'
        tag_class = 'bg-slate-100 text-slate-700 border border-slate-200/80'
        spine_class = 'border-l-[5px] border-l-slate-400'
        icon_color = 'text-slate-500'
        badge_dot = '<span class="w-1.5 h-1.5 rounded-full bg-slate-400"></span>'

    # Speaker & Panelists Modules (All rendered as Equal Sized & Structured Speaker Cards)
    speaker_cards_html = []
    if item.get('moderator'):
        m_card = render_speaker_card(item['moderator'], is_moderator=True)
        if m_card:
            speaker_cards_html.append(m_card)
    if item.get('speaker'):
        s_card = render_speaker_card(item['speaker'])
        if s_card:
            speaker_cards_html.append(s_card)
    if item.get('panelists') and isinstance(item['panelists'], list):
        for p in item['panelists']:
            p_card = render_speaker_card(p)
            if p_card:
                speaker_cards_html.append(p_card)
    all_speakers_html = "\n".join(speaker_cards_html)

    # Sponsor / Co-Host Module (2-Column Layout, Same Row, Matching Height)
    sponsor_html = ""
    sponsor = item.get('sponsor')
    if sponsor and isinstance(sponsor, dict) and sponsor.get('name'):
        s_name = sponsor.get('name', '').strip()
        s_logo = sponsor.get('logo', '').strip()

        logo_img_html = ""
        s_logo_clean = s_logo.split('?')[0] if s_logo else ''
        if s_logo_clean and os.path.exists(os.path.join(base_dir, s_logo_clean)):
            logo_img_html = f'<img src="{s_logo}" alt="{s_name}" class="h-6 max-h-7 w-auto object-contain shrink-0">'
        else:
            logo_img_html = f'<span class="text-xs font-black text-slate-800 tracking-wider uppercase">{s_name}</span>'

        sponsor_html = f'''
        <div class="inline-flex items-stretch rounded-xl border border-slate-200/90 bg-white shadow-sm shrink-0 min-h-[64px] self-stretch">
          <!-- Cá»™t 1: Partner: (Canh giá»¯a cá»™t) -->
          <div class="px-2.5 py-2 bg-slate-50 border-r border-slate-200/80 flex items-center justify-center text-center shrink-0">
            <span class="text-[10px] font-bold tracking-wider uppercase text-slate-500 whitespace-nowrap">
              Partner:
            </span>
          </div>

          <!-- Cá»™t 2: Logo (ná»n trong suá»‘t) & TÃªn doanh nghiá»‡p -->
          <div class="px-3 py-1.5 flex flex-col justify-center gap-1 bg-white">
            <div class="flex items-center">
              {logo_img_html}
            </div>
            <span class="text-[10px] font-bold text-slate-800 tracking-tight">{s_name}</span>
          </div>
        </div>
        '''

    # Combined Meta Row (All Speaker Cards & Partner on the same row)
    meta_row_html = ""
    if all_speakers_html or sponsor_html:
        meta_row_html = f'''
        <div class="mt-3 flex flex-wrap items-center gap-3">
          {all_speakers_html}
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

        <!-- Right Column: Title + Combined Meta Row (All Speakers & Partner Side-by-Side) -->
        <div class="flex-1 min-w-0 flex flex-col justify-center">
          <h3 class="text-base sm:text-lg font-bold text-slate-900 leading-snug group-hover:text-[#0072ce] transition-colors">
            {item['description']}
          </h3>
          {meta_row_html}
        </div>

      </div>
    </div>
    ''')

agenda_items_rendered = '\n'.join(agenda_cards_html)

def get_marvell_logo(css_class="h-12 w-auto", asset="marvell-logo.svg"):
    return f'<img src="{asset}?v=20261016_brand" alt="Marvell" class="{css_class} object-contain" decoding="async">'

marvell_logo_header = get_marvell_logo("brand-logo-horizontal h-12 sm:h-14 w-auto")
marvell_logo_footer = get_marvell_logo("h-12 w-auto")
marvell_logo_ticket = get_marvell_logo("h-10 w-auto", "marvell-logo-white.svg")
marvell_logo_partner = get_marvell_logo("h-24 sm:h-28 w-auto", "marvell-logo-stacked.svg")
marvell_logo_host_card = get_marvell_logo("h-16 sm:h-20 w-auto")

html_content = f'''<!DOCTYPE html>
<html lang="en" class="scroll-smooth" prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb#" itemscope itemtype="http://schema.org/WebPage">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Vietnam Semiconductor Summit 2026 | Marvell Technology</title>
  
  <!-- Anti-Cache Directives (Forces Browser Revalidation) -->
  <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
  <meta http-equiv="Pragma" content="no-cache">
  <meta http-equiv="Expires" content="0">
  
  <!-- Canonical & Standard SEO Meta Tags -->
  <link rel="canonical" href="https://minhnntrademkt.github.io/vietnam-semiconductor-summit-2026/">
  <meta name="title" content="Vietnam Semiconductor Summit 2026 | Marvell Technology">
  <meta name="description" content="Accelerating Vietnam's Semiconductor Revolution. Official Inaugural Congress uniting Government leadership, global chipmakers, and academic scholars. Monday, November 23, 2026, Ho Chi Minh City, Vietnam.">
  <meta name="image" content="https://minhnntrademkt.github.io/vietnam-semiconductor-summit-2026/images/og-banner.jpg?v=20260914_1315">
  <meta name="thumbnail" content="https://minhnntrademkt.github.io/vietnam-semiconductor-summit-2026/images/og-banner.jpg?v=20260914_1315">

  <!-- Schema.org for Google & Zalo -->
  <meta itemprop="name" content="Vietnam Semiconductor Summit 2026 | Marvell Technology">
  <meta itemprop="description" content="Accelerating Vietnam's Semiconductor Revolution. Official Inaugural Congress uniting Government leadership, global chipmakers, and academic scholars. Monday, November 23, 2026, Ho Chi Minh City, Vietnam.">
  <meta itemprop="image" content="https://minhnntrademkt.github.io/vietnam-semiconductor-summit-2026/images/og-banner.jpg?v=20260914_1315">

  <!-- Open Graph / Facebook / LinkedIn / Zalo -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://minhnntrademkt.github.io/vietnam-semiconductor-summit-2026/">
  <meta property="og:site_name" content="Vietnam Semiconductor Summit 2026">
  <meta property="og:locale" content="en_US">
  <meta property="og:title" content="Vietnam Semiconductor Summit 2026 | Marvell Technology">
  <meta name="og:title" content="Vietnam Semiconductor Summit 2026 | Marvell Technology">
  <meta property="og:description" content="Accelerating Vietnam's Semiconductor Revolution. Official Inaugural Congress uniting Government leadership, global chipmakers, and academic scholars. Monday, November 23, 2026, Ho Chi Minh City, Vietnam.">
  <meta name="og:description" content="Accelerating Vietnam's Semiconductor Revolution. Official Inaugural Congress uniting Government leadership, global chipmakers, and academic scholars. Monday, November 23, 2026, Ho Chi Minh City, Vietnam.">
  <meta property="og:image" content="https://minhnntrademkt.github.io/vietnam-semiconductor-summit-2026/images/og-banner.jpg?v=20260914_1315">
  <meta property="og:image:url" content="https://minhnntrademkt.github.io/vietnam-semiconductor-summit-2026/images/og-banner.jpg?v=20260914_1315">
  <meta property="og:image:secure_url" content="https://minhnntrademkt.github.io/vietnam-semiconductor-summit-2026/images/og-banner.jpg?v=20260914_1315">
  <meta name="og:image" content="https://minhnntrademkt.github.io/vietnam-semiconductor-summit-2026/images/og-banner.jpg?v=20260914_1315">
  <meta property="og:image:type" content="image/jpeg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="Vietnam Semiconductor Summit 2026 Official Banner">
  <link rel="image_src" href="https://minhnntrademkt.github.io/vietnam-semiconductor-summit-2026/images/og-banner.jpg?v=20260914_1315">

  <!-- Twitter / X Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Vietnam Semiconductor Summit 2026 | Marvell Technology">
  <meta name="twitter:description" content="Accelerating Vietnam's Semiconductor Revolution. Official Inaugural Congress uniting Government leadership, global chipmakers, and academic scholars. Monday, November 23, 2026, Ho Chi Minh City, Vietnam.">
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
              teal: '#00c7b1',
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
  <link rel="icon" type="image/svg+xml" href="favicon.svg">
  <link rel="alternate icon" href="favicon.svg">
  
  <!-- Marvell Custom Design Tokens -->
  <link rel="stylesheet" href="styles.css?v=20261016_2153">
</head>
<body class="bg-white text-slate-900 antialiased selection:bg-[#0072ce] selection:text-white">

  <!-- Top Scroll Reading Progress Bar -->
  <div id="scroll-progress-bar"></div>

  <!-- =========================================================================
       1. TOP BAR & NAVIGATION (STICKY HEADER - MARVELL CRISP WHITE)
       ========================================================================= -->
  <header id="main-header" class="sticky top-0 z-50 bg-white/95 backdrop-blur-md border-b border-slate-200 shadow-sm transition-transform duration-300 ease-in-out">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-20 sm:h-24 flex items-center justify-between gap-3 lg:gap-6 xl:gap-8">
      
      <!-- Brand Logo & Summit Title -->
      <a href="#" class="summit-brand-lockup flex items-center gap-2 sm:gap-4 min-w-0 group" aria-label="Vietnam Semiconductor Summit 2026 home">
        <div class="flex items-center shrink-0">
          <!-- Marvell Brand Mark Official Vector -->
          {marvell_logo_header}
        </div>
        <div class="h-7 sm:h-9 w-px bg-slate-300 shrink-0"></div>
        <div class="summit-brand-name font-extrabold text-slate-900 uppercase leading-snug">
          <span class="block">Vietnam Semiconductor</span>
          <span class="block">Summit</span>
        </div>
      </a>

      <!-- Desktop Nav Links (Zero Text-Wrap Guarantee & Precision Proportions) -->
      <nav class="hidden xl:flex items-center gap-3.5 xl:gap-6 2xl:gap-8 text-xs lg:text-[13px] xl:text-[15px] font-bold text-slate-800 shrink-0 whitespace-nowrap">
        <a href="#about" class="hover:text-[#0072ce] transition-colors whitespace-nowrap py-1">About</a>
        <a href="#speakers" class="hover:text-[#0072ce] transition-colors whitespace-nowrap py-1">Speakers</a>
        <a href="#panel" class="hover:text-[#0072ce] transition-colors whitespace-nowrap py-1">Strategic Panel</a>
        <a href="#agenda" class="hover:text-[#0072ce] transition-colors whitespace-nowrap py-1">Agenda</a>
        <a href="#partners" class="hover:text-[#0072ce] transition-colors whitespace-nowrap py-1">Partners</a>
        <a href="#faq" class="hover:text-[#0072ce] transition-colors whitespace-nowrap py-1">FAQ</a>
      </nav>

      <!-- CTA Register Button (Marvell Black Kinetic Button with Soft Radius) -->
      <div class="hidden sm:flex items-center shrink-0">
        <a href="#register" class="mrvll-btn-black open-rsvp-modal-btn text-xs xl:text-sm py-2.5 px-4 xl:py-3 xl:px-6 whitespace-nowrap">
          <span>Register Now</span>
          <svg class="btn-arrow w-3.5 h-3.5 xl:w-4 xl:h-4 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
        </a>
      </div>

      <!-- Mobile Hamburger Button -->
      <button id="mobile-menu-btn" class="xl:hidden p-2 text-slate-800 hover:text-black shrink-0">
        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16m-7 6h7"/></svg>
      </button>
    </div>
  </header>

  <!-- Mobile Drawer Menu -->
  <div id="mobile-nav-menu" class="fixed inset-0 z-50 bg-white/98 backdrop-blur-lg hidden flex-col p-6 xl:hidden border-b border-slate-200">
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
        <span>Register Now</span>
        <svg class="btn-arrow w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
      </a>
    </div>
  </div>

  <!-- =========================================================================
       2. HERO SECTION (HIGH-CONTRAST PURE BLACK TECH SILICON GLOW)
       ========================================================================= -->
  <section id="hero" class="relative bg-[#212322] text-white pt-24 pb-20 lg:pt-32 lg:pb-28 overflow-hidden border-b border-slate-800">
    <!-- Original chip image, composed to the right of the reading area. -->
    <div class="hero-chip-background pointer-events-none" aria-hidden="true"></div>
    <div class="hero-background-fade absolute inset-0 pointer-events-none" aria-hidden="true"></div>
    
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10 text-center">
      <div class="hero-copy">
      
      <!-- Top Host Badge -->
      <p class="brand-eyebrow text-sm sm:text-base font-bold text-white tracking-widest uppercase mb-6">
        2026 Inaugural Edition
      </p>

      <!-- Main Headline -->
      <h1 class="text-4xl sm:text-5xl lg:text-6xl font-extrabold tracking-tight text-white max-w-5xl mx-auto leading-tight sm:leading-none">
        Vietnam Semiconductor Summit 2026
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
          <div class="w-11 h-11 rounded-lg bg-cyan-600/15 border border-cyan-500/30 flex items-center justify-center text-[#00b5e2] shrink-0">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"/></svg>
          </div>
          <div>
            <span class="block text-[11px] text-slate-400 uppercase tracking-wider font-semibold">Venue</span>
            <span class="text-sm font-bold text-white">Ho Chi Minh City</span>
            <span class="text-[10px] text-slate-400 block">Grand Ballroom & Tech Tracks</span>
          </div>
        </div>

        <div class="p-5 rounded-xl bg-[#101726]/80 border border-slate-800/80 flex items-center gap-3.5 backdrop-blur-md shadow-md">
          <div class="w-11 h-11 rounded-lg bg-teal-600/15 border border-teal-500/30 flex items-center justify-center text-teal-400 shrink-0">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 5v2m0 4v2m0 4v2M5 5a2 2 0 00-2 2v3a2 2 0 110 4v3a2 2 0 002 2h14a2 2 0 002-2v-3a2 2 0 110-4V7a2 2 0 00-2-2H5z"/></svg>
          </div>
          <div>
            <span class="block text-[11px] text-slate-400 uppercase tracking-wider font-semibold">Registration</span>
            <span class="text-sm font-bold text-teal-400">100% Free RSVP</span>
            <span class="text-[10px] text-slate-400 block">Limited Capacity &bull; Vetted</span>
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
      <div class="hero-actions mt-10 flex flex-col sm:flex-row items-center justify-center gap-4">
        <a href="#register" class="mrvll-btn-white w-full sm:w-auto justify-center text-sm py-4 px-8 open-rsvp-modal-btn">
          <span>Register Now</span>
          <svg class="btn-arrow w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
        </a>
      </div>

      </div>
    </div>
  </section>

  <!-- =========================================================================
       3. METRICS / STATS BAR (CRISP WHITE CORPORATE CLEAN)
       ========================================================================= -->
  <section id="metrics" class="bg-white border-b border-slate-200 py-14">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-2 md:grid-cols-4 gap-8 text-center divide-y md:divide-y-0 md:divide-x divide-slate-200">
        <div class="pt-4 md:pt-0">
          <span class="block text-4xl sm:text-5xl font-extrabold text-[#0072ce] tracking-tight">600+</span>
          <span class="text-xs sm:text-sm font-bold text-slate-800 uppercase tracking-wider mt-2 block">Marvell Silicon Engineers</span>
          <p class="text-xs text-slate-500 mt-1">Specialized IC Design & R&D Talent in Vietnam</p>
        </div>
        <div class="pt-4 md:pt-0">
          <span class="block text-4xl sm:text-5xl font-extrabold text-[#0072ce] tracking-tight">50,000</span>
          <span class="text-xs sm:text-sm font-bold text-slate-800 uppercase tracking-wider mt-2 block">National Target Engineers by 2030</span>
          <p class="text-xs text-slate-500 mt-1">Vietnam Semiconductor Strategy (Decision 1017/QĐ-TTg)</p>
        </div>
        <div class="pt-4 md:pt-0">
          <span class="block text-4xl sm:text-5xl font-extrabold text-[#0072ce] tracking-tight">3</span>
          <span class="text-xs sm:text-sm font-bold text-slate-800 uppercase tracking-wider mt-2 block">Premier R&D Centers</span>
          <p class="text-xs text-slate-500 mt-1">ET6 (HQ) & UOA in HCMC, SP2 in Da Nang</p>
        </div>
        <div class="pt-4 md:pt-0">
          <span class="block text-4xl sm:text-5xl font-extrabold text-[#0072ce] tracking-tight">#3</span>
          <span class="text-xs sm:text-sm font-bold text-slate-800 uppercase tracking-wider mt-2 block">Global Marvell R&D Hub</span>
          <p class="text-xs text-slate-500 mt-1">3rd Largest Worldwide, Following USA & India</p>
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
      <div id="pillars" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        
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
            <div class="w-12 h-12 rounded-lg bg-teal-50 border border-teal-200 flex items-center justify-center text-[#00c7b1] mb-5">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 3v2m6-2v2M9 19v2m6-2v2M5 9H3m2 6H3m18-6h-2m2 6h-2M7 19h10a2 2 0 002-2V7a2 2 0 00-2-2H7a2 2 0 00-2 2v10a2 2 0 002 2zM9 9h6v6H9V9z"/></svg>
            </div>
            <span class="text-[10px] font-bold tracking-widest text-[#00c7b1] uppercase">PILLAR 02</span>
            <h3 class="text-lg font-bold text-slate-900 mt-1 mb-2.5">Advanced Packaging & CPO</h3>
            <p class="text-xs text-slate-600 leading-relaxed">Pioneering Co-Packaged Optics (CPO) architectures, 2.5D/3D Heterogeneous Integration, and high-speed optical interconnects for next-gen silicon.</p>
          </div>
        </div>

        <div class="mrvll-light-card p-7 rounded-xl bg-white flex flex-col justify-between">
          <div>
            <div class="w-12 h-12 rounded-lg bg-cyan-50 border border-cyan-200 flex items-center justify-center text-[#00b5e2] mb-5">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/></svg>
            </div>
            <span class="text-[10px] font-bold tracking-widest text-cyan-600 uppercase">PILLAR 03</span>
            <h3 class="text-lg font-bold text-slate-900 mt-1 mb-2.5">AI Silicon & Cloud Infrastructure</h3>
            <p class="text-xs text-slate-600 leading-relaxed">Enterprise-grade custom computing architectures, high-density server processors, and ultra-low latency optical fabrics for AI cloud data centers.</p>
          </div>
        </div>

        <div class="mrvll-light-card p-7 rounded-xl bg-white flex flex-col justify-between">
          <div>
            <div class="w-12 h-12 rounded-lg bg-teal-50 border border-teal-200 flex items-center justify-center text-teal-600 mb-5">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l9-5-9-5-9 5 9 5z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0012 20.055a11.952 11.952 0 00-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14z"/></svg>
            </div>
            <span class="text-[10px] font-bold tracking-widest text-teal-600 uppercase">PILLAR 04</span>
            <h3 class="text-lg font-bold text-slate-900 mt-1 mb-2.5">Talent & Academic R&D</h3>
            <p class="text-xs text-slate-600 leading-relaxed">Supporting Vietnam's National Strategy to develop 50,000 semiconductor engineers by 2030 (Decision 1017/QĐ-TTg) through joint university R&D laboratories, EDA software sponsorships, and fellowship programs.</p>
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
      
      <div class="brand-host-about bg-gradient-to-br from-slate-900 via-[#0c1322] to-[#0a1b38] rounded-3xl p-8 sm:p-12 lg:p-16 border border-slate-800 shadow-2xl relative overflow-hidden text-left">
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
            </div>
          </div>

          <!-- 3 Feature Pillars of Marvell Vietnam -->
          <div class="grid grid-cols-1 md:grid-cols-3 gap-6 pt-10">
            
            <div class="p-6 rounded-2xl bg-[#101726]/80 border border-slate-800 backdrop-blur-sm">
              <div class="w-10 h-10 rounded-xl bg-blue-600/20 border border-blue-500/40 flex items-center justify-center text-[#00b5e2] mb-4">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"/></svg>
              </div>
              <h3 class="text-base font-bold text-white mb-2">Triple R&D Centers of Excellence</h3>
              <p class="text-xs text-slate-400 leading-relaxed">
                Operating across three premier facilities in <strong>Ho Chi Minh City</strong> (ET6 & UOA) and <strong>Da Nang</strong> (SP2), Marvell Vietnam has emerged as Marvell's <strong>3rd largest R&D center globally</strong>, just after the United States and India.
              </p>
            </div>

            <div class="p-6 rounded-2xl bg-[#101726]/80 border border-slate-800 backdrop-blur-sm">
              <div class="w-10 h-10 rounded-xl bg-cyan-600/20 border border-cyan-500/40 flex items-center justify-center text-[#00b5e2] mb-4">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 3v2m6-2v2M9 19v2m6-2v2M5 9H3m2 6H3m18-6h-2m2 6h-2M7 19h10a2 2 0 002-2V7a2 2 0 00-2-2H7a2 2 0 00-2 2v10a2 2 0 002 2zM9 9h6v6H9V9z"/></svg>
              </div>
              <h3 class="text-base font-bold text-white mb-2">Pioneering CPO & Optical Silicon</h3>
              <p class="text-xs text-slate-400 leading-relaxed">
                Vietnamese engineering teams contribute directly to Marvell's industry-leading <strong>Near Packaged Optics (NPO), Co-Packaged Optics (CPO)</strong>, PAM4 Optical DSPs, Active Electrical Cable (AEC), uEmitter (uLED, uVCSEL), and custom accelerated compute silicon for hyperscale AI data centers.
              </p>
            </div>

            <div class="p-6 rounded-2xl bg-[#101726]/80 border border-slate-800 backdrop-blur-sm">
              <div class="w-10 h-10 rounded-xl bg-cyan-600/20 border border-cyan-500/40 flex items-center justify-center text-[#00b5e2] mb-4">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"/></svg>
              </div>
              <h3 class="text-base font-bold text-white mb-2">600+ Engineers & Academic Alliances</h3>
              <p class="text-xs text-slate-400 leading-relaxed">
                Total headcount of over 600+ specialized IC design and semiconductor engineers expanding rapidly, supported by comprehensive academia partnerships with various universities in Ho Chi Minh City, Da Nang and Hanoi including internship recruitment, scholarship program, training curriculum and lab development.
              </p>
            </div>

          </div>

          <!-- Bottom Action Links -->
          <div class="mt-8 pt-6 border-t border-slate-800/80 flex flex-wrap items-center justify-between gap-4 text-xs">
            <span class="text-slate-400">
              Host Headquarters: <strong>Marvell Technology Vietnam, LLC</strong> &bull; Etown6 Tower (HQ) & UOA Tower, HCMC &bull; SP2, Da Nang
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

      <!-- TIER 1: GUESTS OF HONOR & GOVERNMENT LEADERS -->
      <div class="speaker-tier-government mb-14">
        <h3 class="text-xs font-bold uppercase tracking-widest text-slate-400 mb-6 flex items-center gap-3">
          <span>GUESTS OF HONOR & GOVERNMENT LEADERS</span>
          <div class="flex-1 h-px bg-slate-800"></div>
        </h3>

        <div class="grid grid-cols-2 gap-3 sm:gap-4 md:gap-5 max-w-[556px] mx-auto">
          
          <!-- Nguyen Van Duoc -->
          <div class="mrvll-dark-card speaker-card cursor-pointer group p-3 sm:p-3.5 rounded-xl flex flex-col justify-between border-t-2 border-t-blue-500 bg-[#101726] hover:border-blue-400/80 transition-all duration-300" data-speaker-id="nguyen-van-duoc">
            <div>
              <div class="relative w-full aspect-square rounded-lg sm:rounded-xl overflow-hidden border border-blue-500/40 mb-2.5 sm:mb-3 shadow-[0_0_20px_rgba(0,114,206,0.25)] group-hover:border-blue-400 transition-all bg-blue-950/80">
                <img src="images/speakers/nguyen-van-duoc.jpg" alt="Mr. Nguyen Van Duoc" class="w-full h-full object-cover object-top group-hover:scale-105 transition-transform duration-300" onerror="this.style.display='none'; this.nextElementSibling.classList.remove('hidden');">
                <div class="hidden w-full h-full flex items-center justify-center text-3xl sm:text-4xl font-bold text-blue-400">
                  NVD
                </div>
                <div class="absolute bottom-0 inset-x-0 h-8 sm:h-10 bg-gradient-to-t from-[#101726]/80 to-transparent pointer-events-none"></div>
              </div>
              <h4 class="text-[13px] sm:text-[14px] font-bold text-white mt-1 group-hover:text-blue-400 transition-colors leading-snug line-clamp-2 min-h-[34px] sm:min-h-[38px] flex items-center">Mr. Nguyen Van Duoc</h4>
              <p class="text-[11px] sm:text-xs font-semibold text-blue-400 mt-0.5 truncate">Chairman</p>
              <p class="text-[10px] sm:text-[11px] text-slate-400 mt-0.5 font-medium line-clamp-1">Ho Chi Minh City People's Committee</p>
            </div>
            <div class="mt-2.5 pt-2 border-t border-slate-800/80 text-[10px] sm:text-[10.5px] text-slate-400">
              <div class="text-[10px] sm:text-[10.5px] text-blue-400 flex items-center gap-1.5 font-semibold group-hover:underline">
                <span>View Bio & Abstract</span>
                <svg class="w-3.5 h-3.5 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
              </div>
            </div>
          </div>

          <!-- Melissa A. Brown -->
          <div class="mrvll-dark-card speaker-card cursor-pointer group p-3 sm:p-3.5 rounded-xl flex flex-col justify-between border-t-2 border-t-blue-500 bg-[#101726] hover:border-blue-400/80 transition-all duration-300" data-speaker-id="melissa-brown">
            <div>
              <div class="relative w-full aspect-square rounded-lg sm:rounded-xl overflow-hidden border border-blue-500/40 mb-2.5 sm:mb-3 shadow-[0_0_20px_rgba(0,114,206,0.25)] group-hover:border-blue-400 transition-all bg-blue-950/80">
                <img src="images/speakers/melissa-brown.jpg" alt="Ms. Melissa A. Brown" class="w-full h-full object-cover object-top group-hover:scale-105 transition-transform duration-300" onerror="this.style.display='none'; this.nextElementSibling.classList.remove('hidden');">
                <div class="hidden w-full h-full flex items-center justify-center text-3xl sm:text-4xl font-bold text-blue-400">
                  MB
                </div>
                <div class="absolute bottom-0 inset-x-0 h-8 sm:h-10 bg-gradient-to-t from-[#101726]/80 to-transparent pointer-events-none"></div>
              </div>
              <h4 class="text-[13px] sm:text-[14px] font-bold text-white mt-1 group-hover:text-blue-400 transition-colors leading-snug line-clamp-2 min-h-[34px] sm:min-h-[38px] flex items-center">Ms. Melissa A. Brown</h4>
              <p class="text-[11px] sm:text-xs font-semibold text-blue-400 mt-0.5 truncate">U.S. Consul General</p>
              <p class="text-[10px] sm:text-[11px] text-slate-400 mt-0.5 font-medium line-clamp-1">U.S. Consulate General in Ho Chi Minh City</p>
            </div>
            <div class="mt-2.5 pt-2 border-t border-slate-800/80 text-[10px] sm:text-[10.5px] text-slate-400">
              <div class="text-[10px] sm:text-[10.5px] text-blue-400 flex items-center gap-1.5 font-semibold group-hover:underline">
                <span>View Bio & Abstract</span>
                <svg class="w-3.5 h-3.5 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
              </div>
            </div>
          </div>

        </div>
      </div>

      <!-- TIER 2: STRATEGIC KEYNOTES -->
      <div class="speaker-tier-primary mb-14">
        <h3 class="text-xs font-bold uppercase tracking-widest text-slate-400 mb-6 flex items-center gap-3">
          <span>STRATEGIC KEYNOTES</span>
          <div class="flex-1 h-px bg-slate-800"></div>
        </h3>

        <div class="grid grid-cols-2 sm:grid-cols-3 gap-3 sm:gap-4 md:gap-5 max-w-[844px] mx-auto">
          
          <!-- 1. Mr. Noam Mizrahi -->
          <div class="mrvll-dark-card speaker-card cursor-pointer group p-3 sm:p-3.5 rounded-xl flex flex-col justify-between border-t-2 border-t-[#00b5e2] bg-[#101726] hover:border-cyan-400/80 transition-all duration-300" data-speaker-id="noam-mizrahi">
            <div>
              <div class="relative w-full aspect-square rounded-lg sm:rounded-xl overflow-hidden border border-cyan-500/40 mb-2.5 sm:mb-3 shadow-[0_0_20px_rgba(0,181,226,0.25)] group-hover:border-cyan-400 transition-all bg-cyan-950/80">
                <img src="images/speakers/noam-mizrahi.jpg?v=20261013_1200" alt="Noam Mizrahi" class="w-full h-full object-cover object-top group-hover:scale-105 transition-transform duration-300" onerror="this.style.display='none'; this.nextElementSibling.classList.remove('hidden');">
                <div class="hidden w-full h-full flex items-center justify-center text-3xl sm:text-4xl font-bold text-[#00b5e2]">
                  NM
                </div>
                <div class="absolute bottom-0 inset-x-0 h-8 sm:h-10 bg-gradient-to-t from-[#101726]/80 to-transparent pointer-events-none"></div>
              </div>
              <h4 class="text-[13px] sm:text-[14px] font-bold text-white mt-1 group-hover:text-[#00b5e2] transition-colors leading-snug line-clamp-2 min-h-[34px] sm:min-h-[38px] flex items-center">Mr. Noam Mizrahi</h4>
              <p class="text-[11px] sm:text-xs font-semibold text-[#00b5e2] mt-0.5 truncate">EVP & Corporate CTO</p>
              <p class="text-[10px] sm:text-[11px] text-slate-400 mt-0.5 font-medium line-clamp-1">Marvell Technology, Inc.</p>
            </div>
            <div class="mt-2.5 pt-2 border-t border-slate-800/80 text-[10px] sm:text-[10.5px] text-slate-400">
              Host: <em class="line-clamp-2">National Strategic Semiconductor Architecture</em>
              <div class="mt-2 text-[10px] sm:text-[10.5px] text-[#00b5e2] flex items-center gap-1.5 font-semibold group-hover:underline">
                <span>View Bio & Abstract</span>
                <svg class="w-3.5 h-3.5 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
              </div>
            </div>
          </div>

          <!-- 2. Ms. Bich-Yen Nguyen -->
          <div class="mrvll-dark-card speaker-card cursor-pointer group p-3 sm:p-3.5 rounded-xl flex flex-col justify-between border-t-2 border-t-[#00b5e2] bg-[#101726] hover:border-cyan-400/80 transition-all duration-300" data-speaker-id="nguyen-bich-yen">
            <div>
              <div class="relative w-full aspect-square rounded-lg sm:rounded-xl overflow-hidden border border-cyan-500/40 mb-2.5 sm:mb-3 shadow-[0_0_20px_rgba(0,181,226,0.25)] group-hover:border-cyan-400 transition-all bg-cyan-950/80">
                <img src="images/speakers/bich-yen-nguyen.jpg?v=20261013_1200" alt="Ms. Bich-Yen Nguyen" class="w-full h-full object-cover object-top group-hover:scale-105 transition-transform duration-300" onerror="this.style.display='none'; this.nextElementSibling.classList.remove('hidden');">
                <div class="hidden w-full h-full flex items-center justify-center text-3xl sm:text-4xl font-bold text-[#00b5e2]">
                  BYN
                </div>
                <div class="absolute bottom-0 inset-x-0 h-8 sm:h-10 bg-gradient-to-t from-[#101726]/80 to-transparent pointer-events-none"></div>
              </div>
              <h4 class="text-[13px] sm:text-[14px] font-bold text-white mt-1 group-hover:text-[#00b5e2] transition-colors leading-snug line-clamp-2 min-h-[34px] sm:min-h-[38px] flex items-center">Ms. Bich-Yen Nguyen</h4>
              <p class="text-[11px] sm:text-xs font-semibold text-[#00b5e2] mt-0.5 truncate">Senior Fellow & Co-Founder</p>
              <p class="text-[10px] sm:text-[11px] text-slate-400 mt-0.5 font-medium line-clamp-1">VSAP-LAB / Soitec (IEEE Fellow)</p>
            </div>
            <div class="mt-2.5 pt-2 border-t border-slate-800/80 text-[10px] sm:text-[10.5px] text-slate-400">
              Keynote: <em class="line-clamp-2">Advanced Packaging & Co-Packaged Optics</em>
              <div class="mt-2 text-[10px] sm:text-[10.5px] text-[#00b5e2] flex items-center gap-1.5 font-semibold group-hover:underline">
                <span>View Bio & Abstract</span>
                <svg class="w-3.5 h-3.5 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
              </div>
            </div>
          </div>

          <!-- 3. Dr. Quang-Dam Le -->
          <div class="mrvll-dark-card speaker-card cursor-pointer group p-3 sm:p-3.5 rounded-xl flex flex-col justify-between border-t-2 border-t-[#00b5e2] bg-[#101726] hover:border-cyan-400/80 transition-all duration-300 col-span-2 sm:col-span-1 w-full max-w-[calc(50%-6px)] sm:max-w-none mx-auto" data-speaker-id="le-quang-dam">
            <div>
              <div class="relative w-full aspect-square rounded-lg sm:rounded-xl overflow-hidden border border-cyan-500/40 mb-2.5 sm:mb-3 shadow-[0_0_20px_rgba(0,181,226,0.25)] group-hover:border-cyan-400 transition-all bg-cyan-950/80">
                <img src="images/speakers/le-quang-dam.jpg?v=20260922_0900" alt="Dr. Quang-Dam Le" class="w-full h-full object-cover object-top group-hover:scale-105 transition-transform duration-300" onerror="this.style.display='none'; this.nextElementSibling.classList.remove('hidden');">
                <div class="hidden w-full h-full flex items-center justify-center text-3xl sm:text-4xl font-bold text-[#00b5e2]">
                  QD
                </div>
                <div class="absolute bottom-0 inset-x-0 h-8 sm:h-10 bg-gradient-to-t from-[#101726]/80 to-transparent pointer-events-none"></div>
              </div>
              <h4 class="text-[13px] sm:text-[14px] font-bold text-white mt-1 group-hover:text-[#00b5e2] transition-colors leading-snug line-clamp-2 min-h-[34px] sm:min-h-[38px] flex items-center">Dr. Quang-Dam Le</h4>
              <p class="text-[11px] sm:text-xs font-semibold text-[#00b5e2] mt-0.5 truncate">Vice President & General Director</p>
              <p class="text-[10px] sm:text-[11px] text-slate-400 mt-0.5 font-medium line-clamp-1">Marvell Technology Vietnam, LLC</p>
            </div>
            <div class="mt-2.5 pt-2 border-t border-slate-800/80 text-[10px] sm:text-[10.5px] text-slate-400">
              Keynote: <em class="line-clamp-2">Building What's Next: Vietnam's Semiconductor Journey</em>
              <div class="mt-2 text-[10px] sm:text-[10.5px] text-[#00b5e2] flex items-center gap-1.5 font-semibold group-hover:underline">
                <span>View Bio & Abstract</span>
                <svg class="w-3.5 h-3.5 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
              </div>
            </div>
          </div>

        </div>
      </div>

      <!-- TIER 2: INDUSTRY & ACADEMIA LEADERS -->
      <div class="speaker-tier-industry">
        <h3 class="text-xs font-bold uppercase tracking-widest text-slate-400 mb-6 flex items-center gap-3">
          <span>CORPORATE ARCHITECTS & ACADEMIC LUMINARIES</span>
          <div class="flex-1 h-px bg-slate-800"></div>
        </h3>

        <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-3 sm:gap-3.5">
          
          <!-- 1. Prof. Dr. Mai Nguyen -->
          <div class="mrvll-dark-card speaker-card cursor-pointer group p-3 sm:p-3.5 rounded-xl flex flex-col justify-between border-t-2 border-t-[#00b5e2] bg-[#101726] hover:border-cyan-400/80 transition-all duration-300" data-speaker-id="nguyen-thi-thanh-mai">
            <div>
              <div class="relative w-full aspect-square rounded-lg sm:rounded-xl overflow-hidden border border-cyan-500/40 mb-2.5 sm:mb-3 shadow-[0_0_20px_rgba(0,181,226,0.25)] group-hover:border-cyan-400 transition-all bg-cyan-950/80">
                <img src="images/speakers/nguyen-thi-thanh-mai.jpg?v=20261013_1200" alt="Prof. Dr. Mai Nguyen" class="w-full h-full object-cover object-top group-hover:scale-105 transition-transform duration-300" onerror="this.style.display='none'; this.nextElementSibling.classList.remove('hidden');">
                <div class="hidden w-full h-full flex items-center justify-center text-xl font-bold text-teal-400">NTM</div>
                <div class="absolute bottom-0 inset-x-0 h-8 sm:h-10 bg-gradient-to-t from-[#101726]/80 to-transparent pointer-events-none"></div>
              </div>
              <h4 class="speaker-name text-[13px] sm:text-[14px] font-bold text-white mt-1 transition-colors leading-snug block">Prof. Dr. Mai Nguyen</h4>
              <p class="speaker-role text-[10.5px] text-slate-400 mt-0.5 leading-tight">President</p>
              <span class="speaker-organization text-[11px] text-teal-400 font-semibold block mt-0.5 truncate">Viet Nam National University Ho Chi Minh City (VNU-HCM)</span>
            </div>
            <div class="mt-2.5 pt-2 border-t border-slate-800/80 flex items-center gap-1.5 text-[10px] sm:text-[10.5px] text-white font-semibold group-hover:underline">
              <span>View Bio</span>
              <svg class="w-3.5 h-3.5 group-hover:translate-x-1 transition-all" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
            </div>
          </div>

          <!-- 2. Dr. Phung Nguyen -->
          <div class="mrvll-dark-card speaker-card cursor-pointer group p-3 sm:p-3.5 rounded-xl flex flex-col justify-between border-t-2 border-t-[#00b5e2] bg-[#101726] hover:border-cyan-400/80 transition-all duration-300" data-speaker-id="nguyen-ky-phung">
            <div>
              <div class="relative w-full aspect-square rounded-lg sm:rounded-xl overflow-hidden border border-cyan-500/40 mb-2.5 sm:mb-3 shadow-[0_0_20px_rgba(0,181,226,0.25)] group-hover:border-cyan-400 transition-all bg-cyan-950/80">
                <img src="images/speakers/nguyen-ky-phung.jpg?v=20261013_1200" alt="Dr. Phung Nguyen" class="w-full h-full object-cover object-top group-hover:scale-105 transition-transform duration-300" onerror="this.style.display='none'; this.nextElementSibling.classList.remove('hidden');">
                <div class="hidden w-full h-full flex items-center justify-center text-xl font-bold text-[#00b5e2]">NKP</div>
                <div class="absolute bottom-0 inset-x-0 h-8 sm:h-10 bg-gradient-to-t from-[#101726]/80 to-transparent pointer-events-none"></div>
              </div>
              <h4 class="speaker-name text-[13px] sm:text-[14px] font-bold text-white mt-1 transition-colors leading-snug block">Dr. Phung Nguyen</h4>
              <p class="speaker-role text-[10.5px] text-slate-400 mt-0.5 leading-tight">Chairman</p>
              <span class="speaker-organization text-[11px] text-[#00b5e2] font-semibold block mt-0.5 truncate">Saigon Hi-Tech Park (SHTP)</span>
            </div>
            <div class="mt-2.5 pt-2 border-t border-slate-800/80 flex items-center gap-1.5 text-[10px] sm:text-[10.5px] text-white font-semibold group-hover:underline">
              <span>View Bio</span>
              <svg class="w-3.5 h-3.5 group-hover:translate-x-1 transition-all" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
            </div>
          </div>

          <!-- 3. Dr. Thuat Nguyen -->
          <div class="mrvll-dark-card speaker-card cursor-pointer group p-3 sm:p-3.5 rounded-xl flex flex-col justify-between border-t-2 border-t-[#00b5e2] bg-[#101726] hover:border-cyan-400/80 transition-all duration-300" data-speaker-id="thuat-nguyen">
            <div>
              <div class="relative w-full aspect-square rounded-lg sm:rounded-xl overflow-hidden border border-cyan-500/40 mb-2.5 sm:mb-3 shadow-[0_0_20px_rgba(0,181,226,0.25)] group-hover:border-cyan-400 transition-all bg-cyan-950/80">
                <img src="images/speakers/thuat-nguyen.jpg?v=20261013_1200" alt="Dr. Thuat Nguyen" class="w-full h-full object-cover object-top group-hover:scale-105 transition-transform duration-300" onerror="this.style.display='none'; this.nextElementSibling.classList.remove('hidden');">
                <div class="hidden w-full h-full flex items-center justify-center text-xl font-bold text-teal-400">TN</div>
                <div class="absolute bottom-0 inset-x-0 h-8 sm:h-10 bg-gradient-to-t from-[#101726]/80 to-transparent pointer-events-none"></div>
              </div>
              <h4 class="speaker-name text-[13px] sm:text-[14px] font-bold text-white mt-1 transition-colors leading-snug block">Dr. Thuat Nguyen</h4>
              <p class="speaker-role text-[10.5px] text-slate-400 mt-0.5 leading-tight">Director</p>
              <span class="speaker-organization text-[11px] text-teal-400 font-semibold block mt-0.5 line-clamp-2 leading-tight" title="Semiconductors and Advanced Materials Institute at the Strategic Technology Institute, Vietnam National University">Semiconductors and Advanced Materials Institute at the Strategic Technology Institute, Vietnam National University</span>
            </div>
            <div class="mt-2.5 pt-2 border-t border-slate-800/80 flex items-center gap-1.5 text-[10px] sm:text-[10.5px] text-white font-semibold group-hover:underline">
              <span>View Bio</span>
              <svg class="w-3.5 h-3.5 group-hover:translate-x-1 transition-all" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
            </div>
          </div>

          <!-- 4. Mr. Khanh Nguyen -->
          <div class="mrvll-dark-card speaker-card cursor-pointer group p-3 sm:p-3.5 rounded-xl flex flex-col justify-between border-t-2 border-t-[#00b5e2] bg-[#101726] hover:border-cyan-400/80 transition-all duration-300" data-speaker-id="nguyen-quang-khanh">
            <div>
              <div class="relative w-full aspect-square rounded-lg sm:rounded-xl overflow-hidden border border-cyan-500/40 mb-2.5 sm:mb-3 shadow-[0_0_20px_rgba(0,181,226,0.25)] group-hover:border-cyan-400 transition-all bg-cyan-950/80">
                <img src="images/speakers/nguyen-quang-khanh.jpg?v=20261013_1200" alt="Mr. Khanh Nguyen" class="w-full h-full object-cover object-top group-hover:scale-105 transition-transform duration-300" onerror="this.style.display='none'; this.nextElementSibling.classList.remove('hidden');">
                <div class="hidden w-full h-full flex items-center justify-center text-xl font-bold text-[#00b5e2]">QK</div>
                <div class="absolute bottom-0 inset-x-0 h-8 sm:h-10 bg-gradient-to-t from-[#101726]/80 to-transparent pointer-events-none"></div>
              </div>
              <h4 class="speaker-name text-[13px] sm:text-[14px] font-bold text-white mt-1 transition-colors leading-snug block">Mr. Khanh Nguyen</h4>
              <p class="speaker-role text-[10.5px] text-slate-400 mt-0.5 leading-tight">General Factory Director</p>
              <span class="speaker-organization text-[11px] text-[#00b5e2] font-semibold block mt-0.5 truncate">Intel Products Vietnam (IPV)</span>
            </div>
            <div class="mt-2.5 pt-2 border-t border-slate-800/80 flex items-center gap-1.5 text-[10px] sm:text-[10.5px] text-white font-semibold group-hover:underline">
              <span>View Bio & Abstract</span>
              <svg class="w-3.5 h-3.5 group-hover:translate-x-1 transition-all" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
            </div>
          </div>

          <!-- 5. Mr. Lam Trinh -->
          <div class="mrvll-dark-card speaker-card cursor-pointer group p-3 sm:p-3.5 rounded-xl flex flex-col justify-between border-t-2 border-t-[#00b5e2] bg-[#101726] hover:border-cyan-400/80 transition-all duration-300" data-speaker-id="lam-trinh">
            <div>
              <div class="relative w-full aspect-square rounded-lg sm:rounded-xl overflow-hidden border border-cyan-500/40 mb-2.5 sm:mb-3 shadow-[0_0_20px_rgba(0,181,226,0.25)] group-hover:border-cyan-400 transition-all bg-cyan-950/80">
                <img src="images/speakers/lam-trinh.jpg?v=20261013_1200" alt="Mr. Lam Trinh" class="w-full h-full object-cover object-top group-hover:scale-105 transition-transform duration-300" onerror="this.style.display='none'; this.nextElementSibling.classList.remove('hidden');">
                <div class="hidden w-full h-full flex items-center justify-center text-xl font-bold text-[#00b5e2]">LT</div>
                <div class="absolute bottom-0 inset-x-0 h-8 sm:h-10 bg-gradient-to-t from-[#101726]/80 to-transparent pointer-events-none"></div>
              </div>
              <h4 class="speaker-name text-[13px] sm:text-[14px] font-bold text-white mt-1 transition-colors leading-snug block">Mr. Lam Trinh</h4>
              <p class="speaker-role text-[10.5px] text-slate-400 mt-0.5 leading-tight">Regional Sales Director, South Asia</p>
              <span class="speaker-organization text-[11px] text-[#00b5e2] font-semibold block mt-0.5 truncate">Synopsys Inc</span>
            </div>
            <div class="mt-2.5 pt-2 border-t border-slate-800/80 flex items-center gap-1.5 text-[10px] sm:text-[10.5px] text-white font-semibold group-hover:underline">
              <span>View Bio & Abstract</span>
              <svg class="w-3.5 h-3.5 group-hover:translate-x-1 transition-all" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
            </div>
          </div>

          <!-- 6. Assoc. Prof. Dr. Loan Pham-Nguyen -->
          <div class="mrvll-dark-card speaker-card cursor-pointer group p-3 sm:p-3.5 rounded-xl flex flex-col justify-between border-t-2 border-t-[#00b5e2] bg-[#101726] hover:border-cyan-400/80 transition-all duration-300" data-speaker-id="pham-nguyen-thanh-loan">
            <div>
              <div class="relative w-full aspect-square rounded-lg sm:rounded-xl overflow-hidden border border-cyan-500/40 mb-2.5 sm:mb-3 shadow-[0_0_20px_rgba(0,181,226,0.25)] group-hover:border-cyan-400 transition-all bg-cyan-950/80">
                <img src="images/speakers/pham-nguyen-thanh-loan.jpg?v=20261013_1200" alt="Assoc. Prof. Dr. Loan Pham-Nguyen" class="w-full h-full object-cover object-top group-hover:scale-105 transition-transform duration-300" onerror="this.style.display='none'; this.nextElementSibling.classList.remove('hidden');">
                <div class="hidden w-full h-full flex items-center justify-center text-xl font-bold text-teal-400">PTL</div>
                <div class="absolute bottom-0 inset-x-0 h-8 sm:h-10 bg-gradient-to-t from-[#101726]/80 to-transparent pointer-events-none"></div>
              </div>
              <h4 class="speaker-name text-[13px] sm:text-[14px] font-bold text-white mt-1 transition-colors leading-snug block">Assoc. Prof. Dr. Loan Pham-Nguyen</h4>
              <p class="speaker-role text-[10.5px] text-slate-400 mt-0.5 leading-tight">Head of IC Design & Embedded Systems Laboratory</p>
              <span class="speaker-organization text-[11px] text-teal-400 font-semibold block mt-0.5 truncate">Hanoi University of Science and Technology (HUST)</span>
            </div>
            <div class="mt-2.5 pt-2 border-t border-slate-800/80 flex items-center gap-1.5 text-[10px] sm:text-[10.5px] text-white font-semibold group-hover:underline">
              <span>View Bio & Abstract</span>
              <svg class="w-3.5 h-3.5 group-hover:translate-x-1 transition-all" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
            </div>
          </div>

          <!-- 7. Mr. Hai Hoang -->
          <div class="mrvll-dark-card speaker-card cursor-pointer group p-3 sm:p-3.5 rounded-xl flex flex-col justify-between border-t-2 border-t-[#00b5e2] bg-[#101726] hover:border-cyan-400/80 transition-all duration-300" data-speaker-id="hai-hoang">
            <div>
              <div class="relative w-full aspect-square rounded-lg sm:rounded-xl overflow-hidden border border-cyan-500/40 mb-2.5 sm:mb-3 shadow-[0_0_20px_rgba(0,181,226,0.25)] group-hover:border-cyan-400 transition-all bg-cyan-950/80">
                <img src="images/speakers/hai-hoang.jpg?v=20261013_1200" alt="Mr. Hai Hoang" class="w-full h-full object-cover object-top group-hover:scale-105 transition-transform duration-300" onerror="this.style.display='none'; this.nextElementSibling.classList.remove('hidden');">
                <div class="hidden w-full h-full flex items-center justify-center text-xl font-bold text-[#00b5e2]">HH</div>
                <div class="absolute bottom-0 inset-x-0 h-8 sm:h-10 bg-gradient-to-t from-[#101726]/80 to-transparent pointer-events-none"></div>
              </div>
              <h4 class="speaker-name text-[13px] sm:text-[14px] font-bold text-white mt-1 transition-colors leading-snug block">Mr. Hai Hoang</h4>
              <p class="speaker-role text-[10.5px] text-slate-400 mt-0.5 leading-tight">Staff Manager, Product Marketing</p>
              <span class="speaker-organization text-[11px] text-[#00b5e2] font-semibold block mt-0.5 truncate">Qualcomm Vietnam</span>
            </div>
            <div class="mt-2.5 pt-2 border-t border-slate-800/80 flex items-center gap-1.5 text-[10px] sm:text-[10.5px] text-white font-semibold group-hover:underline">
              <span>View Bio & Abstract</span>
              <svg class="w-3.5 h-3.5 group-hover:translate-x-1 transition-all" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
            </div>
          </div>

          <!-- 8. Mr. Khoa Tran -->
          <div class="mrvll-dark-card speaker-card cursor-pointer group p-3 sm:p-3.5 rounded-xl flex flex-col justify-between border-t-2 border-t-[#00b5e2] bg-[#101726] hover:border-cyan-400/80 transition-all duration-300" data-speaker-id="khoa-tran">
            <div>
              <div class="relative w-full aspect-square rounded-lg sm:rounded-xl overflow-hidden border border-cyan-500/40 mb-2.5 sm:mb-3 shadow-[0_0_20px_rgba(0,181,226,0.25)] group-hover:border-cyan-400 transition-all bg-cyan-950/80">
                <img src="images/speakers/khoa-tran.jpg?v=20261013_1200" alt="Mr. Khoa Tran" class="w-full h-full object-cover object-top group-hover:scale-105 transition-transform duration-300" onerror="this.style.display='none'; this.nextElementSibling.classList.remove('hidden');">
                <div class="hidden w-full h-full flex items-center justify-center text-xl font-bold text-[#00b5e2]">KT</div>
                <div class="absolute bottom-0 inset-x-0 h-8 sm:h-10 bg-gradient-to-t from-[#101726]/80 to-transparent pointer-events-none"></div>
              </div>
              <h4 class="speaker-name text-[13px] sm:text-[14px] font-bold text-white mt-1 transition-colors leading-snug block">Mr. Khoa Tran</h4>
              <p class="speaker-role text-[10.5px] text-slate-400 mt-0.5 leading-tight">General Director</p>
              <span class="speaker-organization text-[11px] text-[#00b5e2] font-semibold block mt-0.5 truncate">Renesas Electronics Vietnam</span>
            </div>
            <div class="mt-2.5 pt-2 border-t border-slate-800/80 flex items-center gap-1.5 text-[10px] sm:text-[10.5px] text-white font-semibold group-hover:underline">
              <span>View Bio & Abstract</span>
              <svg class="w-3.5 h-3.5 group-hover:translate-x-1 transition-all" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
            </div>
          </div>

          <!-- 9. Assoc. Prof. Trang Hoang, Ph.D. -->
          <div class="mrvll-dark-card speaker-card cursor-pointer group p-3 sm:p-3.5 rounded-xl flex flex-col justify-between border-t-2 border-t-[#00b5e2] bg-[#101726] hover:border-cyan-400/80 transition-all duration-300" data-speaker-id="hoang-trang">
            <div>
              <div class="relative w-full aspect-square rounded-lg sm:rounded-xl overflow-hidden border border-cyan-500/40 mb-2.5 sm:mb-3 shadow-[0_0_20px_rgba(0,181,226,0.25)] group-hover:border-cyan-400 transition-all bg-cyan-950/80">
                <img src="images/speakers/hoang-trang.jpg?v=20261013_1200" alt="Assoc. Prof. Trang Hoang, Ph.D." class="w-full h-full object-cover object-top group-hover:scale-105 transition-transform duration-300" onerror="this.style.display='none'; this.nextElementSibling.classList.remove('hidden');">
                <div class="hidden w-full h-full flex items-center justify-center text-xl font-bold text-teal-400">HT</div>
                <div class="absolute bottom-0 inset-x-0 h-8 sm:h-10 bg-gradient-to-t from-[#101726]/80 to-transparent pointer-events-none"></div>
              </div>
              <h4 class="speaker-name text-[13px] sm:text-[14px] font-bold text-white mt-1 transition-colors leading-snug block">Assoc. Prof. Trang Hoang, Ph.D.</h4>
              <p class="speaker-role text-[10.5px] text-slate-400 mt-0.5 leading-tight">Head of Examination & QA Office, Senior IC Design Faculty</p>
              <span class="speaker-organization text-[11px] text-teal-400 font-semibold block mt-0.5 truncate">Ho Chi Minh City University of Technology (HCMUT), VNU-HCM</span>
            </div>
            <div class="mt-2.5 pt-2 border-t border-slate-800/80 flex items-center gap-1.5 text-[10px] sm:text-[10.5px] text-white font-semibold group-hover:underline">
              <span>View Bio & Abstract</span>
              <svg class="w-3.5 h-3.5 group-hover:translate-x-1 transition-all" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
            </div>
          </div>

          <!-- 10. Ms. Loan Nguyen -->
          <div class="mrvll-dark-card speaker-card cursor-pointer group p-3 sm:p-3.5 rounded-xl flex flex-col justify-between border-t-2 border-t-[#00b5e2] bg-[#101726] hover:border-cyan-400/80 transition-all duration-300" data-speaker-id="loan-nguyen">
            <div>
              <div class="relative w-full aspect-square rounded-lg sm:rounded-xl overflow-hidden border border-cyan-500/40 mb-2.5 sm:mb-3 shadow-[0_0_20px_rgba(0,181,226,0.25)] group-hover:border-cyan-400 transition-all bg-cyan-950/80">
                <img src="images/speakers/loan-nguyen.jpg?v=20261013_1200" alt="Ms. Loan Nguyen" class="w-full h-full object-cover object-top group-hover:scale-105 transition-transform duration-300" onerror="this.style.display='none'; this.nextElementSibling.classList.remove('hidden');">
                <div class="hidden w-full h-full flex items-center justify-center text-xl font-bold text-[#00b5e2]">LN</div>
                <div class="absolute bottom-0 inset-x-0 h-8 sm:h-10 bg-gradient-to-t from-[#101726]/80 to-transparent pointer-events-none"></div>
              </div>
              <h4 class="speaker-name text-[13px] sm:text-[14px] font-bold text-white mt-1 transition-colors leading-snug block">Ms. Loan Nguyen</h4>
              <p class="speaker-role text-[10.5px] text-slate-400 mt-0.5 leading-tight">Co-Founder & Chief Executive Officer (CEO)</p>
              <span class="speaker-organization text-[11px] text-[#00b5e2] font-semibold block mt-0.5 truncate">Connexus</span>
            </div>
            <div class="mt-2.5 pt-2 border-t border-slate-800/80 flex items-center gap-1.5 text-[10px] sm:text-[10.5px] text-white font-semibold group-hover:underline">
              <span>View Bio & Abstract</span>
              <svg class="w-3.5 h-3.5 group-hover:translate-x-1 transition-all" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
            </div>
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
      
      <div class="bg-gradient-to-r from-blue-950/40 via-cyan-950/30 to-slate-900/50 p-8 sm:p-12 rounded-2xl border border-blue-500/30 shadow-2xl backdrop-blur-xl">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-12 items-center">
          <div class="lg:col-span-7">
            <span class="brand-eyebrow inline-block text-[#00b5e2] text-sm font-bold uppercase tracking-widest mb-4">
              HIGH-LEVEL STRATEGIC PLENARY
            </span>
            <h2 class="text-2xl sm:text-4xl font-extrabold text-white leading-tight">
              Building Vietnam's National Semiconductor Value Chain 2026&ndash;2035
            </h2>
            <p class="text-slate-300 text-sm sm:text-base mt-4 leading-relaxed">
              A milestone roundtable uniting Government policymakers, multinational semiconductor titans, and top university presidents to establish actionable frameworks for IC design incentives, packaging infrastructure, and workforce readiness.
            </p>

            <div class="mt-8 grid grid-cols-1 sm:grid-cols-3 gap-4 pt-6 border-t border-slate-800/80 text-xs">
              <div>
                <span class="text-slate-400 block uppercase font-bold">Time & Venue</span>
                <span class="font-mono text-cyan-300 font-bold text-sm">16:15 - 16:55 &bull; Grand Ballroom</span>
              </div>
              <div>
                <span class="text-slate-400 block uppercase font-bold">Moderator</span>
                <span class="text-white font-semibold">Mr. Noam Mizrahi</span>
              </div>
              <div>
                <span class="text-slate-400 block uppercase font-bold">Key Focus</span>
                <span class="text-teal-400 font-semibold">National Strategy: 50,000 Engineers & IP Ecosystem</span>
              </div>
            </div>

            <!-- Confirmed Panelists List -->
            <div class="mt-6 pt-4 border-t border-slate-800/60">
              <span class="text-slate-400 block uppercase font-bold text-[11px] mb-2.5">Confirmed Panelists & Leadership:</span>
              <div class="panelist-list flex flex-col sm:flex-row sm:flex-wrap gap-2">
                <div class="flex items-start gap-3 text-sm text-white">
                  <span class="w-1.5 h-1.5 rounded-full bg-[#00b5e2] shrink-0 mt-1 sm:mt-0"></span>
                  <div class="flex flex-wrap items-baseline gap-x-1.5 gap-y-0.5">
                    <strong class="font-bold text-white whitespace-nowrap">Mr. Noam Mizrahi</strong>
                    <span class="text-slate-400 text-[11px]">(Moderator &bull; EVP & Corporate CTO, Marvell Technology)</span>
                  </div>
                </div>
                <div class="flex items-start gap-3 text-sm text-white">
                  <span class="w-1.5 h-1.5 rounded-full bg-[#00b5e2] shrink-0 mt-1 sm:mt-0"></span>
                  <div class="flex flex-wrap items-baseline gap-x-1.5 gap-y-0.5">
                    <strong class="font-bold text-white whitespace-nowrap">Prof. Dr. Mai Nguyen</strong>
                    <span class="text-slate-400 text-[11px]">(President, Viet Nam National University Ho Chi Minh City (VNU-HCM))</span>
                  </div>
                </div>
                <div class="flex items-start gap-3 text-sm text-white">
                  <span class="w-1.5 h-1.5 rounded-full bg-[#00b5e2] shrink-0 mt-1 sm:mt-0"></span>
                  <div class="flex flex-wrap items-baseline gap-x-1.5 gap-y-0.5">
                    <strong class="font-bold text-white whitespace-nowrap">Dr. Phung Nguyen</strong>
                    <span class="text-slate-400 text-[11px]">(Chairman, SHTP)</span>
                  </div>
                </div>
                <div class="flex items-start gap-3 text-sm text-white">
                  <span class="w-1.5 h-1.5 rounded-full bg-teal-400 shrink-0 mt-1 sm:mt-0"></span>
                  <div class="flex flex-wrap items-baseline gap-x-1.5 gap-y-0.5">
                    <strong class="font-bold text-white whitespace-nowrap">Dr. Thuat Nguyen</strong>
                    <span class="text-slate-400 text-[11px]">(Director, Semiconductors and Advanced Materials Institute at the Strategic Technology Institute, Vietnam National University)</span>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Right Column: supplied production image, framed around machine and chip -->
          <div class="lg:col-span-5 flex justify-center lg:justify-end">
            <div class="strategic-panel-image-frame w-full max-w-md overflow-hidden border border-white/20 bg-[#212322]">
              <img src="images/marvell-strategic-panel-production.jpg?v=20261016_panel1" alt="Marvell-branded semiconductor chip beneath a manufacturing machine head" width="2912" height="1632" loading="lazy" decoding="async" class="strategic-panel-image">
            </div>
          </div>
        </div>
      </div>

    </div>
  </section>

  <!-- =========================================================================
       7. INTERACTIVE AGENDA SECTION (CRISP LIGHT THEME - MAXIMUM READABILITY)
       ========================================================================= -->
  <section id="agenda" class="py-20 lg:py-28 bg-[#fbfcfd] border-b border-slate-200">
    <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center mb-12">
        <div class="brand-eyebrow inline-flex items-center gap-2 text-[#0072ce] text-sm font-bold uppercase tracking-widest mb-3">
          <span class="w-1.5 h-1.5 rounded-full bg-[#0072ce] animate-pulse"></span>
          OFFICIAL SUMMIT TIMETABLE
        </div>
        <h2 class="text-3xl sm:text-4xl font-extrabold text-slate-900 tracking-tight">Official Summit Agenda & Timetable</h2>
        <p class="text-slate-600 text-sm sm:text-base mt-2 max-w-2xl mx-auto">Monday, November 23, 2026. Filter sessions by time block or domain track to plan your summit itinerary.</p>
      </div>

      <!-- Session Track Tabs -->
      <div class="flex flex-wrap items-center justify-center gap-2 mb-6 bg-slate-100/90 p-1.5 rounded-xl max-w-xl mx-auto border border-slate-200/60">
        <button class="agenda-tab-btn active px-4 py-2 text-xs font-bold rounded-lg bg-slate-900 text-white shadow-sm transition-all" data-session="all">All Sessions</button>
        <button class="agenda-tab-btn px-4 py-2 text-xs font-bold rounded-lg text-slate-600 hover:text-slate-900 transition-all" data-session="morning">Morning Sessions</button>
        <button class="agenda-tab-btn px-4 py-2 text-xs font-bold rounded-lg text-slate-600 hover:text-slate-900 transition-all" data-session="afternoon">Afternoon Sessions</button>
      </div>

      <!-- Category Filter Pills with Color Dots -->
      <div class="flex flex-wrap items-center justify-center gap-2 mb-10">
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
          <span class="w-2 h-2 rounded-full bg-teal-500"></span>
          <span>Academia & Research</span>
        </button>
        <button class="agenda-filter-pill inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full border border-slate-200 bg-white text-slate-600 hover:border-slate-300 hover:text-slate-900 text-xs font-medium transition-all" data-category="panel">
          <span class="w-2 h-2 rounded-full bg-[#00c7b1]"></span>
          <span>Strategic Panel</span>
        </button>
        <button class="agenda-filter-pill inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full border border-slate-200 bg-white text-slate-600 hover:border-slate-300 hover:text-slate-900 text-xs font-medium transition-all" data-category="networking">
          <span class="w-2 h-2 rounded-full bg-yellow-500"></span>
          <span>Networking</span>
        </button>
      </div>

      <!-- Rendered Agenda Item Cards -->
      <div class="space-y-3.5">
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
      <h2 class="text-3xl font-extrabold text-slate-900 mt-2 mb-10">Uniting Global Chipmakers and Premier Academia</h2>

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
            <p class="text-xs text-slate-500 mt-0.5">Triple R&D Centers of Excellence: Ho Chi Minh City (ET6, UOA) & Da Nang (SP2)</p>
          </div>
        </div>
        <a href="https://www.marvell.com" target="_blank" class="mrvll-btn-primary text-xs shrink-0 py-3">
          <span>ABOUT MARVELL</span>
          <svg class="btn-arrow w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
        </a>
      </div>

      <!-- Strategic Industry & Academic Partners Grid -->
      <div class="text-xs font-bold uppercase tracking-widest text-slate-500 mb-6">GLOBAL SEMICONDUCTOR PARTNERS & PREMIER UNIVERSITIES</div>
      <div class="partner-name-grid max-w-6xl mx-auto grid grid-cols-2 sm:grid-cols-4 xl:grid-cols-8 gap-3.5 items-stretch">
        <div class="min-h-[60px] px-3 py-4 bg-white rounded border border-slate-200 flex items-center justify-center text-sm font-bold text-slate-900">INTEL</div>
        <div class="min-h-[60px] px-3 py-4 bg-white rounded border border-slate-200 flex items-center justify-center text-sm font-bold text-slate-900">QUALCOMM</div>
        <div class="min-h-[60px] px-3 py-4 bg-white rounded border border-slate-200 flex items-center justify-center text-sm font-bold text-slate-900">RENESAS</div>
        <div class="min-h-[60px] px-3 py-4 bg-white rounded border border-slate-200 flex items-center justify-center text-sm font-bold text-slate-900">SYNOPSYS</div>
        <div class="min-h-[60px] px-3 py-4 bg-white rounded border border-slate-200 flex items-center justify-center text-sm font-bold text-slate-900">CONNEXUS</div>
        <div class="min-h-[60px] px-3 py-4 bg-white rounded border border-slate-200 flex items-center justify-center text-sm font-bold text-slate-900">VSAP-LAB</div>
        <div class="min-h-[60px] px-3 py-4 bg-white rounded border border-slate-200 flex items-center justify-center text-sm font-bold text-slate-900">VNU-HCM</div>
        <div class="min-h-[60px] px-3 py-4 bg-white rounded border border-slate-200 flex items-center justify-center text-sm font-bold text-slate-900">HUST</div>
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

      <div class="bg-white p-5 sm:p-8 md:p-10 rounded-2xl border border-slate-200/90 shadow-xl max-w-full">
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
                  <span class="text-[11px] text-slate-500">Practicing Silicon Engineers, Access to all Technical Tracks & Keynotes</span>
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
            <button type="submit" class="mrvll-btn-primary w-full justify-center text-xs sm:text-sm py-3.5 sm:py-4 px-4 sm:px-8 text-center max-w-full">
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
              Yes, <strong>Vietnam Semiconductor Summit 2026</strong> is 100% free for all verified registrants who receive an official invitation letter. Because auditorium seating is limited, registrations are vetted on a first-come, first-approved basis.
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
            <span class="text-slate-900 font-bold block text-xs">Vietnam Semiconductor Summit 2026</span>
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
      <div class="py-8 grid grid-cols-1 md:grid-cols-4 gap-6 border-b border-slate-200/80 text-[11px] text-slate-600">
        <div>
          <span class="font-bold text-slate-900 uppercase block mb-1">Summit Host Secretariat</span>
          <p>Marvell Technology Organizing Committee</p>
          <p class="mt-1">Official Summit Email: <a href="mailto:vietnam-summit@marvell.com" class="text-[#0072ce] font-semibold underline">vietnam-summit@marvell.com</a></p>
        </div>
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

      <div class="pt-8 flex flex-col sm:flex-row items-center justify-between gap-4 text-center sm:text-left text-[11px]">
        <p>&copy; 2026 Marvell Technology, Inc. All rights reserved. Essential technology, done right.</p>
        <p class="text-slate-500 font-mono">Vietnam Semiconductor Summit &bull; Monday, November 23, 2026 &bull; Ho Chi Minh City</p>
      </div>
    </div>
  </footer>

  <!-- =========================================================================
       POP-UP 1: SPEAKER BIO & SESSIONS MODAL (HIGH-TECH MARVELL CANVAS)
       ========================================================================= -->
  <div id="speaker-bio-modal" class="fixed inset-0 z-50 hidden modal-backdrop items-center justify-center p-3 sm:p-4 overflow-y-auto overflow-x-hidden">
    <div class="modal-content-box bg-[#0c1017] max-w-2xl sm:max-w-3xl w-full rounded-2xl border border-cyan-500/40 p-4 sm:p-8 shadow-2xl relative text-left max-h-[90vh] flex flex-col max-w-full">
      <!-- Close Button -->
      <button id="speaker-modal-close" class="absolute top-4 right-4 text-slate-400 hover:text-white p-2 rounded-lg hover:bg-white/10 transition-colors">
        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
      </button>

      <!-- Speaker Profile Header -->
      <div class="flex flex-col sm:flex-row items-start sm:items-center gap-4 sm:gap-6 pb-4 sm:pb-6 border-b border-slate-800 shrink-0">
        <div class="relative w-20 h-20 sm:w-36 sm:h-36 md:w-40 md:h-40 rounded-xl sm:rounded-2xl overflow-hidden border-2 border-cyan-500/60 shadow-[0_0_30px_rgba(0,181,226,0.35)] shrink-0 bg-blue-950/80">
          <img id="speaker-modal-img" src="" alt="Speaker Portrait" class="hidden w-full h-full object-cover object-top" onerror="this.classList.add('hidden'); document.getElementById('speaker-modal-avatar').classList.remove('hidden');">
          <div id="speaker-modal-avatar" class="w-full h-full flex items-center justify-center text-3xl sm:text-5xl font-black text-[#00b5e2]">
            NM
          </div>
        </div>
        <div class="flex-1 min-w-0 pr-6">
          <h3 id="speaker-modal-name" class="text-xl sm:text-3xl font-bold text-white leading-tight">Noam Mizrahi</h3>
          <p id="speaker-modal-title" class="text-xs sm:text-sm font-semibold text-[#00b5e2] mt-1">EVP & Chief Technology Officer (CTO)</p>
          <p id="speaker-modal-org" class="text-xs sm:text-sm text-slate-400 font-medium mt-0.5">Marvell Technology, Inc.</p>
        </div>
      </div>

      <!-- Bio & Sessions Scrollable Body -->
      <div class="py-5 space-y-5 overflow-y-auto modal-scroll-y flex-1 pr-1">
        <div>
          <h4 class="text-xs font-bold uppercase tracking-widest text-slate-400 mb-2 flex items-center gap-2">
            <span class="w-1.5 h-1.5 rounded-full bg-[#00b5e2]"></span>
            <span>BIOGRAPHY & EXECUTIVE PROFILE</span>
          </h4>
          <p id="speaker-modal-bio" class="text-sm text-slate-300 leading-relaxed whitespace-pre-line">...</p>
        </div>

        <div class="pt-2">
          <h4 class="text-xs font-bold uppercase tracking-widest text-slate-400 mb-2.5 flex items-center gap-2">
            <span class="w-1.5 h-1.5 rounded-full bg-[#00b5e2]"></span>
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
        <button id="speaker-modal-rsvp-btn" class="mrvll-btn-primary text-xs py-3 px-4 w-full sm:w-auto justify-center text-center max-w-full">
          <span>REGISTER TO ATTEND</span>
          <svg class="btn-arrow w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
        </button>
      </div>
    </div>
  </div>

  <!-- =========================================================================
       POP-UP 2: QUICK RSVP REGISTRATION MODAL
       ========================================================================= -->
  <div id="quick-rsvp-modal" class="fixed inset-0 z-50 hidden modal-backdrop items-center justify-center p-3 sm:p-4 overflow-y-auto overflow-x-hidden">
    <div class="modal-content-box bg-white max-w-xl w-full rounded-2xl border border-slate-300 p-4 sm:p-8 shadow-2xl relative text-left max-h-[92vh] overflow-y-auto modal-scroll-y max-w-full">
      <!-- Close Button -->
      <button id="quick-rsvp-close" class="absolute top-4 right-4 text-slate-400 hover:text-slate-800 p-2 rounded-lg hover:bg-slate-100 transition-colors">
        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
      </button>

      <div class="mb-5 pr-8">
        <div class="flex items-center gap-2 mb-1.5">
          <span class="w-2 h-2 rounded-full bg-[#0072ce] animate-pulse"></span>
          <span class="text-[11px] font-extrabold tracking-widest text-[#0072ce] uppercase font-mono">FREE RSVP &bull; LIMITED CAPACITY</span>
        </div>
        <h3 class="text-xl sm:text-2xl font-extrabold text-slate-900 leading-tight">Attend Vietnam Semiconductor Summit 2026</h3>
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
                <span class="text-[11px] text-slate-500">Silicon Engineers, Full Technical Access</span>
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
          <button type="submit" class="mrvll-btn-primary w-full justify-center text-xs py-3 sm:py-3.5 px-4 text-center max-w-full">
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
  <div id="ticket-modal" class="fixed inset-0 z-50 hidden modal-backdrop items-center justify-center p-3 sm:p-4 overflow-y-auto overflow-x-hidden">
    <div class="modal-content-box bg-[#0c1017] max-w-lg w-full rounded-2xl border border-cyan-500/50 p-4 sm:p-8 shadow-2xl relative text-left max-w-full">
      
      <!-- Close Button -->
      <button id="modal-close-btn" class="absolute top-4 right-4 text-slate-400 hover:text-white p-2 rounded-lg hover:bg-white/10 transition-colors">
        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
      </button>

      <!-- Badge -->
      <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-teal-950/60 border border-teal-500/30 text-teal-400 text-xs font-bold uppercase tracking-wider mb-4">
        <span class="w-2 h-2 rounded-full bg-teal-400 animate-ping"></span>
        REGISTRATION CONFIRMED &bull; RSVP VALIDATED
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
        <button id="download-ticket-btn" class="mrvll-btn-primary flex-1 justify-center text-xs py-3 px-3 text-center max-w-full">
          <span>PRINT / SAVE TICKET (PDF)</span>
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 17h2a2 2 0 002-2v-4a2 2 0 00-2-2H5a2 2 0 00-2 2v4a2 2 0 002 2h2m2 4h6a2 2 0 002-2v-4a2 2 0 00-2-2H9a2 2 0 00-2 2v4h10z"/></svg>
        </button>
        <button id="add-calendar-btn" class="inline-flex items-center justify-center gap-2 bg-[#101726] border border-cyan-500/40 hover:border-cyan-400 text-[#00b5e2] text-xs font-bold uppercase tracking-wider py-3 px-4 rounded-lg transition-colors max-w-full text-center">
          <span>ADD TO CALENDAR (.ICS)</span>
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg>
        </button>
      </div>

    </div>
  </div>

  <!-- Back to Top Floating Button -->
  <button id="back-to-top-btn" aria-label="Back to top" class="fixed bottom-6 right-6 z-40 p-3 rounded-xl bg-slate-900/90 hover:bg-[#0072ce] text-white shadow-xl border border-slate-700/50 backdrop-blur-md transition-all duration-300 opacity-0 pointer-events-none translate-y-4 flex items-center justify-center group cursor-pointer">
    <svg class="w-5 h-5 group-hover:-translate-y-0.5 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 10l7-7m0 0l7 7m-7-7v18"/>
    </svg>
  </button>

  <!-- Main JavaScript File -->
  <script src="app.js?v=20261016_2153"></script>
</body>
</html>
'''

out_path = os.path.join(base_dir, 'index.html')
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f'Successfully generated {out_path} with Marvell Marketing brand updates')

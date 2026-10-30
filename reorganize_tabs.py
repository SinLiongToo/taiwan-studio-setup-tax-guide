# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    sec_map = {}
    for s in soup.find_all('section'):
        sid = s.get('id')
        if sid:
            sec_map[sid] = s

    # 4 Master Chapters
    chap1 = soup.new_tag('section', id='chap-decision', **{'class': 'tab-content card-custom p-6 md:p-8 space-y-8'})
    chap1.append(sec_map['tab-route'])
    chap1.append(sec_map['tab-client-demands'])
    chap1.append(sec_map['tab-zero-tax'])

    chap2 = soup.new_tag('section', id='chap-receipts', **{'class': 'tab-content card-custom p-6 md:p-8 space-y-8 hidden'})
    chap2.append(sec_map['tab-real-images'])
    chap2.append(sec_map['tab-receipt-types'])

    chap3 = soup.new_tag('section', id='chap-property', **{'class': 'tab-content card-custom p-6 md:p-8 space-y-8 hidden'})
    chap3.append(sec_map['tab-local-taxes'])
    chap3.append(sec_map['tab-stock-other'])

    chap4 = soup.new_tag('section', id='chap-action', **{'class': 'tab-content card-custom p-6 md:p-8 space-y-8 hidden'})
    chap4.append(sec_map['tab-steps'])
    chap4.append(sec_map['tab-401'])
    chap4.append(sec_map['tab-traps'])

    # Style inner sections nicely with dividers
    for k, s in sec_map.items():
        cls = s.get('class', [])
        if 'hidden' in cls: cls.remove('hidden')
        if 'card-custom' in cls: cls.remove('card-custom')
        if 'tab-content' in cls: cls.remove('tab-content')
        s['class'] = 'space-y-6 pt-8 border-t border-slate-200 dark:border-slate-700/60 first:border-t-0 first:pt-0'

    # Clean 4-column master navigation
    nav_html = """
        <!-- 4 大核心章節導覽列 (清楚整齊不雜亂) -->
        <nav class="grid grid-cols-2 md:grid-cols-4 gap-2.5 border-b pb-4" style="border-color: var(--border);">
            <button onclick="switchTab('chap-decision')" class="tab-btn active p-3 rounded-xl text-sm font-bold transition flex items-center justify-center gap-2 border shadow-sm" id="tab-btn-chap1">
                <span>🚦</span> <span class="tab-label">1. 決策篇：免稅免報稅</span>
            </button>
            <button onclick="switchTab('chap-receipts')" class="tab-btn p-3 rounded-xl text-sm font-bold transition flex items-center justify-center gap-2 border shadow-sm" id="tab-btn-chap2">
                <span>📑</span> <span class="tab-label">2. 單據篇：發票收據圖鑑</span>
            </button>
            <button onclick="switchTab('chap-property')" class="tab-btn p-3 rounded-xl text-sm font-bold transition flex items-center justify-center gap-2 border shadow-sm" id="tab-btn-chap3">
                <span>🏡</span> <span class="tab-label">3. 房產篇：住宅登記地方稅</span>
            </button>
            <button onclick="switchTab('chap-action')" class="tab-btn p-3 rounded-xl text-sm font-bold transition flex items-center justify-center gap-2 border shadow-sm" id="tab-btn-chap4">
                <span>🛠️</span> <span class="tab-label">4. 實戰篇：設立登記與報稅</span>
            </button>
        </nav>
    """

    old_nav = soup.find('div', class_='flex flex-wrap gap-2 border-b pb-3')
    if old_nav:
        new_nav_soup = BeautifulSoup(nav_html, 'html.parser')
        old_nav.replace_with(new_nav_soup)

    main_container = soup.find('div', class_='max-w-5xl')
    for s in list(main_container.find_all('section', recursive=False)):
        s.decompose()

    footer = main_container.find('footer')
    footer.insert_before(chap1)
    footer.insert_before(chap2)
    footer.insert_before(chap3)
    footer.insert_before(chap4)

    # Update script dictionary
    script_tag = soup.find_all('script')[-1]
    if script_tag and script_tag.string:
        old_js = script_tag.string
        # update tab labels in JS
        js_replace = """
            tab1: "1. 決策篇：免稅免報稅",
            tab2: "2. 單據篇：發票收據圖鑑",
            tab3: "3. 房產篇：住宅登記地方稅",
            tab4: "4. 實戰篇：設立登記與報稅"
        """
        # write clean script
        pass

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print(f"Processed {filepath}")

process_file('台灣個人工作室設立與稅務全攻略_單檔分享版.html')
process_file('工作室設立與發票報稅全攻略.html')

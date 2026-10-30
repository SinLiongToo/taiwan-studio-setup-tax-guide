# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

def update_standalone_script(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')

    # Update page titles to be sharp and elegant
    title_tag = soup.find('title')
    if title_tag:
        title_tag.string = "台灣個人工作室設立、單據全圖鑑與稅務全攻略（單檔分享版）"

    main_title = soup.find('h1', id='main-title')
    if main_title:
        main_title.string = "台灣個人工作室設立、單據全圖鑑與稅務全攻略"

    sub_title = soup.find('p', id='sub-title')
    if sub_title:
        sub_title.string = "從免稅免報稅抉擇、四大實體單據全真圖鑑（二聯/三聯/收據/勞報）、住家地方稅與囤貨，到 5 步驟取得統編自辦報稅"

    # Perfect interactive script matching the 4 master chapters
    clean_js = """
        // 4 Master Chapters Tab switching
        function switchTab(tabId) {
            document.querySelectorAll('.tab-content').forEach(el => el.classList.add('hidden'));
            document.querySelectorAll('.tab-btn').forEach(btn => {
                btn.classList.remove('active');
            });

            const activeContent = document.getElementById(tabId);
            if (activeContent) activeContent.classList.remove('hidden');

            const activeBtn = event.currentTarget;
            if (activeBtn) {
                activeBtn.classList.add('active');
            }
        }

        // Dual Theme Toggle (Light & Dark)
        const themeBtn = document.getElementById('themeToggle');
        const themeIcon = document.getElementById('themeIcon');
        const themeText = document.getElementById('themeText');

        function setTheme(theme) {
            if (theme === 'dark') {
                document.documentElement.classList.add('dark');
                document.documentElement.classList.remove('light');
                document.documentElement.setAttribute('data-theme', 'dark');
                themeIcon.textContent = '☀️';
                themeText.textContent = currentLang === 'zh' ? '淺色模式' : 'Light Mode';
            } else {
                document.documentElement.classList.remove('dark');
                document.documentElement.classList.add('light');
                document.documentElement.setAttribute('data-theme', 'light');
                themeIcon.textContent = '🌙';
                themeText.textContent = currentLang === 'zh' ? '深色模式' : 'Dark Mode';
            }
        }

        themeBtn.addEventListener('click', () => {
            const isDark = document.documentElement.classList.contains('dark');
            setTheme(isDark ? 'light' : 'dark');
        });

        // Bilingual Dictionary (Traditional Chinese & English)
        const i18n = {
            zh: {
                badge: "實戰避坑 ＆ 單據全圖鑑",
                title: "台灣個人工作室設立、單據全圖鑑與稅務全攻略",
                subtitle: "從免稅免報稅抉擇、四大實體單據全真圖鑑（二聯/三聯/收據/勞報）、住家地方稅與囤貨，到 5 步驟取得統編自辦報稅",
                langBtn: "EN",
                printBtn: "列印 / 存為 PDF",
                themeTextDark: "深色模式",
                themeTextLight: "淺色模式",
                chap1: "1. 決策篇：免稅免報稅",
                chap2: "2. 單據篇：發票收據圖鑑",
                chap3: "3. 房產篇：住宅登記地方稅",
                chap4: "4. 實戰篇：設立登記與報稅"
            },
            en: {
                badge: "Practical Guide & Bill Gallery",
                title: "Taiwan Studio Setup, Bill Gallery & Tax Complete Guide",
                subtitle: "From Zero-Tax route, 4 Physical Bill Simulations (B2C/B2B/Receipts), Property Tax Impact, to 5-Step Registration & Form 401 Filing",
                langBtn: "中文",
                printBtn: "Print / PDF",
                themeTextDark: "Dark Mode",
                themeTextLight: "Light Mode",
                chap1: "1. Decision: Zero Tax & Filing",
                chap2: "2. Bills: Invoice & Receipt Gallery",
                chap3: "3. Property: Home Studio & Tax",
                chap4: "4. Action: Registration & Form 401"
            }
        };

        let currentLang = 'zh';
        const langBtn = document.getElementById('langToggle');
        const langText = document.getElementById('langText');
        const printText = document.getElementById('printText');

        langBtn.addEventListener('click', () => {
            currentLang = currentLang === 'zh' ? 'en' : 'zh';
            langText.textContent = i18n[currentLang].langBtn;
            if (printText) printText.textContent = i18n[currentLang].printBtn;
            document.getElementById('badge-title').textContent = i18n[currentLang].badge;
            document.getElementById('main-title').textContent = i18n[currentLang].title;
            document.getElementById('sub-title').textContent = i18n[currentLang].subtitle;
            
            const btn1 = document.querySelector('#tab-btn-chap1 .tab-label');
            const btn2 = document.querySelector('#tab-btn-chap2 .tab-label');
            const btn3 = document.querySelector('#tab-btn-chap3 .tab-label');
            const btn4 = document.querySelector('#tab-btn-chap4 .tab-label');
            
            if (btn1) btn1.textContent = i18n[currentLang].chap1;
            if (btn2) btn2.textContent = i18n[currentLang].chap2;
            if (btn3) btn3.textContent = i18n[currentLang].chap3;
            if (btn4) btn4.textContent = i18n[currentLang].chap4;

            const isDark = document.documentElement.classList.contains('dark');
            themeText.textContent = isDark ? i18n[currentLang].themeTextLight : i18n[currentLang].themeTextDark;
        });
    """

    # Replace last script
    scripts = soup.find_all('script')
    scripts[-1].string = clean_js

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print(f"Updated {filepath} with clean script and localized labels!")

update_standalone_script('台灣個人工作室設立與稅務全攻略_單檔分享版.html')
update_standalone_script('工作室設立與發票報稅全攻略.html')

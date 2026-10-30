# -*- coding: utf-8 -*-
from playwright.sync_api import sync_playwright
import os

html_path = os.path.abspath('台灣個人工作室設立與稅務全攻略_單檔分享版.html')

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto('file:///' + html_path)
    
    classes = page.evaluate('''() => {
        const set = new Set();
        document.querySelectorAll('*').forEach(el => {
            el.classList.forEach(c => {
                if (c.startsWith('dark:') || c.startsWith('bg-') || c.startsWith('text-')) {
                    set.add(c);
                }
            });
        });
        return Array.from(set).sort();
    }''')
    print("Found classes:", len(classes))
    with open('classes_used.txt', 'w', encoding='utf-8') as f:
        for c in classes:
            f.write(c + '\n')
    browser.close()

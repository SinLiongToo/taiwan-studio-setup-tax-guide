# -*- coding: utf-8 -*-
from playwright.sync_api import sync_playwright
import os

html_path = os.path.abspath('台灣個人工作室設立與稅務全攻略_單檔分享版.html')

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto('file:///' + html_path)
    
    tw_state = page.evaluate('''() => {
        return {
            tailwind_config: window.tailwind ? window.tailwind.config : null,
            document_classes: document.documentElement.className,
        };
    }''')
    print("Tailwind state:", tw_state)
    browser.close()

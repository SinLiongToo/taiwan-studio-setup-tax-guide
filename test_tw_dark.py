# -*- coding: utf-8 -*-
from playwright.sync_api import sync_playwright
import os

html_path = os.path.abspath('台灣個人工作室設立與稅務全攻略_單檔分享版.html')

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto('file:///' + html_path)
    
    test_result = page.evaluate('''() => {
        // Let's test if a div with dark:bg-amber-950 works when html has class 'dark'
        const div = document.createElement('div');
        div.className = 'dark:bg-amber-950 bg-amber-50';
        document.body.appendChild(div);
        
        document.documentElement.classList.add('dark');
        const bgDark = window.getComputedStyle(div).backgroundColor;
        
        return {
            bgDark: bgDark,
            tailwindDefined: typeof tailwind !== 'undefined',
        };
    }''')
    print("Test result:", test_result)
    browser.close()

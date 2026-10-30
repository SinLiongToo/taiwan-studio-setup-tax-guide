# -*- coding: utf-8 -*-
from playwright.sync_api import sync_playwright
import os

html_path = os.path.abspath('台灣個人工作室設立與稅務全攻略_單檔分享版.html')

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={'width': 1280, 'height': 1200})
    page.goto('file:///' + html_path)
    page.click('#themeToggle')
    page.wait_for_timeout(300)
    page.click('#tab-btn-chap4')
    page.wait_for_timeout(300)
    
    styles = page.evaluate('''() => {
        const amber1 = document.querySelector('.bg-amber-50');
        const amber2 = document.querySelector('#step5_d .bg-amber-50');
        
        return {
            amber1_bg: amber1 ? window.getComputedStyle(amber1).backgroundColor : null,
            amber1_color: amber1 ? window.getComputedStyle(amber1).color : null,
            amber2_bg: amber2 ? window.getComputedStyle(amber2).backgroundColor : null,
            amber2_color: amber2 ? window.getComputedStyle(amber2).color : null,
        };
    }''')
    print("Computed Amber styles in dark mode:", styles)
    browser.close()

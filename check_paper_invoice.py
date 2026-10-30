# -*- coding: utf-8 -*-
from playwright.sync_api import sync_playwright
import os

html_path = os.path.abspath('台灣個人工作室設立與稅務全攻略_單檔分享版.html')

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto('file:///' + html_path)
    page.click('#themeToggle') # dark mode
    page.click('#tab-btn-chap2') # bill chapter
    page.wait_for_timeout(300)
    
    styles = page.evaluate('''() => {
        const wrap = document.querySelector('.paper-invoice');
        const buyerBox = wrap ? wrap.querySelector('.rounded') : null;
        const buyerStrong = buyerBox ? buyerBox.querySelector('strong') : null;
        const buyerSpan = buyerBox ? buyerBox.querySelector('span') : null;
        const table = wrap ? wrap.querySelector('table') : null;
        const td = table ? table.querySelector('td') : null;
        
        return {
            wrap_bg: wrap ? window.getComputedStyle(wrap).backgroundColor : null,
            wrap_color: wrap ? window.getComputedStyle(wrap).color : null,
            buyerBox_bg: buyerBox ? window.getComputedStyle(buyerBox).backgroundColor : null,
            buyerStrong_color: buyerStrong ? window.getComputedStyle(buyerStrong).color : null,
            buyerSpan_color: buyerSpan ? window.getComputedStyle(buyerSpan).color : null,
            td_bg: td ? window.getComputedStyle(td).backgroundColor : null,
            td_color: td ? window.getComputedStyle(td).color : null,
        };
    }''')
    print("Exact computed styles of paper-invoice in dark mode:", styles)
    browser.close()

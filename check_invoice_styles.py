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
        const table = document.querySelector('.paper-invoice-triplicate table');
        const td = table ? table.querySelector('td') : null;
        const buyerBox = document.querySelector('.paper-invoice-triplicate div.rounded');
        return {
            td_bg: td ? window.getComputedStyle(td).backgroundColor : null,
            td_color: td ? window.getComputedStyle(td).color : null,
            table_bg: table ? window.getComputedStyle(table).backgroundColor : null,
            buyerBox_bg: buyerBox ? window.getComputedStyle(buyerBox).backgroundColor : null,
            buyerBox_color: buyerBox ? window.getComputedStyle(buyerBox).color : null,
        };
    }''')
    print("Exact computed styles of invoice in dark mode:", styles)
    browser.close()

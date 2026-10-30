# -*- coding: utf-8 -*-
from playwright.sync_api import sync_playwright
import os

html_path = os.path.abspath('台灣個人工作室設立與稅務全攻略_單檔分享版.html')

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto('file:///' + html_path)
    page.click('#themeToggle')
    page.wait_for_timeout(300)
    page.click('#tab-btn-chap4')
    page.wait_for_timeout(300)
    
    styles = page.evaluate('''() => {
        const el = document.querySelector('#step2_d div');
        const li = el ? el.querySelector('li') : null;
        const payout = document.querySelector('#tab-channel-payout .border-emerald-500');
        const payout_li = payout ? payout.querySelector('li') : null;
        
        return {
            step2_bg: el ? window.getComputedStyle(el).backgroundColor : 'none',
            step2_color: li ? window.getComputedStyle(li).color : 'none',
            payout_bg: payout ? window.getComputedStyle(payout).backgroundColor : 'none',
            payout_color: payout_li ? window.getComputedStyle(payout_li).color : 'none',
        };
    }''')
    print("Exact computed styles in dark mode:", styles)
    browser.close()

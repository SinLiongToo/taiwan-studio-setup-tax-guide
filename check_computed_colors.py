# -*- coding: utf-8 -*-
from playwright.sync_api import sync_playwright
import os

html_path = os.path.abspath('台灣個人工作室設立與稅務全攻略_單檔分享版.html')

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto('file:///' + html_path)
    page.wait_for_timeout(500)
    
    # Toggle to dark mode
    page.click('#themeToggle')
    page.wait_for_timeout(500)
    
    # Click 4th tab button by id: tab-btn-action
    page.click('#tab-btn-action')
    page.wait_for_timeout(500)
    
    # Inspect computed colors
    info = page.evaluate('''() => {
        const s2_box = document.querySelector('#step2_d .rounded-xl');
        const s2_li = document.querySelector('#step2_d li');
        const payout_a = document.querySelector('#tab-channel-payout .border-emerald-500');
        const payout_a_li = payout_a ? payout_a.querySelector('li') : null;
        
        return {
            s2_box_bg: s2_box ? window.getComputedStyle(s2_box).backgroundColor : null,
            s2_li_color: s2_li ? window.getComputedStyle(s2_li).color : null,
            payout_a_bg: payout_a ? window.getComputedStyle(payout_a).backgroundColor : null,
            payout_a_color: payout_a_li ? window.getComputedStyle(payout_a_li).color : null,
        };
    }''')
    print("Computed dark mode styles:", info)
    page.screenshot(path='dark_chap4.png')
    browser.close()

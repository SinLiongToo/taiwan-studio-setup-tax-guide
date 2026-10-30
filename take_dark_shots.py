# -*- coding: utf-8 -*-
from playwright.sync_api import sync_playwright
import os

html_path = os.path.abspath('台灣個人工作室設立與稅務全攻略_單檔分享版.html')

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={'width': 1280, 'height': 1200})
    page.goto('file:///' + html_path)
    page.wait_for_timeout(500)
    
    # Toggle to dark mode
    page.click('#themeToggle')
    page.wait_for_timeout(500)
    
    # Click 4th tab button: tab-btn-chap4
    page.click('#tab-btn-chap4')
    page.wait_for_timeout(500)
    
    # Take screenshot of chapter 4
    page.screenshot(path='dark_chap4.png', full_page=False)
    
    # Also click 1st tab to see channel payout card in dark mode
    page.click('#tab-btn-chap1')
    page.wait_for_timeout(500)
    page.screenshot(path='dark_chap1.png', full_page=False)
    
    print("Screenshots taken successfully!")
    browser.close()

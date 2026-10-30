# -*- coding: utf-8 -*-
from playwright.sync_api import sync_playwright
import os

html_path = os.path.abspath('台灣個人工作室設立與稅務全攻略_單檔分享版.html')

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={'width': 1280, 'height': 1200})
    page.goto('file:///' + html_path)
    page.click('#themeToggle') # dark mode
    page.click('#tab-btn-chap2') # bill chapter
    page.wait_for_timeout(300)
    
    # Scroll to triplicate invoice
    page.locator('.paper-invoice').scroll_into_view_if_needed()
    page.wait_for_timeout(300)
    
    page.screenshot(path='dark_invoice_fixed.png')
    print("Screenshot saved to dark_invoice_fixed.png")
    browser.close()

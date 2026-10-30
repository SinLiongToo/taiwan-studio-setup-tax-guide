# -*- coding: utf-8 -*-
from playwright.sync_api import sync_playwright
import os

html_path = os.path.abspath('台灣個人工作室設立與稅務全攻略_單檔分享版.html')

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto('file:///' + html_path)
    page.wait_for_timeout(1000)
    
    # Toggle to dark mode
    page.click('#themeToggle')
    page.wait_for_timeout(500)
    
    # Inspect computed background color and text color of the card in the user's screenshot
    # Check #tab-channel-payout and #step2_t card
    channel_card = page.locator('#tab-channel-payout')
    step2_card = page.locator('#step2_t')
    
    page.screenshot(path='dark_test_before.png', full_page=False)
    print("Screenshot saved to dark_test_before.png")
    
    browser.close()

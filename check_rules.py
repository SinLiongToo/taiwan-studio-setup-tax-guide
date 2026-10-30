# -*- coding: utf-8 -*-
from playwright.sync_api import sync_playwright
import os

html_path = os.path.abspath('台灣個人工作室設立與稅務全攻略_單檔分享版.html')

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto('file:///' + html_path)
    
    css_rules = page.evaluate('''() => {
        let rulesWithDark = 0;
        for (let sheet of document.styleSheets) {
            try {
                for (let r of sheet.cssRules) {
                    if (r.selectorText && r.selectorText.includes('.dark')) {
                        rulesWithDark++;
                    }
                }
            } catch(e) {}
        }
        return {
            totalSheets: document.styleSheets.length,
            rulesWithDark: rulesWithDark
        };
    }''')
    print("CSS rules with dark:", css_rules)
    browser.close()

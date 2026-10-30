# -*- coding: utf-8 -*-
from playwright.sync_api import sync_playwright
import os

html_path = os.path.abspath('台灣個人工作室設立與稅務全攻略_單檔分享版.html')

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto('file:///' + html_path)
    
    script_eval = page.evaluate('''() => {
        // Find all dark:* rules in the document stylesheets
        const darkRules = [];
        for (let sheet of document.styleSheets) {
            try {
                for (let r of sheet.cssRules) {
                    if (r.selectorText && r.selectorText.includes('dark\\\\:')) {
                        darkRules.push(r.selectorText);
                    }
                }
            } catch(e) {}
        }
        return {
            count: darkRules.length,
            sample: darkRules.slice(0, 10)
        };
    }''')
    print("Dark rules in stylesheets:", script_eval)
    browser.close()

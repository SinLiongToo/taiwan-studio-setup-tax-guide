# -*- coding: utf-8 -*-
import re

with open('tailwind_inlined.js', 'r', encoding='utf-8') as f:
    tw_js = f.read()

def inline_in_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    # Find the external script tag
    pattern = r'<script\s+src=[\"\'].*?tailwindcss\.min\.js[\"\']>\s*</script>'
    if re.search(pattern, html):
        html = re.sub(pattern, lambda m: '<script>\n' + tw_js + '\n</script>', html, count=1)
        print(f"Inlined Tailwind into {filename}")
    else:
        print(f"External script not found in {filename}")

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)

inline_in_file('台灣個人工作室設立與稅務全攻略_單檔分享版.html')
inline_in_file('工作室設立與發票報稅全攻略.html')

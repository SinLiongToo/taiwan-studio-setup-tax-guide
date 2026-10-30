# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

with open('台灣個人工作室設立與稅務全攻略_單檔分享版.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# We want 4 clear, well-structured main chapters:
# Chapter 1: 🚦 【決策篇】要開發票嗎？免稅與客需應對
#   - tab-route (免稅+免報稅路線抉擇)
#   - tab-client-demands (客人非要發票怎麼辦？4大解法)
#   - tab-zero-tax (三年10萬如何實質0稅額)
#
# Chapter 2: 📑 【單據篇】三大請款單據與全真圖鑑
#   - tab-real-images (1:1 實物單據圖鑑：勞報單 / 免用發票收據 / 三聯發票)
#   - tab-receipt-types (白話解密：什麼是勞報單？三聯單？)
#
# Chapter 3: 🏡 【房產篇】住家登記、地方稅與囤貨
#   - tab-local-taxes (地方稅衝擊：房屋稅地價稅有用vs沒用、賣房400萬隱藏炸彈)
#   - tab-stock-other (囤在別人家有付錢？租賃與加稅衝擊)
#
# Chapter 4: 🛠️ 【實戰篇】設立登記、自辦401與避坑地雷
#   - tab-steps (五步驟取得統編與設立流程)
#   - tab-401 (自辦401線上申報加減邏輯)
#   - tab-traps (營業稅法第19條不可扣抵進項地雷)

print('Soup parsed successfully.')

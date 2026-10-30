# -*- coding: utf-8 -*-
import glob

fpaths = glob.glob('*.html')

# We want to add:
# 1. In Chapter 1 (tab-zero-tax): A dedicated clear comparison for '方案 B (工作室請款)' vs '方案 A (個人請款)'
#    Can Option B also achieve '免稅 / 免報稅'?
#    Answer:
#    - 營業稅：若申請到「免用統一發票」，國稅局核定免開，且每季營業額低於起徵點（勞務4萬/月、買賣8萬/月），國稅局免發稅單 = 0 營業稅、0 申報！
#    - 營所稅：獨資行號「免納營利事業所得稅」，營利所得穿透至個人。
#    - 個人綜所稅：因一年才3.3萬營收，遠低於個人免稅扣除額，實質「0 所得稅」！
#    - 但若被核定「使用統一發票」：雖然稅額可靠進項或圖書免稅扣到0，但「無法免報稅」，每2個月一定要交 401 申報書。
#
# 2. In Chapter 4 (tab-steps):
#    - Add Step 6 (or update step 4/5): 「前往銀行開立工作室商業戶（行號戶）」
#      戶名長相：【工作室名稱 負責人姓名】（例如：史秀里冊房 涂○○）
#      所需文件：商業登記核准函、國稅局稅籍公文、身分證、大小章、健保卡/駕照
#      重要金流原則：發票開工作室抬頭，通路匯款就必須進工作室商業戶，會計才能核銷，不可隨意匯入個人戶！
#    - In Step 2 (設立登記): 明確標註申請資本額未達 25 萬免附存款餘額證明，不用先開籌備處。
# 3. Add an interactive modal/card or direct section on 「出書/接案通路請款實戰指南：方案 A（個人）vs 方案 B（工作室）」

print('Script ready')

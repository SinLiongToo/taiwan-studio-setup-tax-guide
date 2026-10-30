# -*- coding: utf-8 -*-
import sys
from bs4 import BeautifulSoup

files = ['台灣個人工作室設立與稅務全攻略_單檔分享版.html', '工作室設立與發票報稅全攻略.html']

insertion_html = """
<!-- 國稅局臨櫃現場問答交戰手冊（籌備期、個人出版/創作、問要不要開業） -->
<div class="p-4 rounded-xl bg-gradient-to-br from-indigo-50 to-blue-50 dark:from-slate-900 dark:to-indigo-950/40 border-2 border-indigo-300 dark:border-indigo-700 space-y-3 mt-4" id="tax_office_interview_sop">
    <div class="flex items-center gap-2">
        <span class="text-xl">🏛️</span>
        <h5 class="font-bold text-sm md:text-base text-indigo-950 dark:text-indigo-200">
            國稅局臨櫃現場實戰問答 SOP（特別適用：個人創作／獨立出版／籌備期）
        </h5>
    </div>
    <div class="space-y-2.5 text-xs md:text-sm text-slate-700 dark:text-slate-300">
        <div class="p-3 rounded-lg bg-white/80 dark:bg-slate-900/80 border border-indigo-200 dark:border-indigo-800">
            <p class="font-bold text-indigo-900 dark:text-indigo-300 mb-1">❓ 承辦員問：「要不要開業？何時開業？」</p>
            <p><strong>✅ 建議回答：</strong>「目前還在文字創作與籌備期，請幫我填『預定開業日』（填下個月或下季初，如下月 1 日）。」</p>
            <p class="text-xs text-slate-500 dark:text-slate-400 mt-1">💡 <strong>背後好處：</strong> 爭取籌備緩衝期，避免當期無收入卻提早產生申報負擔；房屋稅營業用起算日也會跟著延後。</p>
        </div>
        <div class="p-3 rounded-lg bg-white/80 dark:bg-slate-900/80 border border-indigo-200 dark:border-indigo-800">
            <p class="font-bold text-indigo-900 dark:text-indigo-300 mb-1">❓ 承辦員問：「預估每月營業額多少？要不要發票？」</p>
            <p><strong>✅ 建議回答：</strong>「我做的是獨立出版與個人創作，過去出版其實都賠錢。這半年都在籌備寫作，幾個月才賣得出幾本書，每個月營收非常低（幾千元或掛零），遠低於 8 萬元起徵點，請務必幫我核定<strong>『免用統一發票（小規模營業人）』</strong>。」</p>
            <p class="text-xs text-slate-500 dark:text-slate-400 mt-1">💡 <strong>關鍵優勢：</strong> 核定免用發票後，<strong>免每 2 個月申報營業稅、免每年辦理營所稅結算申報</strong>（省下每年 2~3 萬記帳費）！</p>
        </div>
        <div class="p-3 rounded-lg bg-white/80 dark:bg-slate-900/80 border border-indigo-200 dark:border-indigo-800">
            <p class="font-bold text-indigo-900 dark:text-indigo-300 mb-1">❓ 現場就知道可不可以免報嗎？何時拍板定案？</p>
            <p><strong>• 明天現場：</strong> 櫃台審核同意以免用發票送件，心裡就有八、九成把握。<br>
            <strong>• 正式確認（約 3~7 天）：</strong> 收到國稅局掛號核准公文，只要上面載明<strong>『准予免用統一發票』</strong>，即 100% 正式確認免每期報稅！</p>
        </div>
        <div class="p-3 rounded-lg bg-emerald-50 dark:bg-emerald-950/40 border border-emerald-300 dark:border-emerald-700 text-emerald-900 dark:text-emerald-200">
            <p class="font-bold mb-1">🏡 房屋稅 100% 全額自住優惠爭取小撇步（現況完全符合！）：</p>
            <p>若現況為<strong>「完全無招牌、無實體店面、無雇用員工、家中無堆放庫存貨物」</strong>，國稅局核准通報地方稅捐處後，向稅捐處主張純住家通訊聯絡並簽署切結書，即有很高機會<strong>爭取全戶 100% 保留自住房屋稅（1.2%）與自用地價稅（2‰）</strong>，連 1/6 都不用切！</p>
        </div>
    </div>
</div>
"""

for fn in files:
    with open(fn, 'r', encoding='utf-8') as f:
        html = f.read()
    soup = BeautifulSoup(html, 'html.parser')
    step3_d = soup.find(id='step3_d')
    if step3_d:
        if not soup.find(id='tax_office_interview_sop'):
            new_block = BeautifulSoup(insertion_html, 'html.parser')
            step3_d.append(new_block)
            with open(fn, 'w', encoding='utf-8') as f:
                f.write(str(soup))
            print(f'Successfully updated {fn}')
        else:
            print(f'Already exists in {fn}')
    else:
        print(f'step3_d not found in {fn}')

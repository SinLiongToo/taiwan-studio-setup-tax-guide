import glob

files = glob.glob('*.html')
print("Found files:", files)

tax_block = """<!-- 方案 B：工作室請款是否能免稅、免報稅全解析 -->
<div class="p-5 rounded-xl border-2 border-indigo-500 bg-indigo-50/50 dark:bg-indigo-950/30 space-y-3 mb-6">
  <div class="flex items-center justify-between flex-wrap gap-2">
    <h3 class="font-bold text-base text-indigo-900 dark:text-indigo-200 flex items-center gap-2">
      <span>💡</span> 關鍵疑問解答：走「方案 B（工作室/商業戶）」請款，也有可能「免稅、免報稅」嗎？
    </h3>
    <span class="text-xs font-bold px-2.5 py-1 rounded-full bg-indigo-200 dark:bg-indigo-800 text-indigo-800 dark:text-indigo-200">
      核心答案：完全有可能！取決於核定的稅籍路線
    </span>
  </div>
  <p class="text-xs md:text-sm text-slate-700 dark:text-slate-300 leading-relaxed">
    如果您決定以<strong>「工作室（商業戶）」</strong>的名義向通路或客戶請款，是否需要繳稅與定期報稅，完全取決於您申請到的<strong>稅籍身分</strong>：
  </p>
  <div class="grid md:grid-cols-2 gap-3 text-xs md:text-sm">
    <div class="p-3.5 rounded-lg bg-emerald-50 dark:bg-emerald-950/50 border border-emerald-300 dark:border-emerald-700 space-y-1.5">
      <div class="font-bold text-emerald-800 dark:text-emerald-300 flex items-center gap-1.5">
        <span>🟢</span> 情況一：核定為「免用發票小規模行號」（最高境界）
      </div>
      <ul class="list-disc list-inside space-y-1 text-slate-700 dark:text-slate-300">
        <li><strong>營業稅：【免報稅 ＋ 免繳稅】！</strong> 每月營業額未達起徵點（勞務4萬、買賣8萬），國稅局查定營業稅為 0 元，<strong>連稅單都不會寄出，平時完全不用定期線上報稅</strong>！</li>
        <li><strong>營所稅：【免納營所稅】！</strong> 獨資行號免繳營利事業所得稅。</li>
        <li><strong>個人綜所稅：【免所得稅】！</strong> 三年 10 萬（平均每年僅 3.3 萬）營利所得穿透到個人，全額被每年個人的免稅額與扣除額吸收，個人綜所稅一樣為 0 元！</li>
        <li><strong>請款方式：</strong> 開立「免用統一發票收據」，款項匯入工作室專屬銀行商業戶頭。</li>
      </ul>
    </div>
    <div class="p-3.5 rounded-lg bg-blue-50 dark:bg-blue-950/50 border border-blue-300 dark:border-blue-700 space-y-1.5">
      <div class="font-bold text-blue-800 dark:text-blue-300 flex items-center gap-1.5">
        <span>🔵</span> 情況二：核定為「使用統一發票」（有發票資格）
      </div>
      <ul class="list-disc list-inside space-y-1 text-slate-700 dark:text-slate-300">
        <li><strong>稅額：【實質 0 稅】！</strong> 圖書出版品依法可申請審查免徵營業稅（免稅發票），或用進項發票（電腦、文具、耗材）扣抵銷項稅額至 0 元；營所稅亦因獨資行號免納。</li>
        <li><strong>申報義務：【⚠️ 無法免申報】！</strong> 即使稅額為 0 元，<strong>每 2 個月（單數月 1~15 日）仍必須親自或請會計線上申報 401 零申報書</strong>，不可漏報。</li>
        <li><strong>請款方式：</strong> 開立二聯/三聯電子或手寫發票，款項匯入工作室專屬銀行商業戶頭。</li>
      </ul>
    </div>
  </div>
</div>
"""

step6_block = """<div class="p-4 rounded-xl box-info flex gap-4 items-start border-2 border-blue-500/30">
<div class="w-8 h-8 rounded-full bg-blue-600 text-white flex items-center justify-center font-bold flex-shrink-0">6</div>
<div class="space-y-2">
  <div class="flex items-center gap-2 flex-wrap">
    <h4 class="font-bold text-base text-blue-900 dark:text-blue-200">
      前往銀行開立工作室專屬「商業戶（行號戶）」（正式公司戶）
    </h4>
    <span class="text-xs font-semibold px-2 py-0.5 rounded-full bg-blue-200 text-blue-800 dark:bg-blue-800 dark:text-blue-200">
      對外請款與商業金流必備
    </span>
  </div>
  <p class="text-sm desc-text leading-relaxed">
    當您拿到<strong>縣市政府商業核准函</strong>與<strong>國稅局稅籍核准公文（統一編號）</strong>後，即可攜帶文件至任何銀行開設專屬的工作室行號帳戶。
  </p>
  <div class="grid md:grid-cols-3 gap-3 text-xs md:text-sm pt-1">
    <div class="p-3 rounded-lg bg-white/80 dark:bg-slate-900/80 border border-blue-200 dark:border-blue-900/60 space-y-1">
      <strong class="text-blue-700 dark:text-blue-300 block">🏦 戶名長相格式</strong>
      <p class="text-slate-600 dark:text-slate-300">
        依法獨資行號的銀行戶名為：<br>
        <span class="font-mono font-bold text-slate-800 dark:text-slate-100 bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">【工作室名稱 負責人姓名】</span><br>
        （例：史秀里冊房 涂○○）
      </p>
    </div>
    <div class="p-3 rounded-lg bg-white/80 dark:bg-slate-900/80 border border-blue-200 dark:border-blue-900/60 space-y-1">
      <strong class="text-blue-700 dark:text-blue-300 block">📋 開戶必備文件</strong>
      <ul class="list-disc list-inside text-slate-600 dark:text-slate-300 space-y-0.5">
        <li>縣市政府商業登記核准函</li>
        <li>國稅局稅籍登記核准函</li>
        <li>負責人身分證 ＋ 第二證件</li>
        <li>工作室大章 ＋ 負責人私章</li>
      </ul>
    </div>
    <div class="p-3 rounded-lg bg-white/80 dark:bg-slate-900/80 border border-blue-200 dark:border-blue-900/60 space-y-1">
      <strong class="text-blue-700 dark:text-blue-300 block">⚠️ 為什麼不能匯個人戶？</strong>
      <p class="text-slate-600 dark:text-slate-300">
        只要憑證開立「工作室統編抬頭」，通路與公司會計系統查核受款人時，<strong>受款戶名必須與憑證抬頭相符</strong>，否則金流憑證不一會被退件擋款！
      </p>
    </div>
  </div>
</div>
</div>
"""

payout_block = """<!-- 通路出版/接案請款實戰指南：方案 A (個人) vs 方案 B (工作室) -->
<section class="space-y-4 pt-6 border-t border-slate-200 dark:border-slate-700/60" id="tab-channel-payout">
  <div class="flex items-center justify-between flex-wrap gap-2">
    <h3 class="text-lg font-bold flex items-center gap-2 text-indigo-700 dark:text-indigo-400">
      <span>📚</span> 出版社／經銷通路請款實戰指南：方案 A（個人自然人） vs 方案 B（工作室商業戶）
    </h3>
    <span class="text-xs font-bold px-2 py-0.5 rounded bg-amber-100 text-amber-800 dark:bg-amber-900/60 dark:text-amber-200">
      即時請款決策
    </span>
  </div>
  <p class="text-xs md:text-sm desc-text leading-relaxed">
    出書給通路請款時，發行商是<strong>付款人</strong>，您是<strong>收款人</strong>。截圖中標註的「開立發票」，是指如果您在通路系統登記為「公司戶」，必須開立憑證寄回通路，財務才能撥款：
  </p>
  <div class="grid md:grid-cols-2 gap-4 text-xs md:text-sm">
    <div class="p-4 rounded-xl border-2 border-emerald-500 bg-white dark:bg-slate-900 space-y-2">
      <div class="flex items-center justify-between">
        <span class="font-bold text-emerald-700 dark:text-emerald-400 text-sm">方案 A：填寫「個人戶（自然人）」請款</span>
        <span class="text-[11px] font-bold px-2 py-0.5 rounded bg-emerald-100 text-emerald-800 dark:bg-emerald-900 dark:text-emerald-200">推薦：本期最速領款</span>
      </div>
      <ul class="space-y-1.5 list-disc list-inside desc-text">
        <li><strong>如何請款：</strong> 通路基本資料填寫您<strong>個人的身分證字號與現有的個人銀行帳號</strong>。</li>
        <li><strong>憑證要求：</strong> <strong>完全不需要開發票或收據！</strong> 系統線上點請款後，通路會寄送「個人版稅／稿費簽收單（9B）」。</li>
        <li><strong>稅務優惠：</strong> 圖書著作權屬於個人版稅與稿費，每人每年享高達 <strong>18 萬元的法定免稅額</strong>。三年 10 萬內完全 0 稅款！</li>
        <li><strong>適合時機：</strong> 工作室尚未核准下來、或者手邊尚無銀行行號戶頭，想在當期截止日前順利把錢領進來。</li>
      </ul>
    </div>
    <div class="p-4 rounded-xl border-2 border-blue-500 bg-white dark:bg-slate-900 space-y-2">
      <div class="flex items-center justify-between">
        <span class="font-bold text-blue-700 dark:text-blue-400 text-sm">方案 B：填寫「公司戶（工作室商業戶）」請款</span>
        <span class="text-[11px] font-bold px-2 py-0.5 rounded bg-blue-100 text-blue-800 dark:bg-blue-900 dark:text-blue-200">工作室品牌常規金流</span>
      </div>
      <ul class="space-y-1.5 list-disc list-inside desc-text">
        <li><strong>如何請款：</strong> 必須等收到商業登記＋國稅局核准函，並前往銀行開立<strong>【工作室 負責人】行號戶</strong>後才能請領。</li>
        <li><strong>憑證要求：</strong>
          <ul class="list-circle list-inside pl-4 space-y-0.5 text-[11px] md:text-xs text-slate-500 dark:text-slate-400">
            <li>• 若為小規模免用發票：寄送<strong>「免用統一發票收據」</strong>（蓋發票章＋私章）。</li>
            <li>• 若為使用統一發票：開立<strong>「圖書免稅發票」或二/三聯發票</strong>。</li>
          </ul>
        </li>
        <li><strong>是否能免稅/免報稅：</strong>
          <ul class="list-circle list-inside pl-4 space-y-0.5 text-[11px] md:text-xs text-slate-500 dark:text-slate-400">
            <li>• 若核定「免用發票」：月營業額低於起徵點，<strong>營業稅 0 元、免定期報稅、營所稅 0 元、個人綜所 0 元</strong>！</li>
            <li>• 若核定「使用發票」：稅額可扣抵為 0 元，但每 2 個月<strong>必須進行 401 零申報</strong>。</li>
          </ul>
        </li>
        <li><strong>適合時機：</strong> 工作室完全設立、銀行公司戶已開立，後續每月的長期定期書款結算。</li>
      </ul>
    </div>
  </div>
</section>
"""

for fp in files:
    with open(fp, 'r', encoding='utf-8') as f:
        c = f.read()

    # 1. Tax explanation in tab-zero-tax
    if '方案 B：工作室請款是否能免稅、免報稅全解析' not in c:
        marker = 'id="t1_box1_t"'
        pos2 = c.find(marker)
        if pos2 != -1:
            grid_pos = c.rfind('<div class="grid md:grid-cols-2 gap-4">', 0, pos2)
            if grid_pos != -1:
                c = c[:grid_pos] + tax_block + c[grid_pos:]
                print('Tax block inserted in', fp)

    # 2. Add step 6
    if '前往銀行開立工作室專屬「商業戶（行號戶）」' not in c:
        step5_anchor = 'id="step5_t"'
        pos_s5 = c.find(step5_anchor)
        if pos_s5 != -1:
            tab401_pos = c.find('id="tab-401"')
            if tab401_pos != -1:
                insert_pos = c.rfind('</div>\n</div>\n</div>', 0, tab401_pos)
                if insert_pos != -1:
                    # After step 5 div closes
                    end_step5 = insert_pos + len('</div>\n</div>\n</div>')
                    c = c[:end_step5] + '\n' + step6_block + c[end_step5:]
                    print('Step 6 inserted in', fp)

    # 3. Add payout_block
    if '出版社／經銷通路請款實戰指南' not in c:
        chap_rec_pos = c.find('id="chap-receipts"')
        if chap_rec_pos != -1:
            sec_start = c.rfind('<section', 0, chap_rec_pos)
            if sec_start != -1:
                c = c[:sec_start] + payout_block + c[sec_start:]
                print('Payout guide inserted in', fp)

    with open(fp, 'w', encoding='utf-8') as f:
        f.write(c)

print("Batch update script execution complete!")

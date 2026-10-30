# -*- coding: utf-8 -*-
import glob

files = glob.glob('*.html')
print("Found files:", files)

target_pattern = """<div class="space-y-2 text-sm desc-text" id="step5_d">
<div class="p-3 rounded-lg bg-amber-50 dark:bg-amber-950/30 border border-amber-300 dark:border-amber-700 text-amber-900 dark:text-amber-200">
<strong>⚠️ 重大觀念澄清（千萬別搞錯時機與機關）：</strong><br/>
• <strong>在商工一站式送件時：</strong> 無法申報房屋稅率（國稅局只管統一編號與營業稅，無權決定房屋稅率）。<br/>
• <strong>正確時機：</strong> 國稅局審查通過並核發「稅籍登記核准公文」後，國稅局系統會<strong>自動通報「地方稅捐稽徵處」</strong>。請務必在<strong>核准後 15 天內</strong>，主動向房屋所在地的地方稅捐稽徵處送件申請！
</div>
<p><strong>申請兩大策略（二擇一）：</strong></p>
<ul class="list-disc list-inside space-y-1">
<li><strong>策略 A（無囤貨/純線上接案）：</strong> 主張依《財政部104年台財稅字第10400128120號令》，該址純為「通訊聯絡場所」，爭取<strong>全戶 100% 維持自住稅率（房屋稅 1.2%、地價稅 2‰）</strong>。</li>
<li><strong>策略 B（有工作桌電腦）：</strong> 申請按法定最低<strong>「實際營業面積 1/6 課徵營業用」</strong>（僅 1/6 面積課 3%，其餘 5/6 面積保留 1.2% 自住優惠）。</li>
</ul>
</div>"""

replacement_content = """<div class="space-y-3 text-sm desc-text" id="step5_d">
<div class="p-3 rounded-lg bg-amber-50 dark:bg-amber-950/30 border border-amber-300 dark:border-amber-700 text-amber-900 dark:text-amber-200">
<strong>⚠️ 重大觀念澄清（千萬別搞錯時機與機關）：</strong><br/>
• <strong>在商工一站式送件時：</strong> 無法申報房屋稅率（國稅局只管統一編號與營業稅，無權決定房屋稅率）。<br/>
• <strong>正確時機：</strong> 國稅局審查通過並核發「稅籍登記核准公文」後，國稅局系統會<strong>自動通報「臺南市政府財政稅務局」</strong>。請務必在<strong>核准後 15 天內</strong>，提出節稅申請！
</div>

<!-- 關鍵疑問：一定要親自去嗎？不去會怎樣？ -->
<div class="p-4 rounded-xl border-2 border-red-400 bg-red-50/60 dark:bg-red-950/30 space-y-2.5">
  <div class="font-bold text-red-900 dark:text-red-200 flex items-center justify-between flex-wrap gap-2">
    <span class="flex items-center gap-1.5 text-sm">
      <span>🚨</span> 實務關鍵痛點：向稅務局申請一定要親自去嗎？不去會怎樣？
    </span>
    <span class="text-xs px-2 py-0.5 rounded-full bg-red-200 dark:bg-red-800 text-red-800 dark:text-red-100 font-bold">
      絕不能放著不管！
    </span>
  </div>
  <div class="grid md:grid-cols-2 gap-3 text-xs md:text-sm">
    <div class="p-3 rounded-lg bg-white/90 dark:bg-slate-900/90 border border-red-200 dark:border-red-900 space-y-1">
      <strong class="text-red-700 dark:text-red-400 block">❌ 若「完全不去、也不申請」的後果：</strong>
      <ul class="list-disc list-inside text-slate-700 dark:text-slate-300 space-y-1">
        <li><strong>房屋稅自動調漲 2.5 倍：</strong> 稅捐處電腦接到通報後，若無申請人主張，會<strong>預設將全戶面積改課營業用稅率（3%）</strong>！原住家房屋稅 4,689 元可能直接暴增至 11,700 元（每年平白多繳約 7,000 元）。</li>
        <li><strong>地價稅直接暴增 5 倍：</strong> 自用住宅用地 2‰ 優惠稅率會被取消，改按一般用地稅率 <strong>10‰</strong> 課徵！</li>
        <li><strong>房地合一 400 萬免稅泡湯：</strong> 未來 6 年內若有換屋或售屋規劃，會因被掛上「營業用途」而喪失自用住宅免稅與重購退稅資格。</li>
      </ul>
    </div>
    <div class="p-3 rounded-lg bg-white/90 dark:bg-slate-900/90 border border-emerald-300 dark:border-emerald-900 space-y-1">
      <strong class="text-emerald-700 dark:text-emerald-400 block">✅ 解法：一定要親跑臨櫃嗎？（免出門線上即可辦！）</strong>
      <p class="text-slate-700 dark:text-slate-300 leading-relaxed">
        <strong>完全不用親跑稅務局！</strong> 您有兩種超省事管道：
      </p>
      <ul class="list-disc list-inside text-slate-700 dark:text-slate-300 space-y-1 pt-0.5">
        <li><strong>管道 1（手機線上辦）：</strong> 收到公文後，至「財政部稅務入口網」或「臺南市政府財政稅務局線上申辦平台」，填寫「房屋使用情形變更申報」，手機拍照上傳公文與工作桌照片，3 分鐘搞定！</li>
        <li><strong>管道 2（電話＋傳真/Email 補件）：</strong> 稅務局收到國稅局通報後，承辦人員通常會主動致電負責人手機，您只要在電話中告知「欲申請 1/6 最低營業面積或純通訊聯絡」，並依承辦人員指示傳真或 Email 申請書即完成審核。</li>
      </ul>
    </div>
  </div>
</div>

<p><strong>申請兩大節稅策略（二擇一）：</strong></p>
<ul class="list-disc list-inside space-y-1">
<li><strong>策略 A（無囤貨/純線上接案）：</strong> 主張依《財政部104年台財稅字第10400128120號令》，該址純為「通訊聯絡場所」，爭取<strong>全戶 100% 維持自住稅率（房屋稅 1.2%、地價稅 2‰）</strong>。</li>
<li><strong>策略 B（有工作桌電腦）：</strong> 申請按法定最低<strong>「實際營業面積 1/6 課徵營業用」</strong>（僅 1/6 面積課 3%，其餘 5/6 面積保留 1.2% 自住優惠）。</li>
</ul>
</div>"""

for fp in files:
    with open(fp, 'r', encoding='utf-8') as f:
        c = f.read()
    
    if '向稅務局申請一定要親自去嗎？不去會怎樣？' not in c and target_pattern in c:
        c = c.replace(target_pattern, replacement_content)
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(c)
        print("Updated successfully:", fp)
    else:
        # Try a flexible substring replacement
        anchor = 'id="step5_d"'
        if anchor in c and '向稅務局申請一定要親自去嗎？不去會怎樣？' not in c:
            start_pos = c.find('<div class="space-y-2 text-sm desc-text" id="step5_d">')
            if start_pos == -1:
                start_pos = c.find('<div class="space-y-3 text-sm desc-text" id="step5_d">')
            end_marker = '<li><strong>策略 B（有工作桌電腦）：</strong>'
            end_pos = c.find(end_marker, start_pos)
            if end_pos != -1:
                end_div = c.find('</ul>\n</div>', end_pos) + len('</ul>\n</div>')
                old_chunk = c[start_pos:end_div]
                c = c[:start_pos] + replacement_content + c[end_div:]
                with open(fp, 'w', encoding='utf-8') as f:
                    f.write(c)
                print("Flexible update successfully:", fp)

print("Batch update completed.")

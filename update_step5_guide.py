# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

def update_property_and_step5(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    # 1. Update Step 5 in Section 4 (tab-steps)
    step5_box = soup.find('h4', id='step5_t')
    if step5_box:
        step5_parent = step5_box.parent
        new_step5_content = """
            <h4 class="font-bold text-base text-slate-900 dark:text-slate-100" id="step5_t">
                向「地方稅捐處」申請自用住宅節稅（關鍵時機點：收到國稅局核准函後）
            </h4>
            <div class="space-y-2 text-sm desc-text" id="step5_d">
                <div class="p-3 rounded-lg bg-amber-50 dark:bg-amber-950/30 border border-amber-300 dark:border-amber-700 text-amber-900 dark:text-amber-200">
                    <strong>⚠️ 重大觀念澄清（千萬別搞錯時機與機關）：</strong><br>
                    • <strong>在商工一站式送件時：</strong> 無法申報房屋稅率（國稅局只管統一編號與營業稅，無權決定房屋稅率）。<br>
                    • <strong>正確時機：</strong> 國稅局審查通過並核發「稅籍登記核准公文」後，國稅局系統會<strong>自動通報「地方稅捐稽徵處」</strong>。請務必在<strong>核准後 15 天內</strong>，主動向房屋所在地的地方稅捐稽徵處送件申請！
                </div>
                <p><strong>申請兩大策略（二擇一）：</strong></p>
                <ul class="list-disc list-inside space-y-1">
                    <li><strong>策略 A（無堆貨/純線上接案）：</strong> 主張依《財政部104年台財稅字第10400128120號令》，該址純為「通訊聯絡場所」，爭取<strong>全戶 100% 維持自住稅率（房屋稅 1.2%、地價稅 2‰）</strong>。</li>
                    <li><strong>策略 B（有工作桌電腦）：</strong> 申請按法定最低<strong>「實際營業面積 1/6 課徵營業用」</strong>（僅 1/6 面積課 3%，其餘 5/6 面積保留 1.2% 自住優惠）。</li>
                </ul>
            </div>
        """
        step5_parent.clear()
        step5_parent.append(BeautifulSoup(new_step5_content, 'html.parser'))

    # 2. Enrich Chapter 3 (tab-local-taxes) with detailed Step-by-Step application guide & document checklist
    local_tax_sec = soup.find('section', id='tab-local-taxes')
    if local_tax_sec:
        # Check if detailed guide already exists, if not, append detailed practical guide
        detailed_guide_html = """
            <!-- 實務手把手：如何向地方稅捐處申請 1/6 營業面積節稅（或全戶通訊自住） -->
            <div class="p-6 rounded-xl border border-indigo-200 dark:border-indigo-900/60 bg-indigo-50/30 dark:bg-indigo-950/20 space-y-5">
                <div class="flex items-center justify-between flex-wrap gap-2">
                    <h3 class="text-lg font-bold text-indigo-900 dark:text-indigo-300 flex items-center gap-2">
                        <span>📝</span> 手把手教學：如何向地方稅捐稽徵處申辦「1/6 營業面積」或「全戶自住通訊場所」？
                    </h3>
                    <span class="px-2.5 py-1 rounded text-xs font-bold bg-indigo-100 text-indigo-800 dark:bg-indigo-900/60 dark:text-indigo-200">地方稅務局專用流程</span>
                </div>

                <div class="p-3.5 rounded-lg bg-blue-100/70 dark:bg-blue-900/40 border border-blue-300 dark:border-blue-700 text-blue-900 dark:text-blue-100 text-xs md:text-sm">
                    <strong>⏰ 申請法定黃金時間點：</strong><br>
                    <strong>「不是」在商工一站式申請！</strong> 請在收到國稅局「稅籍登記核准公文（統編已生效）」之日起 <strong>15 日內</strong>，向房屋與土地所在地的<strong>「地方稅捐稽徵處（地方稅務局）」</strong>提出。若完全沒去申請，稅捐處系統常會預設直接把全戶改課 3% 營業用！
                </div>

                <!-- 必備文件清單 -->
                <div class="space-y-2 text-sm">
                    <h4 class="font-bold text-slate-800 dark:text-slate-200">📋 必備申請文件清單（線上傳檔或臨櫃遞件）：</h4>
                    <div class="grid md:grid-cols-2 gap-3 text-xs md:text-sm">
                        <div class="p-3 rounded-lg border bg-white/70 dark:bg-slate-900/70 space-y-1" style="border-color: var(--border);">
                            <div class="font-bold text-indigo-700 dark:text-indigo-300">1. 兩份申報書（可現場填寫或線上勾選）</div>
                            <p class="desc-text">• 《房屋稅使用情形變更申報書》（載明申請 1/6 營業用或全戶通訊自住）<br>• 《地價稅自用住宅用地申請書》（申請 5/6 土地保留 2‰ 優惠稅率）</p>
                        </div>
                        <div class="p-3 rounded-lg border bg-white/70 dark:bg-slate-900/70 space-y-1" style="border-color: var(--border);">
                            <div class="font-bold text-indigo-700 dark:text-indigo-300">2. 工作室核准公文影本</div>
                            <p class="desc-text">• 縣市政府商業登記核准函影本，或國稅局稅籍登記核准函影本（證明已有合法 8 碼統編）。</p>
                        </div>
                        <div class="p-3 rounded-lg border bg-white/70 dark:bg-slate-900/70 space-y-1" style="border-color: var(--border);">
                            <div class="font-bold text-indigo-700 dark:text-indigo-300">3. 產權證明與身分證件</div>
                            <p class="desc-text">• 房屋所有權狀影本（或最新房屋稅單影本）<br>• 土地所有權狀影本<br>• 屋主身分證正反面影本 ＋ 戶口名簿影本（證明設籍自住）。</p>
                        </div>
                        <div class="p-3 rounded-lg border bg-white/70 dark:bg-slate-900/70 space-y-1" style="border-color: var(--border);">
                            <div class="font-bold text-indigo-700 dark:text-indigo-300">4. 室內平面劃分圖 ＆ 現況照片（最關鍵！）</div>
                            <p class="desc-text">• <strong>平面簡圖：</strong>手繪標記 1/6 辦公區（書房或工作桌）與 5/6 生活區（客廳、臥室、衛浴、廚房）。<br>• <strong>現況照片：</strong>提供工作桌電腦照片 ＋ 客廳房間日常生活照（證明非整層堆貨）。</p>
                        </div>
                    </div>
                </div>

                <!-- 申請管道與步驟 -->
                <div class="space-y-2 text-sm">
                    <h4 class="font-bold text-slate-800 dark:text-slate-200">🚀 具體申辦雙管道：</h4>
                    <div class="grid md:grid-cols-2 gap-3 text-xs md:text-sm">
                        <div class="p-3.5 rounded-lg border bg-white/70 dark:bg-slate-900/70 space-y-1.5" style="border-color: var(--border);">
                            <strong class="text-blue-700 dark:text-blue-400 font-bold flex items-center gap-1">💻 管道 1：線上申辦（省時留紀錄）</strong>
                            <p class="desc-text leading-relaxed">
                                1. 前往「<a href="https://www.etax.nat.gov.tw/" target="_blank" rel="noopener noreferrer" class="text-blue-600 dark:text-blue-400 underline font-medium hover:text-blue-800">財政部稅務入口網 (etax.nat.gov.tw)</a>」或房屋所在地「地方稅捐處/稅務局線上申辦系統」。<br>
                                2. 使用自然人憑證或健保卡登入。<br>
                                3. 分別點選「房屋稅使用情形變更」與「地價稅適用自用稅率」。<br>
                                4. 備註欄註記：<em>「因設立行號，申請按實際營業面積 1/6 課徵營業用，其餘 5/6 維持自住稅率」</em>（或註明符合台財稅字第10400128120號令申請全戶通訊自住），並上傳圖檔送出。
                            </p>
                        </div>
                        <div class="p-3.5 rounded-lg border bg-white/70 dark:bg-slate-900/70 space-y-1.5" style="border-color: var(--border);">
                            <strong class="text-emerald-700 dark:text-emerald-400 font-bold flex items-center gap-1">🏢 管道 2：臨櫃申辦（承辦人直接指導，最安心）</strong>
                            <p class="desc-text leading-relaxed">
                                1. 攜帶身分證、印章、權狀影本、商業登記核准函與手繪平面圖。<br>
                                2. 直接到房屋所在地之「地方稅捐稽徵處」服務櫃檯。<br>
                                3. 告知櫃檯志工或稅務員：<em>「我要辦行號設立後自住房屋 1/6 營業面積分割變更」</em>。<br>
                                4. 臨櫃承辦人員會直接核對平面圖標記比例，審查通常只需 10～15 分鐘即可完成收件。
                            </p>
                        </div>
                    </div>
                </div>

                <!-- 關鍵截止日期警語 -->
                <div class="p-3.5 rounded-lg bg-red-50 dark:bg-red-950/30 border border-red-300 dark:border-red-700 text-red-900 dark:text-red-200 text-xs md:text-sm leading-relaxed">
                    <strong>📅 攸關荷包的兩大關鍵截止日（逾期申請損失當年度優惠）：</strong><br>
                    • <strong>房屋稅：</strong> 應於每期開徵 40 日前（<strong>每年 3 月 22 日前</strong>）提出變更，當年即可適用；逾期申報自次期適用。<br>
                    • <strong>地價稅：</strong> 地價稅於 11 月開徵，必須在開徵 40 日前（<strong>每年 9 月 22 日前</strong>）提出自用住宅分割申請，當年 5/6 土地才能享受 2‰ 優惠稅率！
                </div>
            </div>
        """
        # Append inside tab-local-taxes before the last danger box
        danger_box = local_tax_sec.find('div', class_='box-danger')
        if danger_box:
            danger_box.insert_before(BeautifulSoup(detailed_guide_html, 'html.parser'))
        else:
            local_tax_sec.append(BeautifulSoup(detailed_guide_html, 'html.parser'))

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print(f"Updated {filepath} with clear 1/6 application instructions and step-by-step SOP!")

update_property_and_step5('台灣個人工作室設立與稅務全攻略_單檔分享版.html')
update_property_and_step5('工作室設立與發票報稅全攻略.html')

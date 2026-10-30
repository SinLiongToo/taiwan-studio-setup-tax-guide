# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

def enrich_step2_tax_id(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    # Find Step 2 in Chapter 4 (tab-steps)
    step2_box = soup.find('h4', id='step2_t')
    if step2_box:
        step2_parent = step2_box.parent
        new_step2_content = """
            <div class="flex items-center gap-2 flex-wrap">
                <h4 class="font-bold text-base text-blue-900 dark:text-blue-200" id="step2_t">
                    申請「商業登記 ＋ 稅籍登記」（正式取得 8 碼統一編號的關鍵步驟）
                </h4>
                <a href="https://onestop.nat.gov.tw/" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-1 text-xs font-semibold px-2.5 py-0.5 rounded-full bg-blue-200 hover:bg-blue-300 text-blue-900 dark:bg-blue-800 dark:hover:bg-blue-700 dark:text-blue-100 transition border border-blue-400">
                    🔗 登入商工一站式申辦統編 ↗
                </a>
            </div>
            
            <div class="space-y-3 text-sm leading-relaxed" id="step2_d">
                <p>
                    在台灣，個人工作室要拿到合法正式的「8 碼統一編號」，就是在這一步向<strong>「經濟部商工一站式系統」</strong>遞件。系統會一併送交<strong>「縣市政府商業處（核准商業登記並產生統編）」</strong>與<strong>「國稅局（核准稅籍身分）」</strong>：
                </p>

                <!-- 取得統編的 6 大填表與必備資料 -->
                <div class="p-4 rounded-xl bg-white/80 dark:bg-slate-900/80 border border-blue-300 dark:border-blue-800 space-y-2.5 text-xs md:text-sm">
                    <div class="font-bold text-blue-800 dark:text-blue-300 text-sm">📋 申辦統編必填欄位與準備文件（照著填即可）：</div>
                    <ul class="space-y-1.5 list-disc list-inside desc-text">
                        <li><strong>填入預查編號：</strong> 輸入步驟 1 取得的預查核准編號，系統自動帶出您的工作室名稱。</li>
                        <li><strong>負責人資料：</strong> 填寫負責人姓名、身分證字號、戶籍地址（上傳身分證正反面影本圖檔）。</li>
                        <li><strong>資本額填寫（避坑）：</strong> 填寫 <strong>新台幣 10 萬～20 萬元</strong> 即可。<br>
                            👉 <em>法規好處：資本額未達 25 萬元依法「免附銀行存款餘額證明（免驗資）」</em>，不用特地去銀行開籌備處存錢再開證明，最省事！</li>
                        <li><strong>營業地址文件（自用住宅）：</strong><br>
                            • 建物所有權狀影本（或最新一期房屋稅單影本）。<br>
                            • 建物所有權人使用同意書（房子若是自己的，自己簽同意提供設立；若是父母/配偶的，由家人簽署同意書）。</li>
                        <li><strong>勾選「併同辦理稅籍登記」（一次搞定國稅局）：</strong><br>
                            務必勾選併同辦理稅籍登記，資料會自動拋轉給國稅局稽徵所。</li>
                        <li><strong>規費繳納：</strong> 線上以信用卡或台灣 Pay 支付規費 <strong>新台幣 700 元</strong>（若臨櫃為 1,000 元）。</li>
                    </ul>
                </div>

                <!-- 稅籍種類勾選抉擇：決定是免用發票還是開發票 -->
                <div class="p-3.5 rounded-lg bg-amber-50 dark:bg-amber-950/30 border border-amber-300 dark:border-amber-700 text-amber-900 dark:text-amber-200 text-xs md:text-sm">
                    <strong>⚡ 取得統編時的「發票身分關鍵抉擇」（在此處決定）：</strong><br>
                    • <strong>想要「免稅＋免報稅」（開小規模收據）：</strong> 稅籍種類「千萬不要加註自願使用發票」，國稅局看到年收低會自動把統編核定為「免用統一發票小規模營業人」。<br>
                    • <strong>想要「開三聯式發票」（配合客戶）：</strong> 請務必在備註欄明確註記<strong>「申請自願使用統一發票」</strong>，稅務員才會准許您去領購票證買發票。
                </div>

                <div class="p-3 rounded-lg bg-emerald-100/70 dark:bg-emerald-900/40 border border-emerald-300 dark:border-emerald-700 text-emerald-900 dark:text-emerald-100 text-xs md:text-sm">
                    <strong>🎉 統編何時會正式出來？</strong><br>
                    送件後約 <strong>3～5 個工作天</strong>，縣市政府經發局/商業處審核通過，會寄發「商業登記核准函」電子公文，公文最上方就會印上您工作室的專屬 <strong>8 碼統一編號</strong>！此時您就已具備合法開立收據或簽署合約的法律身分。
                </div>
            </div>
        """
        step2_parent.clear()
        step2_parent.append(BeautifulSoup(new_step2_content, 'html.parser'))

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print(f"Updated {filepath} with comprehensive Tax ID (統編) application SOP!")

enrich_step2_tax_id('台灣個人工作室設立與稅務全攻略_單檔分享版.html')
enrich_step2_tax_id('工作室設立與發票報稅全攻略.html')

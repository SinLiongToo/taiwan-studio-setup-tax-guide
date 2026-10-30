# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

def enrich_step3_official_doc(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    # Find Step 3 in Chapter 4 (tab-steps)
    step3_box = soup.find('h4', id='step3_t')
    if step3_box:
        step3_parent = step3_box.parent
        new_step3_content = """
            <h4 class="font-bold text-base text-slate-900 dark:text-slate-100" id="step3_t">
                會收到什麼公文？收到後何時去國稅局？（紙本公文 vs. 電子公文全解析）
            </h4>
            
            <div class="space-y-3 text-sm leading-relaxed" id="step3_d">
                <p>
                    送出商工一站式申請後，很多人會問：「我真的會收到實體紙本公文嗎？是用寄的還是 Email？」答案是：<strong>您一共會收到「兩份」正式公文！</strong>
                </p>

                <!-- 兩份公文型態解析 -->
                <div class="grid md:grid-cols-2 gap-3 text-xs md:text-sm">
                    <div class="p-3.5 rounded-lg border bg-white/80 dark:bg-slate-900/80 border-blue-200 dark:border-blue-900/60 space-y-1.5">
                        <div class="font-bold text-blue-700 dark:text-blue-300 flex items-center gap-1">
                            <span>📄</span> 第一份：縣市政府「商業登記核准函」
                        </div>
                        <ul class="list-disc list-inside desc-text space-y-1">
                            <li><strong>發文機關：</strong> 縣市政府經濟發展局 / 商業處。</li>
                            <li><strong>送達方式：</strong> 若線上申辦，可直接在「商工一站式」下載<strong>「電子核准公文（PDF）」</strong>；同時也會以<strong>「掛號郵寄紙本公文」</strong>寄到您的營業地址或戶籍地址。</li>
                            <li><strong>關鍵內容：</strong> 載明您的工作室名稱、負責人姓名、資本額，以及最核心的<strong>「8 碼統一編號」</strong>！</li>
                        </ul>
                    </div>

                    <div class="p-3.5 rounded-lg border bg-white/80 dark:bg-slate-900/80 border-emerald-200 dark:border-emerald-900/60 space-y-1.5">
                        <div class="font-bold text-emerald-700 dark:text-emerald-300 flex items-center gap-1">
                            <span>🏛️</span> 第二份：國稅局「稅籍登記核准公文」
                        </div>
                        <ul class="list-disc list-inside desc-text space-y-1">
                            <li><strong>發文機關：</strong> 營業地址管轄的國稅局分局或稽徵所。</li>
                            <li><strong>送達方式：</strong> 縣市商業處核准後會把資料轉給國稅局，國稅局審查約 2～4 天後，以<strong>「實體掛號信」</strong>郵寄到您的通訊地址。</li>
                            <li><strong>關鍵內容：</strong> 核定您的稅籍身分（是「免用發票」還是「使用發票」），並通知您至國稅局辦理後續手續。</li>
                        </ul>
                    </div>
                </div>

                <!-- 依路線劃分去國稅局的動作 -->
                <div class="p-4 rounded-xl bg-amber-50 dark:bg-amber-950/30 border border-amber-300 dark:border-amber-700 text-amber-900 dark:text-amber-200 space-y-2 text-xs md:text-sm">
                    <strong class="font-bold text-sm block">💡 收到國稅局公文後，一定要親自跑一趟國稅局嗎？（路線不同差別極大）</strong>
                    
                    <div class="grid md:grid-cols-2 gap-3 pt-1">
                        <div class="p-2.5 rounded bg-white/70 dark:bg-slate-900/70 border border-amber-200 dark:border-amber-900">
                            <span class="font-bold text-emerald-700 dark:text-emerald-300">🟢 路線 A：免用統一發票（最輕鬆）</span>
                            <p class="desc-text mt-1">國稅局公文若註明「核定免用統一發票」，且無特別要求面談：<br>
                            👉 <strong>很多分局甚至完全不用去現場！</strong> 稅籍自動生效，您刻好「免用發票專用章」就能開始對外營業開收據了。</p>
                        </div>

                        <div class="p-2.5 rounded bg-white/70 dark:bg-slate-900/70 border border-amber-200 dark:border-amber-900">
                            <span class="font-bold text-blue-700 dark:text-blue-300">🔵 路線 B：使用統一發票（必須親自跑一趟）</span>
                            <p class="desc-text mt-1">依營業稅法規定，初次使用統一發票的負責人<strong>必須本人親自到國稅局現場核驗身分</strong>：<br>
                            👉 帶<strong>負責人身分證正本、大小章、縣市政府商業登記核准函</strong>，在稅籍卡親筆簽名，現場領取一本硬紙卡的<strong>「統一發票購票證」</strong>，才能去農會買手寫發票。</p>
                        </div>
                    </div>
                </div>
            </div>
        """
        step3_parent.clear()
        step3_parent.append(BeautifulSoup(new_step3_content, 'html.parser'))

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print(f"Updated {filepath} with Official Document & Tax Bureau Visit details!")

enrich_step3_official_doc('台灣個人工作室設立與稅務全攻略_單檔分享版.html')
enrich_step3_official_doc('工作室設立與發票報稅全攻略.html')

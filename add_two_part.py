# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

def add_two_part_invoice(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    # Find the real-images container (inside chap-receipts)
    real_images_sec = soup.find('section', id='tab-real-images')
    receipt_types_sec = soup.find('section', id='tab-receipt-types')

    # 1. Add authentic 1:1 Two-part invoice simulation to tab-real-images
    two_part_bill_html = """
            <!-- 圖鑑 ④: 二聯式統一發票 (B2C 個人專用) -->
            <div class="space-y-3 pt-6 border-t" style="border-color: var(--border);">
                <div class="flex items-center justify-between">
                    <h3 class="font-bold text-base md:text-lg flex items-center gap-2 text-rose-800 dark:text-rose-400">
                        <span>圖鑑 ④</span> 二聯式統一發票（B2C 專用：開給一般個人、無統編買家）
                    </h3>
                    <span class="px-2.5 py-1 rounded text-xs font-bold bg-rose-100 text-rose-800 dark:bg-rose-900/50 dark:text-rose-300">開給自然人個人專用</span>
                </div>

                <div class="real-bill-wrap p-6 md:p-8 text-xs md:text-sm" style="background-color: #fff1f2; color: #881337; font-family: 'MingLiU', 'Courier New', monospace; border: 2px solid #e11d48;">
                    <div class="watermark-text" style="color: rgba(225, 29, 72, 0.08);">統一發票二聯式</div>
                    
                    <div class="flex justify-between items-start mb-3 border-b-2 border-rose-700 pb-2">
                        <div>
                            <div class="text-xl md:text-2xl font-black text-rose-950 tracking-wider">統一發票（二聯式）</div>
                            <div class="text-xs font-bold text-rose-700 mt-0.5">中華民國 115 年 09 - 10 月份 ｜ 【第二聯：收執聯】</div>
                        </div>
                        <div class="text-right">
                            <div class="text-base md:text-lg font-mono font-black text-red-600 tracking-wider">字軌號碼：BB-66778899</div>
                            <div class="text-xs text-rose-700">開立日期：115 年 10 月 20 日</div>
                        </div>
                    </div>

                    <div class="mb-3 bg-white/70 p-2.5 rounded border border-rose-300">
                        <div><strong class="text-rose-900">買受人：</strong> 陳大華 先生/女士 <span class="text-xs text-rose-600 ml-2">（※ 個人買家依法免填身分證字號與統編）</span></div>
                    </div>

                    <!-- 二聯式發票明細表格 (特色：內含5%營業稅，不拆分未稅與稅額) -->
                    <table class="w-full text-center border-collapse border border-rose-500 bg-white/80 mb-3">
                        <thead>
                            <tr class="bg-rose-100 text-rose-950 font-bold">
                                <th class="border border-rose-400 p-2">品名</th>
                                <th class="border border-rose-400 p-2 w-14">數量</th>
                                <th class="border border-rose-400 p-2 w-28">單價（含稅）</th>
                                <th class="border border-rose-400 p-2 w-32">金額（含稅）</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td class="border border-rose-300 p-2 text-left">客製手作藝文陶藝品 / 個人顧問諮詢</td>
                                <td class="border border-rose-300 p-2 font-mono">1</td>
                                <td class="border border-rose-300 p-2 font-mono">10,500</td>
                                <td class="border border-rose-300 p-2 font-mono font-bold">10,500</td>
                            </tr>
                            <tr>
                                <td class="border border-rose-300 p-2 text-gray-400">以下空白</td>
                                <td class="border border-rose-300 p-2"></td>
                                <td class="border border-rose-300 p-2"></td>
                                <td class="border border-rose-300 p-2"></td>
                            </tr>
                        </tbody>
                    </table>

                    <!-- 金額總計區 (二聯式最大特色：只有總計，稅額已內含) -->
                    <div class="border border-rose-600 bg-rose-50/70 p-3 mb-3 text-xs md:text-sm">
                        <div class="flex justify-between items-center font-bold text-rose-950">
                            <span>總計新台幣（中文大寫）：<strong class="text-sm md:text-base ml-2">壹萬零伍佰 元整</strong></span>
                            <span class="font-mono font-black text-lg text-rose-950">NT$ 10,500</span>
                        </div>
                        <div class="text-[11px] text-rose-700 mt-1">※ 依營業稅法規定，二聯式發票金額一律為「內含 5% 營業稅」，申報 401 時系統會自動換算銷售額（10,500 ÷ 1.05 = 10,000，稅額 500 元）。</div>
                    </div>

                    <!-- 底部印章與分聯說明 -->
                    <div class="flex justify-between items-end">
                        <div class="text-[11px] text-rose-800 leading-relaxed font-sans">
                            注意：<br>
                            1. 金額大寫塗改者無效。<br>
                            2. 只有兩聯：第一聯【存根聯】自己留存5年；第二聯【收執聯】交給消費者對獎。<br>
                            3. 個人消費者可憑收執聯兌領每期統一發票千萬元中獎獎金！
                        </div>
                        <div class="flex items-center gap-2">
                            <div class="red-seal-box p-2 text-xs w-48">
                                <div class="text-[11px] font-bold">極客軟體工程行</div>
                                <div class="text-[10px] font-mono">統一編號：99887766</div>
                                <div class="text-[9px]">負責人：林大偉 ｜ 02-23456789</div>
                                <div class="text-[9px]">新北市板橋區縣民大道二段</div>
                                <div class="text-[10px] border-t border-red-500 mt-0.5 pt-0.5 tracking-wider font-bold">統一發票專用章 (1)</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
    """

    if real_images_sec:
        two_part_soup = BeautifulSoup(two_part_bill_html, 'html.parser')
        real_images_sec.append(two_part_soup)

    # 2. Add Explanation & Comparison Table in tab-receipt-types
    two_vs_three_table_html = """
            <!-- 二聯式 vs 三聯式 深度比較區塊 -->
            <div class="p-6 rounded-xl border border-rose-200 dark:border-rose-900/60 bg-rose-50/30 dark:bg-rose-950/20 space-y-4">
                <h3 class="text-lg font-bold text-rose-900 dark:text-rose-300 flex items-center gap-2">
                    <span>💡</span> 深度解析：什麼時候開「二聯式」？什麼時候開「三聯式」？
                </h3>
                <p class="text-sm desc-text leading-relaxed">
                    只要您是核准「使用統一發票」的工作室，國稅局代售點買到的發票本通常分為兩種本子：<strong>【二聯式發票本】</strong> 與 <strong>【三聯式發票本】</strong>。兩者核心差異如下：
                </p>

                <div class="overflow-x-auto">
                    <table class="w-full text-sm border-collapse">
                        <thead>
                            <tr class="bg-slate-100 dark:bg-slate-800 text-slate-800 dark:text-slate-100">
                                <th class="p-3 border text-left font-bold" style="border-color: var(--border);">比較項目</th>
                                <th class="p-3 border text-left font-bold text-rose-700 dark:text-rose-400" style="border-color: var(--border);">二聯式統一發票 (B2C)</th>
                                <th class="p-3 border text-left font-bold text-emerald-700 dark:text-emerald-400" style="border-color: var(--border);">三聯式統一發票 (B2B)</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td class="p-3 border font-semibold" style="border-color: var(--border);">開立對象</td>
                                <td class="p-3 border font-bold text-rose-700 dark:text-rose-400" style="border-color: var(--border);">一般個人自然人、無統編之買家</td>
                                <td class="p-3 border font-bold text-emerald-700 dark:text-emerald-400" style="border-color: var(--border);">公司、行號、具統編之機關團體</td>
                            </tr>
                            <tr>
                                <td class="p-3 border font-semibold" style="border-color: var(--border);">總共有幾聯？</td>
                                <td class="p-3 border" style="border-color: var(--border);"><strong>只有 2 聯</strong>（存根聯、收執聯）</td>
                                <td class="p-3 border" style="border-color: var(--border);"><strong>共有 3 聯</strong>（存根聯、扣抵聯、收執聯）</td>
                            </tr>
                            <tr>
                                <td class="p-3 border font-semibold" style="border-color: var(--border);">5% 營業稅寫法</td>
                                <td class="p-3 border font-bold" style="border-color: var(--border);"><strong>內含稅！</strong>不單獨寫稅額，直接寫含稅總價（例如直接寫 10,500）</td>
                                <td class="p-3 border font-bold" style="border-color: var(--border);"><strong>外加拆開！</strong>清楚拆分「未稅 10,000」與「稅額 500」</td>
                            </tr>
                            <tr>
                                <td class="p-3 border font-semibold" style="border-color: var(--border);">買家能不能扣抵稅額？</td>
                                <td class="p-3 border" style="border-color: var(--border);">❌ 不能（個人沒有營業稅可抵）</td>
                                <td class="p-3 border text-emerald-700 dark:text-emerald-400 font-bold" style="border-color: var(--border);">✅ 可以（憑第二聯扣抵 5% 銷項稅額）</td>
                            </tr>
                            <tr>
                                <td class="p-3 border font-semibold" style="border-color: var(--border);">買家能不能對獎？</td>
                                <td class="p-3 border text-emerald-700 dark:text-emerald-400 font-bold" style="border-color: var(--border);">✅ 可以！個人憑發票號碼對統一發票千萬大獎</td>
                                <td class="p-3 border text-red-600 dark:text-red-400" style="border-color: var(--border);">❌ 載有買受人統編之發票依法不得領獎</td>
                            </tr>
                            <tr>
                                <td class="p-3 border font-semibold" style="border-color: var(--border);">401 申報填哪裡？</td>
                                <td class="p-3 border font-mono" style="border-color: var(--border);">格式代號 32（二聯式收銀機或手寫）</td>
                                <td class="p-3 border font-mono" style="border-color: var(--border);">格式代號 31（三聯式統一發票）</td>
                            </tr>
                        </tbody>
                    </table>
                </div>

                <div class="p-4 rounded-lg bg-amber-50 dark:bg-amber-950/40 border border-amber-300 dark:border-amber-700 text-amber-900 dark:text-amber-200 text-xs md:text-sm">
                    <strong>⚠️ 實務小常識：個人買家突然說「我也要報帳」怎麼辦？</strong><br>
                    若個人買家代表公司採購，開票時就不能開二聯式，必須直接開「三聯式統一發票」並打上該公司的 8 碼統編；若手邊剛好沒有三聯式發票本，二聯式發票亦可在買受人欄位備註客戶統編，但申報時會計處理較為繁瑣，因此一般習慣<strong>「對個人開二聯、對公司開三聯」</strong>最標準合規！
                </div>
            </div>
    """

    if receipt_types_sec:
        comp_soup = BeautifulSoup(two_vs_three_table_html, 'html.parser')
        receipt_types_sec.append(comp_soup)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print(f"Updated {filepath} with Two-Part Invoice section and comparison table!")

add_two_part_invoice('台灣個人工作室設立與稅務全攻略_單檔分享版.html')
add_two_part_invoice('工作室設立與發票報稅全攻略.html')

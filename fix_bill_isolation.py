# -*- coding: utf-8 -*-
import glob

files = glob.glob('*.html')
print("Found files:", files)

bill_isolation_css = """
        /* =========================================================
           AUTHENTIC PAPER BILL ISOLATION (IMMUNE TO DARK THEME)
           Physical simulation receipts must keep their real physical paper
           colors (white paper, light green invoice paper, carbon copy, etc.)
           with pitch black ink regardless of theme!
           ========================================================= */
        .real-bill-wrap,
        .paper-salary,
        .paper-receipt,
        .paper-invoice,
        .paper-b2c,
        html.dark .real-bill-wrap,
        html.dark .paper-salary,
        html.dark .paper-receipt,
        html.dark .paper-invoice,
        html.dark .paper-b2c,
        [data-theme="dark"] .real-bill-wrap,
        [data-theme="dark"] .paper-salary,
        [data-theme="dark"] .paper-receipt,
        [data-theme="dark"] .paper-invoice,
        [data-theme="dark"] .paper-b2c {
            box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.4), 0 8px 10px -6px rgba(0, 0, 0, 0.3) !important;
        }

        /* 1. Salary / Compensation Slip (勞務報酬單) - Pure White Physical Paper */
        .paper-salary,
        html.dark .paper-salary,
        [data-theme="dark"] .paper-salary {
            background-color: #ffffff !important;
            color: #111827 !important;
        }
        .paper-salary *,
        html.dark .paper-salary *,
        [data-theme="dark"] .paper-salary * {
            color: #111827;
        }
        .paper-salary th,
        html.dark .paper-salary th,
        [data-theme="dark"] .paper-salary th {
            background-color: #f3f4f6 !important;
            color: #111827 !important;
            border-color: #d1d5db !important;
        }
        .paper-salary td,
        html.dark .paper-salary td,
        [data-theme="dark"] .paper-salary td {
            background-color: #ffffff !important;
            color: #111827 !important;
            border-color: #d1d5db !important;
        }

        /* 2. Small Scale Receipt (免用統一發票收據) - Classic Red Border Bill */
        .paper-receipt,
        html.dark .paper-receipt,
        [data-theme="dark"] .paper-receipt {
            background-color: #fffbf5 !important;
            color: #1c1917 !important;
        }
        .paper-receipt *,
        html.dark .paper-receipt *,
        [data-theme="dark"] .paper-receipt * {
            color: #1c1917;
        }
        .paper-receipt .bg-white\\/70,
        .paper-receipt .bg-white\\/80,
        html.dark .paper-receipt .bg-white\\/70,
        html.dark .paper-receipt .bg-white\\/80,
        [data-theme="dark"] .paper-receipt .bg-white\\/70,
        [data-theme="dark"] .paper-receipt .bg-white\\/80 {
            background-color: #ffffff !important;
            color: #1c1917 !important;
        }
        .paper-receipt th,
        html.dark .paper-receipt th,
        [data-theme="dark"] .paper-receipt th {
            background-color: #fef2f2 !important;
            color: #991b1b !important;
        }
        .paper-receipt td,
        html.dark .paper-receipt td,
        [data-theme="dark"] .paper-receipt td {
            background-color: #ffffff !important;
            color: #1c1917 !important;
        }

        /* 3. Triplicate Invoice (三聯式統一發票) - Light Green Bank Carbon Paper */
        .paper-invoice,
        html.dark .paper-invoice,
        [data-theme="dark"] .paper-invoice {
            background-color: #f0fdf4 !important;
            color: #064e3b !important;
        }
        .paper-invoice *,
        html.dark .paper-invoice *,
        [data-theme="dark"] .paper-invoice * {
            color: #064e3b;
        }
        .paper-invoice .bg-white\\/60,
        .paper-invoice .bg-white\\/80,
        .paper-invoice div.rounded,
        html.dark .paper-invoice .bg-white\\/60,
        html.dark .paper-invoice .bg-white\\/80,
        html.dark .paper-invoice div.rounded,
        [data-theme="dark"] .paper-invoice .bg-white\\/60,
        [data-theme="dark"] .paper-invoice .bg-white\\/80,
        [data-theme="dark"] .paper-invoice div.rounded {
            background-color: #ffffff !important;
            color: #064e3b !important;
            border-color: #86efac !important;
        }
        .paper-invoice strong,
        html.dark .paper-invoice strong,
        [data-theme="dark"] .paper-invoice strong {
            color: #064e3b !important;
        }
        .paper-invoice span.font-mono,
        html.dark .paper-invoice span.font-mono,
        [data-theme="dark"] .paper-invoice span.font-mono {
            color: #022c22 !important;
        }
        .paper-invoice table,
        html.dark .paper-invoice table,
        [data-theme="dark"] .paper-invoice table {
            background-color: #ffffff !important;
            border-color: #10b981 !important;
        }
        .paper-invoice th,
        html.dark .paper-invoice th,
        [data-theme="dark"] .paper-invoice th {
            background-color: #dcfce7 !important;
            color: #064e3b !important;
            border-color: #86efac !important;
        }
        .paper-invoice td,
        html.dark .paper-invoice td,
        [data-theme="dark"] .paper-invoice td {
            background-color: #ffffff !important;
            color: #0f172a !important;
            border-color: #86efac !important;
        }
        .paper-invoice .text-red-600,
        html.dark .paper-invoice .text-red-600,
        [data-theme="dark"] .paper-invoice .text-red-600 {
            color: #dc2626 !important;
        }

        /* 4. Duplicate Invoice (二聯式統一發票) - Light Blue/Sky Paper */
        .paper-b2c,
        html.dark .paper-b2c,
        [data-theme="dark"] .paper-b2c {
            background-color: #f0f9ff !important;
            color: #0c4a6e !important;
        }
        .paper-b2c *,
        html.dark .paper-b2c *,
        [data-theme="dark"] .paper-b2c * {
            color: #0c4a6e;
        }
        .paper-b2c .bg-white\\/70,
        .paper-b2c .bg-white\\/80,
        .paper-b2c div.rounded,
        html.dark .paper-b2c .bg-white\\/70,
        html.dark .paper-b2c .bg-white\\/80,
        html.dark .paper-b2c div.rounded,
        [data-theme="dark"] .paper-b2c .bg-white\\/70,
        [data-theme="dark"] .paper-b2c .bg-white\\/80,
        [data-theme="dark"] .paper-b2c div.rounded {
            background-color: #ffffff !important;
            color: #0c4a6e !important;
            border-color: #7dd3fc !important;
        }
        .paper-b2c th,
        html.dark .paper-b2c th,
        [data-theme="dark"] .paper-b2c th {
            background-color: #e0f2fe !important;
            color: #0369a1 !important;
            border-color: #7dd3fc !important;
        }
        .paper-b2c td,
        html.dark .paper-b2c td,
        [data-theme="dark"] .paper-b2c td {
            background-color: #ffffff !important;
            color: #0f172a !important;
            border-color: #7dd3fc !important;
        }
        .paper-b2c .text-red-600,
        html.dark .paper-b2c .text-red-600,
        [data-theme="dark"] .paper-b2c .text-red-600 {
            color: #dc2626 !important;
        }
"""

for fp in files:
    with open(fp, 'r', encoding='utf-8') as f:
        c = f.read()
    
    if '/* AUTHENTIC PAPER BILL ISOLATION' not in c:
        c = c.replace('</style>', bill_isolation_css + '\n</style>')
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(c)
        print("Injected Bill Isolation CSS to:", fp)

print("Done!")

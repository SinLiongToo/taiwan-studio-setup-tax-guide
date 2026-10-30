# -*- coding: utf-8 -*-
import glob

files = glob.glob('*.html')
print("Found files:", files)

dark_override_css = """
        /* =========================================================
           STRICT GENERATIVE UI DARK MODE OVERRIDES (HIGH CONTRAST)
           ========================================================= */
        html.dark, [data-theme="dark"] {
            --bg-body: #0b0f19 !important;
            --bg-card: #111827 !important;
            --text-main: #f9fafb !important;
            --text-muted: #cbd5e1 !important;
            --border: #374151 !important;
            --primary: #60a5fa !important;
            --badge-bg: #1f2937 !important;
            --code-bg: #030712 !important;
        }

        /* Enforce pure dark surface on all card containers & sub-boxes in Dark Mode */
        html.dark .card-custom, [data-theme="dark"] .card-custom {
            background-color: #111827 !important;
            border-color: #374151 !important;
            color: #f9fafb !important;
        }

        /* Fix all nested cards that previously had bg-white/80 or bg-white */
        html.dark .bg-white,
        html.dark .bg-white\\/60,
        html.dark .bg-white\\/70,
        html.dark .bg-white\\/80,
        html.dark .bg-white\\/90,
        [data-theme="dark"] .bg-white,
        [data-theme="dark"] .bg-white\\/60,
        [data-theme="dark"] .bg-white\\/70,
        [data-theme="dark"] .bg-white\\/80,
        [data-theme="dark"] .bg-white\\/90 {
            background-color: #1f2937 !important;
            border-color: #374151 !important;
            color: #f3f4f6 !important;
        }

        /* Fix text contrast inside cards */
        html.dark .desc-text,
        [data-theme="dark"] .desc-text {
            color: #d1d5db !important;
        }
        
        html.dark .desc-text strong,
        [data-theme="dark"] .desc-text strong {
            color: #ffffff !important;
        }

        html.dark .desc-text li,
        [data-theme="dark"] .desc-text li {
            color: #e5e7eb !important;
        }

        /* Information & Callout Boxes High-Contrast Dark Overrides */
        html.dark .box-info, [data-theme="dark"] .box-info {
            background-color: #172554 !important;
            border-color: #2563eb !important;
            color: #dbeafe !important;
        }
        html.dark .box-info strong, [data-theme="dark"] .box-info strong {
            color: #ffffff !important;
        }

        html.dark .box-success, [data-theme="dark"] .box-success {
            background-color: #064e3b !important;
            border-color: #059669 !important;
            color: #d1fae5 !important;
        }
        html.dark .box-success strong, [data-theme="dark"] .box-success strong {
            color: #ffffff !important;
        }

        html.dark .box-warning, [data-theme="dark"] .box-warning {
            background-color: #451a03 !important;
            border-color: #d97706 !important;
            color: #fef3c7 !important;
        }
        html.dark .box-warning strong, [data-theme="dark"] .box-warning strong {
            color: #ffffff !important;
        }

        html.dark .border-emerald-500, [data-theme="dark"] .border-emerald-500 {
            background-color: #064e3b33 !important;
            border-color: #10b981 !important;
        }

        html.dark .border-blue-500, [data-theme="dark"] .border-blue-500 {
            background-color: #1e3a8a33 !important;
            border-color: #3b82f6 !important;
        }

        html.dark .border-indigo-500, [data-theme="dark"] .border-indigo-500 {
            background-color: #312e8133 !important;
            border-color: #6366f1 !important;
        }

        /* Ensure list markers and texts are crisp and bright */
        html.dark ul, html.dark ol, [data-theme="dark"] ul, [data-theme="dark"] ol {
            color: #e5e7eb;
        }
"""

for fp in files:
    with open(fp, 'r', encoding='utf-8') as f:
        c = f.read()

    # Insert dark mode overrides into <style>
    style_end = '</style>'
    if '/* STRICT GENERATIVE UI DARK MODE OVERRIDES' not in c:
        c = c.replace(style_end, dark_override_css + '\n' + style_end)
        print("Injected CSS into:", fp)

    with open(fp, 'w', encoding='utf-8') as f:
        f.write(c)

print("Injected successfully!")

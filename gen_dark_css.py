# -*- coding: utf-8 -*-
with open('classes_used.txt', 'r', encoding='utf-8') as f:
    classes = [l.strip() for l in f if l.strip().startswith('dark:')]

css_lines = []
css_lines.append("/* GENERATED COMPLETE TAILWIND DARK MODE UTILITIES */")

for c in classes:
    prop = c[5:] # remove dark:
    # Escape colon and slash for CSS selector
    escaped_sel = "html.dark ." + "dark\\:" + prop.replace('/', '\\/').replace('[', '\\[').replace(']', '\\]')
    escaped_sel_data = "[data-theme=\"dark\"] ." + "dark\\:" + prop.replace('/', '\\/').replace('[', '\\[').replace(']', '\\]')
    
    val = ""
    # Background colors
    if prop == "bg-amber-900/60": val = "background-color: rgba(120, 53, 15, 0.6) !important;"
    elif prop == "bg-amber-950/30": val = "background-color: rgba(69, 26, 3, 0.4) !important;"
    elif prop == "bg-amber-950/40": val = "background-color: rgba(69, 26, 3, 0.5) !important;"
    elif prop == "bg-blue-800": val = "background-color: #1e40af !important;"
    elif prop == "bg-blue-900": val = "background-color: #1e3a8a !important;"
    elif prop == "bg-blue-900/40": val = "background-color: rgba(30, 58, 138, 0.4) !important;"
    elif prop == "bg-blue-900/50": val = "background-color: rgba(30, 58, 138, 0.5) !important;"
    elif prop == "bg-blue-900/60": val = "background-color: rgba(30, 58, 138, 0.6) !important;"
    elif prop == "bg-blue-950/50": val = "background-color: rgba(23, 37, 84, 0.5) !important;"
    elif prop == "bg-emerald-900": val = "background-color: #064e3b !important;"
    elif prop == "bg-emerald-900/40": val = "background-color: rgba(6, 78, 59, 0.4) !important;"
    elif prop == "bg-emerald-900/50": val = "background-color: rgba(6, 78, 59, 0.5) !important;"
    elif prop == "bg-emerald-900/60": val = "background-color: rgba(6, 78, 59, 0.6) !important;"
    elif prop == "bg-emerald-950/50": val = "background-color: rgba(2, 44, 34, 0.5) !important;"
    elif prop == "bg-indigo-800": val = "background-color: #3730a3 !important;"
    elif prop == "bg-indigo-900/60": val = "background-color: rgba(49, 46, 129, 0.6) !important;"
    elif prop == "bg-indigo-950/20": val = "background-color: rgba(30, 27, 75, 0.3) !important;"
    elif prop == "bg-indigo-950/30": val = "background-color: rgba(30, 27, 75, 0.4) !important;"
    elif prop == "bg-purple-900/60": val = "background-color: rgba(88, 28, 135, 0.6) !important;"
    elif prop == "bg-red-800": val = "background-color: #991b1b !important;"
    elif prop == "bg-red-900/40": val = "background-color: rgba(127, 29, 29, 0.4) !important;"
    elif prop == "bg-red-900/60": val = "background-color: rgba(127, 29, 29, 0.6) !important;"
    elif prop == "bg-red-950/20": val = "background-color: rgba(69, 10, 10, 0.3) !important;"
    elif prop == "bg-red-950/30": val = "background-color: rgba(69, 10, 10, 0.4) !important;"
    elif prop == "bg-rose-900/50": val = "background-color: rgba(136, 19, 55, 0.5) !important;"
    elif prop == "bg-rose-950/20": val = "background-color: rgba(76, 5, 25, 0.3) !important;"
    elif prop == "bg-sky-900/50": val = "background-color: rgba(12, 74, 110, 0.5) !important;"
    elif prop == "bg-slate-800": val = "background-color: #1e293b !important;"
    elif prop == "bg-slate-900": val = "background-color: #0f172a !important;"
    elif prop == "bg-slate-900/70": val = "background-color: rgba(15, 23, 42, 0.7) !important;"
    elif prop == "bg-slate-900/80": val = "background-color: rgba(15, 23, 42, 0.8) !important;"
    elif prop == "bg-slate-900/90": val = "background-color: rgba(15, 23, 42, 0.9) !important;"
    # Border colors
    elif prop == "border-amber-700": val = "border-color: #b45309 !important;"
    elif prop == "border-amber-900": val = "border-color: #78350f !important;"
    elif prop == "border-blue-700": val = "border-color: #1d4ed8 !important;"
    elif prop == "border-blue-800": val = "border-color: #1e40af !important;"
    elif prop == "border-blue-900/60": val = "border-color: rgba(30, 58, 138, 0.6) !important;"
    elif prop == "border-emerald-700": val = "border-color: #047857 !important;"
    elif prop == "border-emerald-900": val = "border-color: #064e3b !important;"
    elif prop == "border-emerald-900/60": val = "border-color: rgba(6, 78, 59, 0.6) !important;"
    elif prop == "border-indigo-900/60": val = "border-color: rgba(49, 46, 129, 0.6) !important;"
    elif prop == "border-red-700": val = "border-color: #b91c1c !important;"
    elif prop == "border-red-900": val = "border-color: #7f1d1d !important;"
    elif prop == "border-rose-900/60": val = "border-color: rgba(136, 19, 55, 0.6) !important;"
    elif prop == "border-slate-700/60": val = "border-color: rgba(51, 65, 85, 0.6) !important;"
    # Text colors
    elif prop == "text-amber-200": val = "color: #fde68a !important;"
    elif prop == "text-amber-400": val = "color: #fbbf24 !important;"
    elif prop == "text-blue-100": val = "color: #dbeafe !important;"
    elif prop == "text-blue-200": val = "color: #bfdbfe !important;"
    elif prop == "text-blue-300": val = "color: #93c5fd !important;"
    elif prop == "text-blue-400": val = "color: #60a5fa !important;"
    elif prop == "text-emerald-100": val = "color: #d1fae5 !important;"
    elif prop == "text-emerald-200": val = "color: #a7f3d0 !important;"
    elif prop == "text-emerald-300": val = "color: #6ee7b7 !important;"
    elif prop == "text-emerald-400": val = "color: #34d399 !important;"
    elif prop == "text-indigo-200": val = "color: #c7d2fe !important;"
    elif prop == "text-indigo-300": val = "color: #a5b4fc !important;"
    elif prop == "text-indigo-400": val = "color: #818cf8 !important;"
    elif prop == "text-purple-400": val = "color: #c084fc !important;"
    elif prop == "text-red-100": val = "color: #fee2e2 !important;"
    elif prop == "text-red-200": val = "color: #fecaca !important;"
    elif prop == "text-red-300": val = "color: #fca5a5 !important;"
    elif prop == "text-red-400": val = "color: #f87171 !important;"
    elif prop == "text-rose-300": val = "color: #fda4af !important;"
    elif prop == "text-rose-400": val = "color: #fb7185 !important;"
    elif prop == "text-sky-300": val = "color: #7dd3fc !important;"
    elif prop == "text-sky-400": val = "color: #38bdf8 !important;"
    elif prop == "text-slate-100": val = "color: #f1f5f9 !important;"
    elif prop == "text-slate-200": val = "color: #e2e8f0 !important;"
    elif prop == "text-slate-300": val = "color: #cbd5e1 !important;"
    elif prop == "text-slate-400": val = "color: #94a3b8 !important;"
    elif prop == "hover:bg-blue-700": val = "" # skip hover
    elif prop == "hover:bg-blue-800": val = "" # skip hover
    
    if val:
        css_lines.append(f"{escaped_sel}, {escaped_sel_data} {{ {val} }}")

generated_css = "\n".join(css_lines)
with open("dark_utilities.css", "w", encoding="utf-8") as f:
    f.write(generated_css)
print("Generated dark_utilities.css with", len(css_lines), "rules.")

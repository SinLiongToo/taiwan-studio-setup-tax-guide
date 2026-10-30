# -*- coding: utf-8 -*-
import glob

with open('dark_utilities.css', 'r', encoding='utf-8') as f:
    dark_css = f.read()

files = glob.glob('*.html')
for fp in files:
    with open(fp, 'r', encoding='utf-8') as f:
        c = f.read()
    
    if '/* GENERATED COMPLETE TAILWIND DARK MODE UTILITIES */' not in c:
        c = c.replace('</style>', dark_css + '\n</style>')
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(c)
        print("Embedded dark mode utilities into:", fp)

print("All files updated!")

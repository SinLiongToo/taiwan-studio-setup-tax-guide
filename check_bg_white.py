# -*- coding: utf-8 -*-
import glob, re

f = glob.glob('*分享版.html')[0]
c = open(f, 'r', encoding='utf-8').read()

# Let's find every occurrence of bg-white, bg-slate, bg-emerald-50, bg-blue-50, etc. that doesn't have dark: counterpart or uses bad contrast in dark mode
matches = re.findall(r'class="[^"]*bg-white[^"]*"', c)
print("bg-white count:", len(matches))
for m in set(matches):
    print(" ", m)

matches_desc = re.findall(r'class="[^"]*desc-text[^"]*"', c)
print("desc-text count:", len(matches_desc))

# -*- coding: utf-8 -*-
import glob

f = glob.glob('*分享版.html')[0]
c = open(f, 'r', encoding='utf-8').read()

print("theme toggle search:")
pos = c.find('btn-theme')
print("btn-theme:", pos)
if pos == -1:
    pos = c.find('theme')
    while pos != -1 and pos < len(c):
        print("theme occurrence:", pos, repr(c[pos-20:pos+50]))
        pos = c.find('theme', pos+5)
        if pos > 490000:
            break

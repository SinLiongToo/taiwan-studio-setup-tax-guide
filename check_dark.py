# -*- coding: utf-8 -*-
import glob

f = glob.glob('*分享版.html')[0]
c = open(f, 'r', encoding='utf-8').read()

print("theme buttons or scripts:")
pos = c.find('theme-toggle')
if pos != -1:
    print(c[pos-100:pos+300])
else:
    pos2 = c.find('dark')
    print("first 5 dark mentions:")
    for i in range(5):
        p = c.find('dark', pos2)
        print(p, c[p-20:p+50])
        pos2 = p + 4

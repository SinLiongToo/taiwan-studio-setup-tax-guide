# -*- coding: utf-8 -*-
import glob

f = glob.glob('*分享版.html')[0]
c = open(f, 'r', encoding='utf-8').read()

pos = c.find('toggleTheme')
print("toggleTheme definition:")
print(c[pos:pos+400])

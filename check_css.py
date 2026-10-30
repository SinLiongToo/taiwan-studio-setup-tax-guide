# -*- coding: utf-8 -*-
import glob

f = glob.glob('*分享版.html')[0]
c = open(f, 'r', encoding='utf-8').read()

print("box-info definition:")
pos = c.find('.box-info')
print(c[pos:pos+300])

print("html tag definition:")
h_pos = c.find('html.dark')
print(c[h_pos:h_pos+300])

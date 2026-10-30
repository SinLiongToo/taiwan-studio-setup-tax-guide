# -*- coding: utf-8 -*-
import glob

f = glob.glob('*分享版.html')[0]
c = open(f, 'r', encoding='utf-8').read()

# Let's inspect CSS variables
p = c.find(':root')
print("CSS Variables:")
print(c[p:p+1000])

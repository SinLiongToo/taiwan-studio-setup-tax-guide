# -*- coding: utf-8 -*-
import glob

f = glob.glob('*分享版.html')[0]
c = open(f, 'r', encoding='utf-8').read()

print("box-info & box-success:")
p = c.find('.box-info')
print(c[p:p+800])

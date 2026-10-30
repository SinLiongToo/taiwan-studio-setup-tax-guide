# -*- coding: utf-8 -*-
import glob

f = glob.glob('*分享版.html')[0]
c = open(f, 'r', encoding='utf-8').read()

print("theme toggle script:")
pos = c.find('themeToggle')
print(c[pos-100:pos+800].encode('raw_unicode_escape').decode('ascii'))

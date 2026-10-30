# -*- coding: utf-8 -*-
import glob

f = glob.glob('*分享版.html')[0]
c = open(f, 'r', encoding='utf-8').read()

print("Snippet surrounding line 473846:")
pos = 473846
print(c[pos-300:pos+150].encode('raw_unicode_escape').decode('ascii'))

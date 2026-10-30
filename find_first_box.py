# -*- coding: utf-8 -*-
import glob

f = glob.glob('*分享版.html')[0]
c = open(f, 'r', encoding='utf-8').read()

print("Searching for first circled element text:")
# In the screenshot:
# "營業身分與發票抉擇" or "千萬不要加註"
terms = ["營業身分", "發票抉擇", "千萬不要加註", "統編何時會正式出來"]
for t in terms:
    pos = c.find(t)
    print(t, "->", pos)
    if pos != -1:
        print(c[pos-100:pos+250].encode('raw_unicode_escape').decode('ascii'))

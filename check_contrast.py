# -*- coding: utf-8 -*-
import glob

f = glob.glob('*分享版.html')[0]
c = open(f, 'r', encoding='utf-8').read()

print("Checking styles for .desc-text, .tab-channel-payout, etc:")
for cls in ['.desc-text', '.card-custom', 'html.dark .card-custom', 'html.dark body']:
    p = c.find(cls)
    if p != -1:
        print(cls, "->", c[p:p+150].replace('\n', ' '))
    else:
        print(cls, "not found")

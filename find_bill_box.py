# -*- coding: utf-8 -*-
import glob

f = glob.glob('*分享版.html')[0]
c = open(f, 'r', encoding='utf-8').read()

pos = c.find('AA-88996633')
start = c.rfind('<div class="', 0, pos)
# find the container of this bill
print("Bill container:")
bill_box = c.rfind('<div class="real-bill-wrap', 0, pos)
if bill_box == -1:
    bill_box = c.rfind('<div class="paper-', 0, pos)
print("bill_box at:", bill_box)
print(c[bill_box:bill_box+150].encode('raw_unicode_escape').decode('ascii'))

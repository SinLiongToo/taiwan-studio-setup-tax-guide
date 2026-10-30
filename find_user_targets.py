# -*- coding: utf-8 -*-
import glob

f = glob.glob('*分享版.html')[0]
c = open(f, 'r', encoding='utf-8').read()

print("Locating the two problematic sections from user screenshot:")
# Problem 1: "取得稅局核定的「營業身分與發票抉擇」"
p1 = c.find('取得稅局核定的')
if p1 != -1:
    print("Found p1:")
    print(c[p1-150:p1+300].encode('raw_unicode_escape').decode('ascii'))

# Problem 2: "重大觀念澄清（千萬別搞錯時機與機關）"
p2 = c.find('重大觀念澄清')
if p2 != -1:
    print("Found p2:")
    print(c[p2-150:p2+300].encode('raw_unicode_escape').decode('ascii'))

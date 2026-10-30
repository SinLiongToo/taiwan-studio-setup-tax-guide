# -*- coding: utf-8 -*-
import glob

f = glob.glob('*分享版.html')[0]
c = open(f, 'r', encoding='utf-8').read()

pos = c.find('聯發整合行銷股份有限公司')
print("Found target invoice at pos:", pos)
print(c[pos-300:pos+500].encode('raw_unicode_escape').decode('ascii'))

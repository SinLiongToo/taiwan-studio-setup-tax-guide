# -*- coding: utf-8 -*-
import glob

f = glob.glob('*分享版.html')[0]
c = open(f, 'r', encoding='utf-8').read()

# Let's inspect the sub-card in step 2 that is showing up as light background with white/light text in the screenshot!
# In the screenshot:
# "(clipboard) 申辦統編必填欄位與準備文件 (照著填即可) :"
# has a light blue-grey background with nearly invisible text!
pos = c.find('申辦統編必填欄位與準備文件')
if pos != -1:
    print("Found '申辦統編必填欄位與準備文件'!")
    print(c[pos-200:pos+800].encode('raw_unicode_escape').decode('ascii'))
else:
    print("Not found by exact string, let's search step2_d:")
    s2 = c.find('id="step2_d"')
    print(c[s2:s2+1500].encode('raw_unicode_escape').decode('ascii'))

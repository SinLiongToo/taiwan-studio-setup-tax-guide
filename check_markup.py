# -*- coding: utf-8 -*-
import glob

f = glob.glob('*分享版.html')[0]
c = open(f, 'r', encoding='utf-8').read()

# Let's inspect step 1 and step 2
s1_idx = c.find('id="step1_t"')
print("Step 1 snippet:")
print(c[s1_idx-100:s1_idx+500].encode('raw_unicode_escape').decode('ascii'))

s2_idx = c.find('id="step2_t"')
print("Step 2 snippet:")
print(c[s2_idx-100:s2_idx+600].encode('raw_unicode_escape').decode('ascii'))

# Also check payout guide snippet
p_idx = c.find('id="tab-channel-payout"')
print("Payout snippet:")
print(c[p_idx:p_idx+800].encode('raw_unicode_escape').decode('ascii'))

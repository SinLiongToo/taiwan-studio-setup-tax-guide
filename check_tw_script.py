# -*- coding: utf-8 -*-
import glob

f = glob.glob('*分享版.html')[0]
c = open(f, 'r', encoding='utf-8').read()

print("Checking Tailwind CDN:")
pos = c.find('cdn.tailwindcss.com')
print("cdn.tailwindcss.com pos:", pos)

pos_script = c.find('tailwind =')
print("tailwind config pos:", pos_script)
print(c[pos_script:pos_script+300])

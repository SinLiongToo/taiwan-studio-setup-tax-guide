# -*- coding: utf-8 -*-
with open('classes_used.txt', 'r', encoding='utf-8') as f:
    lines = [l.strip() for l in f if l.strip().startswith('dark:')]
print("Dark classes used:")
for l in lines:
    print(" ", l)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：albert time:20/2/18

f = open('/Users/Aalon/test.txt', 'r')
a = f.read()
print(a)
f.close()

try:
    f = open('/Users/Aalon/test.txt', 'r')
    print(f.read())
finally:
    if f:
        f.close()

with open('/Users/Aalon/test.txt', 'r') as f:
    print(f.read())

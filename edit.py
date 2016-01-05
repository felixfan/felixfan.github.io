# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 15:55:38 2016

@author: alicefelix
"""

import sys

dat = sys.argv[1]

f = open(dat)

n = 0

for r in f:
    r = r.strip()
    if r.startswith('-'):
    	n += 1
    print r
    if n == 2:
    	print '{% include JB/setup %}'
    	n = 0
f.close()

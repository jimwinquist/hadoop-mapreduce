#!/usr/bin/python

import sys

salesTotal = 0
count = 0
oldKey = None

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        continue
    
    thisKey, thisSale = data
    
    if oldKey and oldKey != thisKey:
        print oldKey, "\t", (salesTotal/count)
        oldKey = thisKey;
        salesTotal = 0
        count = 0

    oldKey = thisKey
    salesTotal += float(thisSale)
    count += 1

if oldKey != None:
    print oldKey, "\t", (salesTotal/count)
    
    

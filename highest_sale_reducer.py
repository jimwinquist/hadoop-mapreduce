#!/usr/bin/python

import sys

highestSale = 0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    thisKey, thisSale = data_mapped

    if oldKey and oldKey != thisKey
        print oldKey, "\t", highestSale
        oldKey = thisKey;
        highestSale = 0

    oldKey = thisKey
    if float(thisSale) > highestSale:
        highestSale = float(thisSale)

if oldKey != None:
    print oldKey, "\t", highestSale


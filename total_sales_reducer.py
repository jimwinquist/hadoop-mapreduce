#!/usr/bin/python

import sys

numberOfSales = 0
totalValueOfSales = 0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    thisKey, thisSale = data_mapped

    totalValueOfSales += float(thisSale)
    numberOfSales += 1

print numberOfSales, "\t", totalValueOfSales
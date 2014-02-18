#!/usr/bin/python

import sys

hitsTotal = 0
oldPage = None

for line in sys.stdin:
    data_mapped = line.strip()
    if len(data_mapped) != 1:
        continue

    thisPage = data_mapped

    if oldPage and oldPage != thisPage:
        print oldPage, "\t", hitsTotal
        oldPage = thisPage;
        hitsTotal = 0

    oldPage = thisPage
    hitsTotal += 1

if oldPage != None:
    print oldPage, "\t", hitsTotal


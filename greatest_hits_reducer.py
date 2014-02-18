#!/usr/bin/python

import sys

hitsTotal = 0
oldPage = None
greatestPage = None
greatestHits = 0

for line in sys.stdin:
    data_mapped = line.strip().split()
    if len(data_mapped) != 1:
        continue

    thisPage = data_mapped[0]

    if oldPage and oldPage != thisPage:
        if hitsTotal > greatestHits:
            greatestHits = hitsTotal
            greatestPage = oldPage
        oldPage = thisPage;
        hitsTotal = 0

    oldPage = thisPage
    hitsTotal += 1

if oldPage != None:
    if hitsTotal > greatestHits:
        greatestHits = hitsTotal
        greatestPage = oldPage
    print greatestPage, "\t", greatestHits


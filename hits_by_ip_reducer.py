#!/usr/bin/python

import sys

hitsTotal = 0
oldIP = None

for line in sys.stdin:
    data_mapped = line.strip().split()
    if len(data_mapped) != 1:
        continue

    thisIP = data_mapped[0]

    if oldIP and oldIP != thisIP:
        print oldIP, "\t", hitsTotal
        oldIP = thisIP;
        hitsTotal = 0

    oldIP = thisIP
    hitsTotal += 1

if oldIP != None:
    print oldIP, "\t", hitsTotal


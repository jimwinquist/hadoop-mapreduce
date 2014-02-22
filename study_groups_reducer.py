#!/usr/bin/python

import sys

oldKey = None
contributors = []

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue
    
    thisKey, author = data_mapped
    
    if oldKey and oldKey != thisKey:
        print oldKey, "\t", sorted(contributors)
        oldKey = thisKey;
        contributors = []
    
    oldKey = thisKey
    contributors.append(author)

if oldKey != None:
    print oldKey, "\t", sorted(contributors)

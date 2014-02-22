#!/usr/bin/python

import sys
import operator

tagTotal = 0
oldKey = None
tag_dict = {}

for line in sys.stdin:
    data_mapped = line.strip().split()
    if len(data_mapped) != 1:
        continue
    
    thisKey = data_mapped[0]
    
    if oldKey and oldKey != thisKey:
        tag_dict[oldKey] = tagTotal
        #print oldKey, "\t", tagTotal
        oldKey = thisKey;
        tagTotal = 0
    
    oldKey = thisKey
    tagTotal += 1

if oldKey != None:
    tag_dict[oldKey] = tagTotal
    #print oldKey, "\t", tagTotal

sorted_tags = sorted(tag_dict.iteritems(), key=operator.itemgetter(1))
for tag in sorted_tags[-10:]:
    print "{0}\t{1}".format(tag[0], tag[1])
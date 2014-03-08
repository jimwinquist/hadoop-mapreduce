#!/usr/bin/python
'''
We are interested in finding out the most commonly used tags to
categorize posts on a forum. The goal is to write a map reduce program
that would process forum node data and output the top 10 tags ordered
by the number of questions they appear in.

In the reducer we will initialize a python dictionary to store all the
tags as keys their values will be the count of the number of times that
tag is output by the map phase. For each tag we come across we will add
it to the dict and then increment it's count for each subsequent
occurence. When we reach the next key(tag) we will repeat.

Then when the reducer has finished recording all of the tags and their
counts we can sort the dictionary by value, return the top ten tags and
their values and output them to standard output.

The input from the mapper for each record will be a single tag as a
string.
'''

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

    if oldKey is not None and oldKey != thisKey:
        tag_dict[oldKey] = tagTotal
        oldKey = thisKey;
        tagTotal = 0

    oldKey = thisKey
    tagTotal += 1

if oldKey is not None:
    tag_dict[oldKey] = tagTotal

sorted_tags = sorted(tag_dict.iteritems(), key=operator.itemgetter(1))
for tag in sorted_tags[-10:]:
    print "{0}\t{1}".format(tag[0], tag[1])

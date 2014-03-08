#!/usr/bin/python
"""
It could be useful to know how active users are on the forum and to
find out the average number of posts each person makes.

The goal is to write a map reduce program that parses forum node data
and returns a single float value representing the average number of
posts per active user.

In the reducer we will collect all the authors as the primary key in a
large dictionary and assign to each key a value representing the number
of times that author posted on the forum. Then we can calculate the
average number of posts per user.
"""

import sys
import operator

postTotal = 0
oldKey = None
author_dict = {}

for line in sys.stdin:
    data_mapped = line.strip().split()
    if len(data_mapped) != 1:
        continue

    thisKey = data_mapped[0]

    if oldKey is not None and oldKey != thisKey:
        author_dict[oldKey] = postTotal
        oldKey = thisKey
        postTotal = 0

    oldKey = thisKey
    postTotal += 1

if oldKey is not None:
    author_dict[oldKey] = postTotal

count = 0
total = 0
for author in author_dict:
    count += 1
    total += author_dict[author]

print "{0}".format(total/float(count))

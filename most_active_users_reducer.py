#!/usr/bin/python
'''
We are interested in finding out the most active users on the forum.
The goal is to write a map reduce program that would process forum
node data and output the top 10 active users in the order of most
activity.

In the reducer we will initialize a python dictionary to store all the
authors as keys and their values will be the count of the number of
times that author is output by the map phase. For each author we come
across we will add it to the dict and then increment it's count for
each subsequent occurence. When we reach the next key(author_id) we
will repeat.

Then when the reducer has finished recording all of the author_ids and
their counts we can sort the dictionary by value, return the top ten
authors and their values and output them to standard output.

The input from the mapper for each record will be a single author_id as
a string.
'''

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
        oldKey = thisKey;
        postTotal = 0

    oldKey = thisKey
    postTotal += 1

if oldKey is not None:
    author_dict[oldKey] = postTotal

sorted_authors = sorted(author_dict.iteritems(), key=operator.itemgetter(1))
for item in sorted_authors[-10:]:
    author_id = item[0]
    post_count = item[1]
    print "{0}\t{1}".format(author_id, post_count)

#!/usr/bin/python
'''
We are interested to see which are the top rated posts on the forum.

The goal is to write a mapreduce program that would process forum_node
data and output the top 10 posts ordered by score.

In the reducer we want to add all of the posts to a dictionary with the
post_id as the key and the score as the value.

Then we can sort the dictionary by value and return the top 10. Example
output from the reducer would be a top 10 list in the following format:

post_id     score
'''

import sys
import operator

post_dict = {}

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    post_id, score = data_mapped
    post_dict[post_id] = int(score)

sorted_posts = sorted(post_dict.iteritems(), key=operator.itemgetter(1))
for post in sorted_posts[-10:]:
    print "{0}\t{1}".format(post[0], post[1])

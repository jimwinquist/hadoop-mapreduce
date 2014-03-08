#!/usr/bin/python
'''
Students come from all around the world, so we need to know both at
what times of day the activity is the highest, and to know which of the
students are active at that time.

The goal is to write a map reduce program that would process forum node
data and find for each student what is the hour during which the
student has posted the most.

In the reducer we will loop through the author_id\thour pairs from the
mapper and assemble a dictionary that assigns each user as a key, with
a nested key for each hour the user has posted. Then we will keep a
count of how many times the user posted as the value associated with
the hour key.

Then for each user we can find which hour as the largest count and
output the value with the author_id

Output from reducers should be:

author_id    hour

If there is a tie: there are multiple hours during which a student has
posted a maximum number of posts, we will output the student-hour pairs
on separate lines.
'''

import sys

time_index = {}

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    author_id, hour = data_mapped

    if author_id in time_index.keys():
        if hour in time_index[author_id].keys():
            time_index[author_id][hour] += 1
        else:
            time_index[author_id][hour] = 1
    else:
        time_index[author_id] = {}
        time_index[author_id][hour] = 1

for author_id in time_index:
    maxHour = max(time_index[author_id],
                    key = lambda x:time_index[author_id].get(x))
    maxValue = time_index[author_id][maxHour]
    for hour in time_index[author_id]:
        if time_index[author_id][hour] == maxValue:
            print "{0}\t{1}".format(author_id, hour)

#!/usr/bin/python
'''
We might want to help students form study groups. But first we want to
see if there are already students on forums that communicate a lot
between themselves.

The goal is to write a mapreduce program that for each forum thread
(that is a question node with all it's answers and comments) would give
us a list of students that have posted there - either asked the
question, answered a question or added a comment. If a student posted
to that thread several times, they should be added to that list several
times as well, to indicate intensity of communication.

In the reducer we will loop through each post_id\tauthor_id pair from
the mapper and using the post_id as the primary key assemble an array
of all of the author_id's associated with that key. Then when we reach
the next key output the previous key and the array of associated
contributors.

Output from the reducers should be:
post_id    [contributors]
'''

import sys

oldKey = None
contributors = []

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    thisKey, author = data_mapped

    if oldKey is not None and oldKey != thisKey:
        print oldKey, "\t", sorted(contributors)
        oldKey = thisKey;
        contributors = []

    oldKey = thisKey
    contributors.append(author)

if oldKey is not None:
    print oldKey, "\t", sorted(contributors)

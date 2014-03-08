#!/usr/bin/python
'''
We are interested to see which are the top rated posts on the forum.

The goal is to write a mapreduce program that would process forum_node
data and output the top 10 posts ordered by score.

In the mapper we use the csv module to read in forum node data from
standard input and store it in a reader object. Then parse each record
and output the post id and score:

post_id     score

Each line in the forum_node.tsv input file represents a forum post with
the following 19 tab delimited fields:

id\ttitle\ttagnames\tauthor_id\tbody\tnode_type\tparent_id\t
abs_parent_id\tadded_at\tscore\tstate_string\tlast_edited_id\t
last_activity_by_id\tlast_activity_at\tactive_revision_id\textra\t
extra_ref_id\textra_count\tmarked
'''

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
#Skip the header row
reader.next()

for record in reader:
    #Make sure each record conforms to the format we expect
    if len(record) == 19:
        post_id = record[0]
        score = record[9]

        print "{0}\t{1}".format(post_id, score)

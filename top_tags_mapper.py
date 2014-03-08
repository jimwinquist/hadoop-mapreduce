#!/usr/bin/python
'''
We are interested in finding out the most commonly used tags to
categorize posts on a forum. The goal is to write a map reduce program
that would process forum node data and output the top 10 tags ordered
by the number of questions they appear in.

In the mapper we simply need to get the values in the tagnames field
and for each one print it out as the primary key to standard output.

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
reader.next()

for record in reader:
    if len(record) == 19:
        tagnames = record[2]
        tags = tagnames.strip().split()
        for tag in tags:
            print "{0}".format(tag)


#!/usr/bin/python
"""
It could be useful to know how active users are on the forum and to
find out the average number of posts each person makes.

The goal is to write a map reduce program that parses forum node data
and returns a single float value representing the average number of
posts per active user.

In the mapper we will simply loop through each post record and return
the author_id to standard output.

Each line in the forum_node.tsv input file represents a forum post with
the following 19 tab delimited fields:

id\ttitle\ttagnames\tauthor_id\tbody\tnode_type\tparent_id\t
abs_parent_id\tadded_at\tscore\tstate_string\tlast_edited_id\t
last_activity_by_id\tlast_activity_at\tactive_revision_id\textra\t
extra_ref_id\textra_count\tmarked
"""

import sys
import csv


reader = csv.reader(sys.stdin, delimiter='\t')
#Skip the header row
reader.next()

for record in reader:
    if len(record) == 19:
        author_id = record[3]
        print "{0}".format(author_id)

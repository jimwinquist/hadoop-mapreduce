#!/usr/bin/python
'''
We are interested in finding out the most active users on the forum. The goal
is to write a map reduce program that would process forum node data and
output the top 10 active users in the order of most activity.

In the mapper we simply need to get the values in the author_id field and for
each one print it out as the primary key to standard output.

Each line in the forum_node.tsv input file represents a forum post with the
following 19 tab delimited fields:

id\ttitle\ttagnames\tauthor_id\tbody\tnode_type\tparent_id\tabs_parent_id\t
added_at\tscore\tstate_string\tlast_edited_id\tlast_activity_by_id\t
last_activity_at\tactive_revision_id\textra\textra_ref_id\textra_count\tmarked
'''

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
reader.next()

for record in reader:
    if len(record) == 19:
        author_id = record[3]
        print "{0}".format(author_id)


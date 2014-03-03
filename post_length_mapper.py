#!/usr/bin/python
'''
We are interested to see if there is a correlation between the length of a post
and the length of answers.

The goal is to write a mapreduce program that would process forum_node data
and output the length of the post and the average answer (just answer, not comment)
length for each post.

In the mapper we use the csv module to read in forum node data from standard input
and store it in a reader object. Then parse each record and if it's a question write to standard output
the id as primary key and the length of the post as the value. If it's an answer output the abs_parent_id
as primary key and the length of the post as the value. In addition we will want to add a marker to each
output. 'A' for questions and 'B' for answers.

We are only interested in questions and answers. So, if the node_type doesn't match one of these we will
skip the record and move to the next.

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
        post_id, title, tagnames, author_id, body, node_type, parent_id, abs_parent_id = record[:8]
        if node_type == 'question':
            marker = 'A'
            print "{0}\t{1}\t{2}".format(post_id, marker, str(len(body)))
        elif node_type == 'answer':
            marker = 'B'
            print "{0}\t{1}\t{2}".format(abs_parent_id, marker, str(len(body)))
        else:
            pass


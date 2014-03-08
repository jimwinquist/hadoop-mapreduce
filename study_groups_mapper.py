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

In the mapper we are interested in the fields for post_id,
abs_parent_id, node_type, and author_id. We will return the post_id as
primary key and the author_id as the associated value.

We will loop through each record and check the node_type.
If the post is a question we will output the post_id and author_id.
If the post is an answer or comment we will output the abs_parent_id
and author_id.

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
        post_id, title, tagnames, author_id, body, node_type, parent_id, \
        abs_parent_id = record[:8]

        if node_type == 'question':
            print "{0}\t{1}".format(post_id, author_id)
        else:
            print "{0}\t{1}".format(abs_parent_id, author_id)


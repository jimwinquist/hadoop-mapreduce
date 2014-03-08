#!/usr/bin/python
"""
Students come from all around the world, so we need to know both at
what times of day the activity is the highest, and to know which of the
students are active at that time.

The goal is to write a map reduce program that would process forum node
data and find for each student what is the hour during which the
student has posted the most.

In the mapper we are interested in the added_at field and we will then
use the datetime module to return the hour from the datetime object.
Then we can return the author_id as the primary key and the hour as the
value.

Output from mappers should be:

author_id    hour

Each line in the forum_node.tsv input file represents a forum post with
the following 19 tab delimited fields:

id\ttitle\ttagnames\tauthor_id\tbody\tnode_type\tparent_id\t
abs_parent_id\tadded_at\tscore\tstate_string\tlast_edited_id\t
last_activity_by_id\tlast_activity_at\tactive_revision_id\textra\t
extra_ref_id\textra_count\tmarked
"""

import sys
import csv
import datetime

reader = csv.reader(sys.stdin, delimiter='\t')
reader.next()
for record in reader:
    if len(record) == 19:
        author_id = record[3]
        added_at = record[8]

        #We can ignore the tim-zone offset
        time = added_at.partition("+")[0]
        hour = (datetime.datetime.strptime(time, "%Y-%m-%d %H:%M:%S.%f")
                .strftime("%H"))
        print "{0}\t{1}".format(author_id, hour)

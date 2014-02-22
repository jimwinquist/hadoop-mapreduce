#!/usr/bin/python

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
reader.next()

for record in reader:
    if len(record) == 19:
        post_id, title, tagnames, author_id, body, node_type, parent_id, abs_parent_id = record[:8]
        if node_type == 'question':
            print "{0}\t{1}".format(post_id, author_id)
        else:
            print "{0}\t{1}".format(abs_parent_id, author_id)


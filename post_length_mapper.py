#!/usr/bin/python

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


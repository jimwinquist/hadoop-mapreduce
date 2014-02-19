#!/usr/bin/python

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
reader.next()

for record in reader:
    if len(record) == 5:
        user_ptr_id, reputation, gold, silver, bronze = record
        marker = 'A'
        print "{0}\t{1}\t{2}\t{3}\t{4}\t{5}".format(user_ptr_id, marker, reputation, gold, silver, bronze)
    elif len(record) == 19:
        post_id, title, tagnames, author_id, body, node_type, parent_id, abs_parent_id, added_at, score = record[:10]
        marker = 'B'
        print "{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}".format(author_id, marker, post_id, title, tagnames, node_type, parent_id, abs_parent_id, added_at, score)

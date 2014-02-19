#!/usr/bin/python

import sys
import csv
import re

reader = csv.reader(sys.stdin, delimiter='\t')
reader.next()
for record in reader:
    post_id = record[0]
    body = record[4]
    text = re.split('\W+', body)
    for word in text:
        if word:
            print "{0}\t{1}".format(word.lower(), post_id)

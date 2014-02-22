#!/usr/bin/python

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


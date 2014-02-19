#!/usr/bin/python

import sys
import csv
import datetime

reader = csv.reader(sys.stdin, delimiter='\t')
reader.next()
for record in reader:
    if len(record) == 19:
        author_id = record[3]
        added_at = record[8]
        
        time = added_at.partition("+")[0]
        hour = datetime.datetime.strptime(time, "%Y-%m-%d %H:%M:%S.%f").strftime("%H")
        print "{0}\t{1}".format(author_id, hour)


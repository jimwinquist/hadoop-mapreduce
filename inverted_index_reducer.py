#!/usr/bin/python

import sys
import csv

forum_index = {}

reader = csv.reader(sys.stdin, delimiter='\t')

for data in reader:
    if len(data) != 2:
        continue
    
    word, post_id = data
    forum_index.setdefault(word, [])
    forum_index[word].append(post_id)
 
#print "{0}".format(len(forum_index["fantastic"]))

#print "{0}".format(forum_index["fantastically"])

for key in forum_index:
    num_occurences = len(forum_index[key])
    post_id_index = sorted(set(forum_index[key]))
    print "{0}\t{1}\t{2}".format(key, num_occurences, post_id_index)

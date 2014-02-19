#!/usr/bin/python

import sys

oldKey = None
user_data = []
post_data = []

for line in sys.stdin:
    record = line.strip().split("\t")
    thisKey = record[0]
    marker = record[1]

    if oldKey and oldKey != thisKey:
        if post_data:
            for post in post_data:
                if user_data:
                    for user in user_data:
                        post.extend(user)
                        print('\t'.join(map(str,post)))
                
        oldKey = thisKey
        user_data = []
        post_data = []

    oldKey = thisKey
    if marker == 'A':
        user_ptr_id, marker, reputation, gold, silver, bronze = record
        user_data.append([reputation, gold, silver, bronze])
    elif marker == 'B':
        author_id, marker, post_id, title, tagnames, node_type, parent_id, abs_parent_id, added_at, score = record
        post_data.append([post_id, title, tagnames, author_id, node_type, parent_id, abs_parent_id, added_at, score])
        
if oldKey != None:
    if post_data:
        for post in post_data:
            if user_data:
                for user in user_data:
                    post.extend(user)
                    print('\t'.join(map(str,post)))

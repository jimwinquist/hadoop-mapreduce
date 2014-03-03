#!/usr/bin/python
'''
We are interested to see if there is a correlation between the length of a post
and the length of answers.

The goal is to write a mapreduce program that would process forum_node data
and output the length of the post and the average answer (just answer, not comment)
length for each post.

In the reducer we start by initializing arrays for storing question and answer lengths for a given key.
Then we read in our mapper (key, value) pairs from standard input, split them by tab and store the values as
variables. As we loop through the keys, we will append the values to the appropriate array. Then when we
come across a new key output the question length and average answer length associated with that question.

Each line from the mapper will have the following 3 tab delimited fields:
post_id\tmarker\post_length
'''

import sys

oldKey = None
question = None
answers = []

for line in sys.stdin:
    record = line.strip().split("\t")
    thisKey = record[0]
    marker = record[1]
    post_length = record[2]

    if oldKey is not None and oldKey != thisKey:
        if question is not None:
            if answers:
                answers = [int(answer) for answer in answers]
                print "{0}\t{1}\t{2}".format(oldKey, question, str(sum(answers)/len(answers)))
            else:
                print "{0}\t{1}\t{2}".format(oldKey, question, '0')
                
        oldKey = thisKey
        question = None
        answers = []


    oldKey = thisKey
    if marker == 'A':
        question = post_length
    elif marker == 'B':
        answers.append(post_length)
        
if oldKey is not None:
    if question is not None:
        if answers:
            answers = [int(answer) for answer in answers]
            print "{0}\t{1}\t{2}".format(oldKey, question, str(sum(answers)/len(answers)))
        else:
            print "{0}\t{1}\t{2}".format(oldKey, question, '0')

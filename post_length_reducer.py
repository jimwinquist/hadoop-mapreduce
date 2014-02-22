#!/usr/bin/python

import sys

oldKey = None
question = []
answers = []
lengthTotal = 0
countTotal = 0

for line in sys.stdin:
    record = line.strip().split("\t")
    thisKey = record[0]
    marker = record[1]

    if oldKey and oldKey != thisKey:
        if answers:
            for answer in answers:
                countTotal += 1
                lengthTotal += float(answer)
        if question:
            for q in question:
                if countTotal > 0:
                    print "{0}\t{1}\t{2}".format(oldKey, q, str(lengthTotal/countTotal))
                else:
                    print "{0}\t{1}\t{2}".format(oldKey, q, '0')
                
        oldKey = thisKey
        question = []
        answers = []
        lengthTotal = 0
        countTotal = 0

    oldKey = thisKey
    if marker == 'A':
        post_length = record[2]
        question.append(post_length)
    elif marker == 'B':
        answer_length = record[2]
        answers.append(answer_length)
        
if oldKey != None:
    if answers:
        for answer in answers:
            countTotal += 1
            lengthTotal += float(answer)
    if question:
        for q in question:
            if countTotal > 0:
                print "{0}\t{1}\t{2}".format(oldKey, q, str(lengthTotal/countTotal))
            else:
                print "{0}\t{1}\t{2}".format(oldKey, q, '0')

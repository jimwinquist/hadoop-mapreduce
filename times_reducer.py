#!/usr/bin/python

import sys

time_index = {}

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        continue
    
    author_id, hour = data
    
    if author_id in time_index.keys():
        if hour in time_index[author_id].keys():
            time_index[author_id][hour] += 1
        else:
            time_index[author_id][hour] = 1    
    else:
        time_index[author_id] = {}
        time_index[author_id][hour] = 1

for author_id in time_index:   
    maxHour = max(time_index[author_id], key = lambda x:time_index[author_id].get(x) )
    maxValue = time_index[author_id][maxHour]
    for hour in time_index[author_id]:
        if time_index[author_id][hour] == maxValue:
            print "{0}\t{1}".format(author_id, hour)
    
    


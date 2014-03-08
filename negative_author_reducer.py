#!/usr/bin/python
"""
It could be useful to judge the sentiment of posts on the forum and to
be able to find out who are the most positive or negative contributors
to the forums.

The goal is to write a map reduce program that uses an external file(
AFINN-111.txt)to create a dictionary of mood scores per word. Then we
can loop through the posts in the forum node data and assign mood
scores to every word in each post. We can then total up all the scores
for each author and see which authors are using the most positive
language and which authors are using the most negative language.

In the reducer I loop through each primary key(author_id) and total up
all the post_scores associated with that author and store it in a
dictionary. Then when all of the authors post scores have been totaled
I can sort the dictionary by score and return the top 10 most positive
or most negative author_ids with their associated total mood scores.
Another fun experiment might be to get the average mood score per
author or the average mood score per user on the forum to judge
overall forum sentiment.

The output from the reducers will be a top ten list in the format:
author_id   total_mood_score

I had to modify the hadoop streaming command to pass in the additional
file AFINN-111.txt as part of the job. Following is the modified
command string:

hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/ \
hadoop-streaming-2.0.0-mr1-cdh4.1.1.jar \
-mapper negative_author_mapper.py -reducer negative_author_reducer.py \
-file negative_author_mapper.py -file negative_author_reducer.py \
-file AFINN-111.txt -input forum_node_data \
-output negative_author_output
"""
import sys
import operator

scoreTotal = 0
oldKey = None
author_dict = {}

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    thisKey, score = data_mapped

    if oldKey is not None and oldKey != thisKey:
        author_dict[oldKey] = scoreTotal
        oldKey = thisKey
        scoreTotal = 0

    oldKey = thisKey
    scoreTotal += float(score)

if oldKey is not None:
    author_dict[oldKey] = scoreTotal

sorted_authors = sorted(author_dict.iteritems(), key=operator.itemgetter(1))
for author in sorted_authors[:10]:
    print "{0}\t{1}".format(author[0], author[1])

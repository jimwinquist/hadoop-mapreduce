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

In the mapper I use AFINN-111.txt to build a dictionary of mood scores.
I then grab the author_id and body of each post and for each word in
the body loop through and assign a mood score to each word, and output
the author_id and total score for that post to standard output. e.g.

author_id   post_score

I had to modify the hadoop streaming command to pass in the additional
file AFINN-111.txt as part of the job. Following is the modified
command string:

hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/ \
hadoop-streaming-2.0.0-mr1-cdh4.1.1.jar \
-mapper positive_author_mapper.py -reducer positive_author_reducer.py \
-file positive_author_mapper.py -file positive_author_reducer.py \
-file AFINN-111.txt -input forum_node_data \
-output positive_author_output

Each line in the forum_node.tsv input file represents a forum post with
the following 19 tab delimited fields:

id\ttitle\ttagnames\tauthor_id\tbody\tnode_type\tparent_id\t
abs_parent_id\tadded_at\tscore\tstate_string\tlast_edited_id\t
last_activity_by_id\tlast_activity_at\tactive_revision_id\textra\t
extra_ref_id\textra_count\tmarked
"""

import sys
import csv
import re

mood_dict = {}

mood_file = open('AFINN-111.txt')
for line in mood_file:
        scores = line.split('\t')
        mood_dict[scores[0]] = float(scores[1])

reader = csv.reader(sys.stdin, delimiter='\t')
#Skip the header row
reader.next()

for record in reader:
    if len(record) == 19:
        author_id = record[3]
        body = record[4]
        text = re.split('\W+', body)

        post_score = 0.0
        for word in text:
            if word:
                if word.lower() in mood_dict:
                    post_score += mood_dict[word.lower()]
        print "{0}\t{1}".format(author_id, post_score)

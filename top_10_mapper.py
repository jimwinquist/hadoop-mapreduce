#!/usr/bin/python
import sys
import csv
from operator import itemgetter

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
    
    L = []
    for line in reader:
        
        # YOUR CODE HERE
        L.append([len(line[4]), line])
    
    OL = sorted(L, key = itemgetter(0))
    
    for item in OL[-10:]:
        writer.writerow(item[1])



test_text = """\"\"\t\"\"\t\"\"\t\"\"\t\"333\"\t\"\"
    \"\"\t\"\"\t\"\"\t\"\"\t\"88888888\"\t\"\"
    \"\"\t\"\"\t\"\"\t\"\"\t\"1\"\t\"\"
    \"\"\t\"\"\t\"\"\t\"\"\t\"11111111111\"\t\"\"
    \"\"\t\"\"\t\"\"\t\"\"\t\"1000000000\"\t\"\"
    \"\"\t\"\"\t\"\"\t\"\"\t\"22\"\t\"\"
    \"\"\t\"\"\t\"\"\t\"\"\t\"4444\"\t\"\"
    \"\"\t\"\"\t\"\"\t\"\"\t\"666666\"\t\"\"
    \"\"\t\"\"\t\"\"\t\"\"\t\"55555\"\t\"\"
    \"\"\t\"\"\t\"\"\t\"\"\t\"999999999\"\t\"\"
    \"\"\t\"\"\t\"\"\t\"\"\t\"7777777\"\t\"\"
    """

# This function allows you to test the mapper with the provided test string
def main():
    import StringIO
    sys.stdin = StringIO.StringIO(test_text)
    mapper()
    sys.stdin = sys.__stdin__

main()

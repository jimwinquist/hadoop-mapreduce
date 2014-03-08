#!/usr/bin/python

import sys
from urlparse import urlparse

for line in sys.stdin:
    data = line.strip().split(" ")

    if len(data) == 10:
        ip, identity, username, endtime, zone, method, url, querystring, status, size = data
        path = urlparse(url)[2]
        query = urlparse(url)[4]
        if query:
            path += '?' + query
        print "{0}".format(path)


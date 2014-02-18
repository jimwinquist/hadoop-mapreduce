#!/usr/bin/python

import sys

for line in sys.stdin:
    data = line.strip().split(" ")

    if len(data) == 10:
        ip, identity, username, endtime, zone, method, url, querystring, status, size = data

        print "{0}".format(ip)


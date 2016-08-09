#!/usr/bin/python

import httplib

conn = httplib.HTTPConnection("www.feingold-research.com")
conn.request("GET","/transaktionshistorie-favoritendepot/")
res = conn.getresponse()
data = res.read()
print data


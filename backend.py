#!/usr/bin/python3

import subprocess as sp
import cgi

print('content-type: text/html')
print()

data = cgi.FieldStorage()
x = data.getvalue('x')

output = sp.getoutput('x')

print(output)

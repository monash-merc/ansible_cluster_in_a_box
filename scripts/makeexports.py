#!/usr/bin/python

import sys, os

def config(source, host, option, input = None):
    content = None 
    if input:
        if not host in input:
            content = input + " " + host + "(" + option + ")"
    else:
        content = source + " " + host + "(" + option + ")"
    return content
                
path = sys.argv[1]
host = sys.argv[2]
option = sys.argv[3]
source = sys.argv[4]

io = open(path, 'r')
input = io.read()
io.close()
content = config(source, host, option, input)
if content:
    io = open(path, 'w')
    io.write(content)
    io.close()


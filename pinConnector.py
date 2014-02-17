#!/usr/bin/python

# designed for xilinx datasheets

import sys
import string

if (len(sys.argv) == 2):
  filename = sys.argv[1]
else:
  print str(len(sys.argv))
  raise Exception("wrong number of input arguments")

outfile = open('out-pads.txt', 'w')

maxcol = 16
colwidth = 1.0

pos = 0.0
index = 0
pincount = {}
connections = {}

with open(filename) as f:
  for line in f:
    components = line.split(' ')
    name = components[1]
    pad = components[2]
    
    if name in pincount:
      if pincount[name] == 1:
	oldpad = connections[name]
	connections.pop(name, None)
	connections[name+"@0"] = oldpad
      pincount[name] = pincount[name] + 1
      printname = name+"@"+str(pincount[name]-1)
    else:
      pincount[name] = 1
      printname = name
      
    connections[printname] = pad
    
for item in connections:
  outfile.write("CONNECT '"+item+"' '"+connections[item]+"';\n")
    
f.close()

outfile.close()

#!/usr/bin/python

# designed for xilinx datasheets

import sys
import string

if (len(sys.argv) == 2):
  filename = sys.argv[1]
else:
  print str(len(sys.argv))
  raise Exception("wrong number of input arguments")

outfile = open('out.txt', 'w')

pos = 0.0
pincount = {}

with open(filename) as f:
  for line in f:
    components = line.split(' ')
    name = components[1]
    
    if name in pincount:
      if pincount[name] == 1:
	outfile.write("NAME '"+name+"' '"+name+"@0';\n") #add counter to other pin
      pincount[name] = pincount[name] + 1
      printname = name+"@"+str(pincount[name]-1)
    else:
      pincount[name] = 1
      printname = name
    
    if "GND" in name or "VCC" in name:
      pintype = "Pwr"
    elif name == "NC":
      pintype = "NC"
    else:
      pintype = "I/O"
    
    outfile.write("PIN '"+printname+"' R180 "+pintype+" (1.0 "+str(pos)+");\n")
    pos = pos - 0.1
    # outfile.write('words['+str(start)+'] = {word: "' + line.replace('\n','') + '", timey: '+str(80*len(line))+', ignore: '+str(start+1)+', click: -1, colors: "' + color + '"};\n')
    
outfile.close()
f.close()

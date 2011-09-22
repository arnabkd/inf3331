#!/usr/bin/env python
import sys, re; from math import *
teststring = ""
try :
	teststring = sys.argv[1] + " " + sys.argv[2]
except:
	print "usage : python xygenerator.py start:stop,step func"

myregex = r'(\d+):(\d+),(\d+\.?\d*)\s(.*)' #regex to detect "'start:stop',step 'func'"
func_info = re.search(myregex, teststring).groups() #save the attributes for the x-y pairs to be generated
outfile = open ("generated.txt" , 'w')

try:
	start = float(func_info[0]);stop = float(func_info[1]); step = float(func_info[2]) #converting function attributes to floats
	x = start
	while (x <= stop):						
		outfile.write ("x: %d  y = %s = %f\n" % (x, func_info[3] , eval(func_info[3])))
		x += step
	outfile.close()
except :
	print "something went wrong (arguments were not typed properly)"




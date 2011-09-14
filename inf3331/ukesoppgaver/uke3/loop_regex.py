#!/usr/bin/env python

loop1 = '[0:12]'     # 0,1,2,3,4,5,6,7,8,9,10,11,12
loop2 = '[0:12, 4]'  # 0,4,8,12

r1 = r'\[(.+):(.+?),?(.*)\]' # '+?' means it matches 1 instead of 12. Not greedy enough
r2 = r'\[(.+):(.+),?(.*)\]' #too greedy

import re
print re.search(r1, loop1).groups()
print re.search(r2, loop1).groups()
print re.search(r1, loop2).groups()
print re.search(r2, loop2).groups()


r3 = r'\[(.+):([\d|.]+),?\s?(\d*)\]'
print "Output from working regex: "
print re.search(r3, loop2).groups()
print re.search(r3, loop1).groups()
 



#!/usr/bin/env python
import sys

infile = sys.argv[1]

ins = open (infile , "r")

matches = []
pattern = 'CPU-time'

#Read all lines that contain the pattern given above
#and append them to matches
for line in ins:
    if(line.startswith(pattern)):
	matches.append(line.split())
       

#A insertion-sort modified to take in the matches list and sort it :
#Every element's key is the element in position 1
#Example element in matchlist : ['CPU-time:', '9.92', 'g77', '-O2', 'if-test', 'inside', 'the', 'main', 'loop']
def insertionsort( matchlist ):
    for i in range (len (matchlist)):
        tmp = matchlist[i]
        j = i
        
        while (j > 0 and float(matchlist[j-1][1]) > float(tmp[1])):
            matchlist[j] = matchlist[j-1]
            j = j - 1
        matchlist[j] = tmp
    return matchlist
    


matches = insertionsort(matches)

#All elements look like this (sorted of course)
#CPU-time: 252.40   .. .. .. ..
for match in matches:
    print match


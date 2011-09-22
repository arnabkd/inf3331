#!/usr/bin/env python
"""Find all numbers in a string."""
import re

#Regex is greedy, hence the most complicated regex must be placed first, second-most greedy next and so on
r = r"([+\-]?\d\.\d+[Ee][+\-]\d\d?|[+\-]?\d+\.?\d*|[+\-]?\.\d+)"
c = re.compile(r)
s = "an array: (1)=3.9836, (2)=4.3E-09, (3)=8766, (4)=.549"
numbers = c.findall(s)
# make dictionary a, where a[1]=3.9836 and so on:
a = {}
for i in range(0,len(numbers)-1,2):
    a[int(numbers[i])] = float(numbers[i+1])
sorted_keys = a.keys(); sorted_keys.sort()
for index in sorted_keys:
    print "[%d]=%g" % (index,a[index])

#Kjoreeksempel
#arnabkd@spes ~/Desktop/uni/inf3331/inf3331/ukesoppgaver/uke3 $ python regexerror.py 
#[1]=3.9836
#[2]=4.3e-09
#[3]=8766
#[4]=0.549

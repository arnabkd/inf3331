#!/usr/bin/env python
import sys
argc = len(sys.argv)

def printusage():
    print "Usage : python count_words.py <textfile> <search-string>"
    print "For case-insensitive search, add -i before textfile"
    print "To keep word-boundaries, add -b before textfile"

#Checking that arguments are correct
#Assuming that users insert arguments in the correct order
# argv = ['count_words.py' , args.. , 'filename' 'search-string']
if (argc < 3 or argc > 5):
    printusage()
    sys.exit()

insensitive = ("-i" in sys.argv)
boundaries = ("-b" in sys.argv) 

filename = sys.argv[argc-2]
search_string = sys.argv[argc-1]

ifile = open (filename, 'r')
sum = 0

for line in ifile:
    if(insensitive):
        line = line.lower()
        search_string = search_string.lower()
    if(not boundaries):    
        sum += line.count(search_string)
    else:
        for word in line.split():
            if (word == search_string):
                sum += 1
    

res = "Number of occurances of string '%s' in '%s' : %d" %(search_string , filename , sum)
print res
exit()

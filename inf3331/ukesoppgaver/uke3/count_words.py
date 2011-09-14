#!/usr/bin/env python
import sys
argc = len(sys.argv)

def printusage():
    print "Usage : python count_words.py <textfile> <search-string>"
    print "For case-insensitive search, add -i before textfile"
    print "To keep word-boundaries, add -b before textfile"

#Checking that arguments are correct
#Assuming that users put run options before filename and search-string
# argv = ['count_words.py' , .. , 'filename' 'search-string']
if (argc < 3 or argc > 5):
    printusage()
    sys.exit()

insensitive = 1 if ("-i" in sys.argv) else 0
boundaries = 1 if ("-b" in sys.argv) else 0

filename = sys.argv[argc-2]
search_string = sys.argv[argc-1]

out = "Looking for '%s'  in '%s'" %(search_string , filename)
print out


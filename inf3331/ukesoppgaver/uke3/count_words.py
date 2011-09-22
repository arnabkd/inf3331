#!/usr/bin/env python
import sys
argc = len(sys.argv)

def printusage():
    print "Usage : python count_words.py <textfile> <search-string>"
    print "For case-insensitive search, add -i before textfile"
    print "To keep word-boundaries, add -b before textfile"

#Checking that arguments are correct
#Assuming that users insert arguments in the correct order (but order of -i and -b do not matter)
# argv = ['count_words.py' , args.. , 'filename' 'search-string']
if (argc < 3 or argc > 5):
    printusage()
    sys.exit()

insensitive = 1 if ("-i" in sys.argv) else 0
boundaries = 1 if ("-b" in sys.argv) else 0

filename = sys.argv[argc-2]
search_string = sys.argv[argc-1]

ifile = open (filename, 'r')
sum = 0

for line in ifile:
    if(insensitive):
		line = line.lower()
		search_string = search_string.lower()
    if(boundaries):
		for word in line.split():
	    	i = 1 if (word.strip('.') == search_string) else 0
	    	sum += i
    else:
		sum += line.count(search_string)



res = "Number of occurences of string '%s' in '%s' : %d" %(search_string , filename , sum)
print res
sys.exit()

#Kjoreeksempler :
#arnabkd@spes ~/Desktop/uni/inf3331/inf3331/ukesoppgaver/uke3 $ python count_words.py  football.txt ball
#Number of occurences of string 'ball' in 'football.txt' : 3

#arnabkd@spes ~/Desktop/uni/inf3331/inf3331/ukesoppgaver/uke3 $ python count_words.py -i football.txt goal
#Number of occurences of string 'goal' in 'football.txt' : 3

#arnabkd@spes ~/Desktop/uni/inf3331/inf3331/ukesoppgaver/uke3 $ python count_words.py -i -b football.txt goal
#Number of occurences of string 'goal' in 'football.txt' : 2

#arnabkd@spes ~/Desktop/uni/inf3331/inf3331/ukesoppgaver/uke3 $ python count_words.py -b football.txt goal
#Number of occurences of string 'goal' in 'football.txt' : 1

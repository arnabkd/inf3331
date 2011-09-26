#Arnab Kumar Datta - Week 4
#!/usr/bin/env python

import sys,re

try:
    filename = open(sys.argv[1], 'r')
except :
    print "file not found"


def gettime():

    rex2 = 'Date/Time    : (\d+):(\d+):(\d+)\s(\d+):(\d+):(\d+)\n'
    for line in filename:
        try:
            return re.search(rex2,line).groups()
        except:
            x = 1
            
def prefix(originalname, date_time_info):
    try:
        return date_time_info[0]+"_"+date_time_info[1]+"_"+date_time_info[2]+"__"+date_time_info[3]+"_"+date_time_info[4]+"_"+date_time_info[5]+"__"+originalname
    except:
        return "invalid input"

print prefix("img_4938.jpg", gettime())


#Runtime example
#arnabkd@defiance ~/Desktop/uni/inf3331/inf3331/ukesoppgaver/uke4 $ python jpegrename.py sample.txt 
#2002_05_19__18_10_03__img_4938.jpg

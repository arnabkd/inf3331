#!/usr/bin/env python
import sys

# sys.argv looks like this : [inverseconvert.py] [outfile] [stepsize] [infile1] [infile2] [infile3]
outfile = sys.argv[1]
stepsize = sys.argv[2]
filenames = [sys.argv[3] , sys.argv[4] , sys.argv[5]]

content = []

#Add content :
for x in range (3):
    filecontent = [] #each file has some content
    ins = open (filenames[x] , "r")
    
    for line in ins:
        line = line.rstrip('\n')
        value  = line.split()[1] #get the second column of the line
        value = float(value)
        filecontent.append (value)
    
    content.append(filecontent) #append filecontent from each file
    
    
#content is now a 2-dimensional list. 
#Time to open our output file and write the information to it
out = open(outfile, "w")
out.write('Some comment\n')
out.write(stepsize)
out.write('\n')

#Write column headers
for name in filenames:
    out.write(name.rstrip('.dat'))
    out.write ("  ")
out.write('\n')


#Write table data 
for x in range(len (content)):
    for y in range (len (content)):
        out.write (str(content[y][x]))
        out.write ("               ")
    out.write('\n')


out.close()

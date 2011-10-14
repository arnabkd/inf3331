#Task 6.3 arnabkd (Arnab Kumar Datta)
import sys
try:
    boo = sys.argv[1].split('.py')[0]
    boo = __import__(boo)
    
    outfilename = sys.argv[2]
    output =  boo.foo(sys.argv[3], sys.argv[4])

    src = open(sys.argv[1], 'r')
    out = open(outfilename, 'w')
    for line in src:
	out.write(line)
    src.close()
    out.write('\n')
    
    out.write('\"\"\" \n')
    out.write('Run time example:\n')

    out.write('python'+ sys.argv[1] + ' '+ sys.argv[3] + ' ' + sys.argv[4]+ '\n')

    out.write(str(output) + '\n')
    
    out.write('\"\"\"')
    out.close()
except:
    print "error"


#Runtime example
#arnabkd@bounty ~/Desktop/uni/inf3331/inf3331/ukesoppgaver/uke6 $ python test2.py bar.py assign#ment.txt 100 150
#arnabkd@bounty ~/Desktop/uni/inf3331/inf3331/ukesoppgaver/uke6 $ more assignment.txt 
#!/usr/bin/env python

#def foo(arg1, arg2):
#        return int(arg1) + int(arg2)


#if __name__ == "__main__":
#    import sys
#    print foo(sys.argv[1], sys.argv[2])
#""" 
#Run time example:
#pythonbar.py 100 150
#250
#"""

import subprocess,sys
# import sys

 # def automate_output(src,  arglist):
	 # proc = subprocess.Popen(['python', src, arglist], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	 # print(proc.communicate()[0])

# def print_to_file (src, outfile, arglist):
	# print "printing to file %s" %(outfile)
	# out = open(outfile, 'w')
	# s = open(src, 'r')
	
	# for line in s:
		# out.write(line)
	# s.close()
	
	# out.write(" \"\"\"\n Run time example: \n")	
	# out.write(automate(src, arglist))
	# out.write(" \"\"\"\n")
	# out.close()
	

# try: 
	# src = sys.argv[1]
	# outfile = sys.argv[2]
	# arglist = sys.argv[3:]
	# automate(src, arglist)
	# print_to_file(src,outfile,arglist)	
# except:
	# print "error"
	# print "usage : python automate_runtime.py scriptname outfile args"





src = 'bar.py'
args = ['2' , '3']

def cmd_output(args, **kwds):
  kwds.setdefault("stdout", subprocess.PIPE)
  kwds.setdefault("stderr", subprocess.STDOUT)
  p = subprocess.Popen(args, **kwds)
  return p.communicate()[0]


print cmd_output(src, list(args))
# proc = subprocess.Popen(['python', src,  list(args)], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
# print proc.communicate()[0]
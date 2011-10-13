#Arnab Kumar Datta (arnabkd)
#Task 5.1

import os

def findprograms(prog_list):
	progs_found = {}
	for prog in prog_list:
		progs_found[prog] = None #set the path to none for all programs that we are searching for (we don't know where they are installed)
	paths = os.getenv("PATH").split(os.pathsep)

	for path in paths:
		apps_in_path = os.listdir(path)
		for app in prog_list:
			if app in apps_in_path:	progs_found[app] = path
	return progs_found


#################################################################################################################
#                                               Test Code                                                       # 
#################################################################################################################
programs = {
	'gnuplot'  : 'plotting program',
	'gs'	   : 'ghostscript, ps/pdf interpreter and previewer',
	'f2py'	   : 'generator for Python interfaces to F77',
	'swig'	   : 'generator for Python interfaces to C/C++',
	'convert'  : 'image conversion, part of the ImageMagick package',
	'xemacs'   : 'xemacs - does not exist on login servers'
	}
installed = findprograms(programs.keys())

for program in installed.keys():
	if installed[program]:
		print "You have %s (%s)" % (program, programs[program])
	else:
		print "*** Program %s was not found on the system" % (program,)


# Runtime example
#arnabkd@speedwell ~/Desktop/uni/inf3331/inf3331/ukesoppgaver/uke5 $ python findprograms.py 
#You have convert (image conversion, part of the ImageMagick package)
#You have gs (ghostscript, ps/pdf interpreter and previewer)
#You have gnuplot (plotting program)
#You have swig (generator for Python interfaces to C/C++)
#You have f2py (generator for Python interfaces to F77)
#*** Program xemacs was not found on the system

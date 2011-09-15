import re #was missing import statement

#Numbers were not grouped properly together when in scientific notation format
#Added () around (\d+(\.\d*)?|\d*\.\d+)([eE][+\-]?\d+)?
real = \
 r"\s*(?P<number>-?((\d+(\.\d*)?|\d*\.\d+)([eE][+\-]?\d+)?))\s*"
c = re.compile(real)
some_interval = "[3.58652e+05 , 6E+09]"
groups = c.findall(some_interval)
lower = float(groups[0][c.groupindex['number']]) #1 changed to 0
upper = float(groups[1][c.groupindex['number']]) #2 changed to 1

print "%.5e" %lower
print "%.5e" %upper

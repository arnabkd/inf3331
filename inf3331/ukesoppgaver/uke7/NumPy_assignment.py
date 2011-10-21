#Arnab Kumar Datta  (arnabkd) - Task 7.2
from scitools.numpytools import *

x = sequence(0, 1, 0.5)

#y = 2*x + 1
y = x.copy();  y*=2;  y += 1
#z = 4*x - 4
z = x.copy();  z*=4;  z -= 4
print x, y, z

#The fix is to copy the numpy array instead of setting y = x
#arnabkd@stcroix ~/Desktop/uni/inf3331/inf3331/ukesoppgaver/uke7 $ python NumPy_assignment.py 
#[ 0.   0.5  1. ] [ 1.  2.  3.] [-4. -2.  0.]

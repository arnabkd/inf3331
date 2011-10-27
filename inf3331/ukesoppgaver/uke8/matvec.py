#Task 8.1 - Arnab Kumar Datta (arnabkd)
from numpy import *

A = array([[1,2,3],[4,5,7],[6,8,10]],float)
b = array([-3,-2,-1],float)


print "A"
print A
print "b"
print b
print "Matrix * Vector product of A and b is : "
print inner(A,b)

#Runtime example
#arnabkd@starrenburg ~/Desktop/uni/inf3331/inf3331/ukesoppgaver/uke8 $ python m#atvec.py 
#A
#[[  1.   2.   3.]
# [  4.   5.   7.]
# [  6.   8.  10.]]
#b
#[-3. -2. -1.]
#Matrix * Vector product of A and b is : 
#[-10. -29. -44.]

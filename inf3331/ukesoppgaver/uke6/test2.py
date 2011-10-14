import sys
# from subprocess import *

# args = sys.argv[1:]
# src = 'bar.py'
print sys.argv[1]
print sys.argv[2]
# import bar; print 'via import',; bar.foo(sys.argv[1], sys.argv[2])
import bar; print 'via import',; bar.foo(sys.argv[1],sys.argv[2])

# bar.main(args.split(' '))

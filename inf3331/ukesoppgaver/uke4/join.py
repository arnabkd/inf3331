"""
 Perl-style join with a delimiter and args can be an arbitary mixture of strings, lists, tuples
 @param delim
 @param args
 @returns list
"""
def join(delim, *args):    
    list = []
    for arg in args:
        if (type(arg).__name__ == 'list' or type(arg).__name__ == 'tuple'):
            for word in arg:
                list.append(word)
                list.append(delim)
	elif (type(arg) == str):
	    list.append(arg)
	    list.append(delim)
    return list


list1 = ['s1','s2','s3']
tuple1 = ('s4', 's5')

ex1 = join(' ', 't1', 't2', list1, tuple1, 't3', 't4')
ex2 = join('  #  ', list1, 't0')
print ex1
print ex2

#Runtime example - printed out ex1 and ex2. This is a list, so it does not look exactly like the task specifies
#arnabkd@defiance ~/Desktop/uni/inf3331/inf3331/ukesoppgaver/uke4 $ python join.py 
#['t1', ' ', 't2', ' ', 's1', ' ', 's2', ' ', 's3', ' ', 's4', ' ', 's5', ' ', 't3', ' ', 't4', ' ']
#['s1', '  #  ', 's2', '  #  ', 's3', '  #  ', 't0', '  #  ']

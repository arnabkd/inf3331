# map() takes two (or more) arguments, a function and a list to apply the function to
# lambda can be put anywhere a function is expected
# map() calls lambada for every element in the self list
# since Vector has overloaded __getitem__ and __len__ definitions
# the Vector object can be considered a list
# the lambda function adds each other item to each item in the list
# note this only adds objects that can typicaly be added by python


class Vector:

	def __init__(self, data):		
		self.data = data



	# overload print
	# repr returns a string containing a printable representation of an object
	# otherwise printing a Vector object would look like:
	#<__main__.Vector instance at 0x0000000017A9DF48>
	def __repr__(self):		
		return repr(self.data)

	# overload +
	def __add__(self, other):		
		return Vector(map(lambda x, y: x+y, self, other))

	# overload -
	def __sub__(self, other):		
		return Vector(map(lambda x, y: x-y, self, other))

	# overload /
	def __div__(self, other):		
		return Vector(map(lambda x, y: x/y, self, other))

	# overload *
	def __mul__(self, other):		
		return Vector(map(lambda x, y: x*y, self, other))

	# overload %
	def __mod__(self, other):		
		return Vector(map(lambda x, y: x%y, self, other))

	# overload []
	def __getitem__(self, index):		
		return self.data[index]

	# overload set []
	def __setitem__(self, key, item):		
		self.data[key] = item

	# return size to len()
	def __len__(self):		
		return len(self.data)
		


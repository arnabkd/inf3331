# map() takes two (or more) arguments, a function and a list to apply the function to
# lambda can be put anywhere a function is expected
# map() calls lambada for every element in the self list
# since Vector has overloaded __getitem__ and __len__ definitions
# the Vector object can be considered a list
# the lambda function adds each other item to each item in the list
# note this only adds objects that can typicaly be added by python

# print statements added to show what is getting called
class Vector:

	def __init__(self, data):
		print "__init__"
		self.data = data

	def __call__(self, varA, varB):
		print "__call__"
		print "do something with ", varA, " and ", varB

	# overload print
	# repr returns a string containing a printable representation of an object
	# otherwise printing a Vector object would look like:
	#<__main__.Vector instance at 0x0000000017A9DF48>
	def __repr__(self):
		print "__repr__"
		return repr(self.data)

	# overload +
	def __add__(self, other):
		print "__add__"
		return Vector(map(lambda x, y: x+y, self, other))

	# overload -
	def __sub__(self, other):
		print "__sub__"
		return Vector(map(lambda x, y: x-y, self, other))

	# overload /
	def __div__(self, other):
		print "__div__"
		return Vector(map(lambda x, y: x/y, self, other))

	# overload *
	def __mul__(self, other):
		print "__mul__"
		return Vector(map(lambda x, y: x*y, self, other))

	# overload %
	def __mod__(self, other):
		print "__mod__"
		return Vector(map(lambda x, y: x%y, self, other))

	# overload []
	def __getitem__(self, index):
		print "__getitem__"
		return self.data[index]

	# overload set []
	def __setitem__(self, key, item):
		print "__setitem__"
		self.data[key] = item

	# return size to len()
	def __len__(self):
		print "__len__"
		return len(self.data)
vecA = Vector([1, 0, 0])
print vecA
vecB = vecA + vecA
print vecB

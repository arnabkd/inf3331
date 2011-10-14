class Vec3D:

	def __init__(self, attrlist):		
		self.attributes = attrlist

	def __repr__(self):		
		classname = self.__class__.__name__
		return '%s%s' %(classname, repr(self.attributes))

	# overload +
	def __add__(self, other):		
		return Vec3D(map(lambda x, y: x+y, self, other))

	# overload -
	def __sub__(self, other):		
		return Vec3D(map(lambda x, y: x-y, self, other))

	# dot product
	def __mul__(self, other):		
		return Vec3D(map(lambda x, y: x*y, self, other))

	#subscripting with assignment
	def __setitem__(self, index, item):		
		self.attributes[index] = item
	
	#subscripting
	def __getitem__(self, index):
		return self.attributes[index] 
		
	# return size to len()
	def __len__(self):		
		return 42
		
u = Vec3D([1,0,1])
v = Vec3D([0,1,0])
str(u)
print len(u)
u[1] = 5
print u
import math
	
class Vec3D(object):

	def __init__(self, x,y,z):
		self.attributes = [x,y,z]	
	
	#pretty print
	def __str__(self):
		return str(self.attributes)
	
	#override repr
	def __repr__(self):
		classname = self.__class__.__name__
		return '%s%s' %(classname, repr(self.attributes))
		
	#Eucledian norm	
	def len(self):
		sq_list =  map(lambda x, y: x*y, self.attributes, self.attributes)
		return math.sqrt(sum(sq_list))	
		
	#subscripting 
	def __getitem__(self, index):		
		return self.attributes[index]
	
	#subscripting with assignment
	def __setitem__(self, index, value):		
		self.attributes[index] = value
	
	#override ** (cross product)
	def __pow__(self,other):
		vec1 = self.attributes;	vec2 = other.attributes
		x = vec1[1] * vec2[2] - vec2[1] * vec1[2]
		y = vec1[2] * vec2[0] - vec2[2] * vec1[0]
		z = vec1[0] * vec2[1] - vec2[0] * vec1[1]		
		return Vec3D(x,y,z)
		
	#override + (vector+scalar addition)
	def __add__(self,other):	
		if(isinstance(other, Vec3D)):
			res = map(lambda x,y: x+y, self.attributes , other.attributes)	
		else:
			res = map(lambda x: x+other, self.attributes)
		return Vec3D(res[0], res[1], res[2])
	
	#override - (vector/scalar subtraction)
	def __sub__(self,other):
		if(isinstance(other, Vec3D)):
			res = map(lambda x,y: x-y, self.attributes , other.attributes)	
		else:
			res = map(lambda x: x - other, self.attributes)
		return Vec3D(res[0], res[1], res[2])
		
	def __mul__(self,other):
		if(isinstance(other, Vec3D)):
			res = map(lambda x,y: x*y, self.attributes, other.attributes)
		else:
			res = map(lambda x: x * other, self.attributes)
		return sum(res)
		
	#override float + Vec3D - will be called if float does not have __add__(y) with y being an instance of Vec3D 
	def __radd__(self , other):
		return self + other
	
	#override float-Vec3D - will be called if float does not have __sub__(y) with y being an instance of Vec3D 
	def __rsub__(self,other):
		return self - other
	
	#override float-Vec3D - will be called if float does not have __mul__(y) with y being an instance of Vec3D 
	def __rmul__(self,other):
		return self * other
	
	
	#override vec3d / float 
	def __div__(self,other):
		return map(lambda x: x / other, self.attributes)
		
	
#Runtime code
u = Vec3D(1, 0, 0)
v = Vec3D(0, -0.2, 8)		
a = 1.2

print "vector addition", u+v
print "scalar and vector addition", a+v
print "vector and scalar addition", v+a

print "vector and scalar subtraction", v-a
print "scalar and vector subtraction", a-v

print "vector and scalar multiplication", v*a
print "scalar and vector multiplication", a*v

print "vector by scalar division", v/a





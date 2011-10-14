import math
	
class Vec3D(object):

	def __init__(self, x,y,z):
		self.attributes = [x,y,z]	
	
	def __str__(self):
		return str(self.attributes)
			
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
	
	#override pow (cross product)
	def __pow__(self,other):
		vec1 = self.attributes;	vec2 = other.attributes
		x = vec1[1] * vec2[2] - vec2[1] * vec1[2]
		y = vec1[2] * vec2[0] - vec2[2] * vec1[0]
		z = vec1[0] * vec2[1] - vec2[0] * vec1[1]		
		return Vec3D(x,y,z)
		
	#override + (vector addition)
	def __add__(self,other):	
		res = map(lambda x,y: x+y, self.attributes , other.attributes)		
		return Vec3D(res[0], res[1], res[2])
	
	#override - (vector subtraction)
	def __sub__(self,other):
		res = map(lambda x,y: x-y, self.attributes , other.attributes)		
		return Vec3D(res[0], res[1], res[2])
		
	def __mul__(self,other):
		res = map(lambda x,y: x*y, self.attributes, other.attributes)
		return sum(res)
		
#Runtime code		
u = Vec3D(1,0,0)
v = Vec3D(0,1,0)

print str(u)
print repr(u)
print "Eucledian norm" , u.len()
print "subscripting -> u[1]", u[1]
v[2] = 2.5
print "subscripting with assignment -> v[2]=",v[2]
print "cross product u**v",u**v
print "vector addition: u+v",u+v
print "dot product:", u*v

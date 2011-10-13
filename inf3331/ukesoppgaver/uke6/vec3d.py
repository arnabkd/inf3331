import math

class Vec3D:
    def __init__(self, x,y,z):
       self.data = [x,y,z]
    
    def __repr__(self):
        classname = self.__class__.__name__
        return '%s %s' %(classname, self.data)

    def __str__(self):
       return self.data


    def len(self):
        return math.sqrt(math.pow(self.getX(),2) + math.pow(self.getY(),2) + math.pow(self.getZ(),2))

    #def __add__(self, other):
     #   return Vec3D(map(lambda x,y: x+y, self, other))

u = Vec3D(1,0,1)
v = Vec3D(0,1,0)

print u
#print u+v

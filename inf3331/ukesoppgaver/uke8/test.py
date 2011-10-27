class C:
    def __init__(self, dx = 1):
        self._dx = dx
    def get_dx(self):
        return self._dx
    def set_dx(self,val):
        pass
    def del_dx(self):
        pass

    dx = property(get_dx,None,None)

c = C()
c.dx = 42
print c.dx


class RadiusVector:
    def __init__(self,*args):
        self.coords=list(args)

    def __getitem__(self,item):
        if type(item)==int:
            return self.coords[item]
        else:
            return slice(self.coords)

    def __setitem__(self,item,val):
        if type(item)==int:
            self.coords[item]=val
        else:
            print(item.start)
            # self.coords[slice(item)]=val

v = RadiusVector(1, 1, 1, 1)
print(v[1]) # 1
v[:] = 1, 2, 3, 4
print(v[2]) # 3
print(v[1:]) # (2, 3, 4)
v[0] = 10.5
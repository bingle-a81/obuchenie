class RadiusVector:
    def __init__(self,*args) -> None:
        if len(args)==1:
            self.coords=[0]*args[0]
        else:
            self.coords=args

    def set_coords(self,*args):
        a=min(len(self.coords),len(args))
        ab=list(self.coords)
        ab[:a]=args[:a]
        self.coords=tuple(ab)

    def get_coords(self):
        return tuple(self.coords)
    
    def __len__(self):
        return len(self.coords)
    
    def __abs__(self):
        return sum(map(lambda x:x*x,self.coords))**0.5
    
vector3D = RadiusVector(3)
vector3D.set_coords(3, -5.6, 8)
a, b, c = vector3D.get_coords()
vector3D.set_coords(3, -5.6, 8, 10, 11) # ошибки быть не должно, последние две координаты игнорируются
vector3D.set_coords(1, ) # ошибки быть не должно, меняются только первые две координаты
print(vector3D.get_coords())
res_len = len(vector3D) # res_len = 3
res_abs = abs(vector3D)
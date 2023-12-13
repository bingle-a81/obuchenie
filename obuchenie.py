
class Vector:
    def __init__(self,*args) -> None:
        self.vectors=list(args)

    def __add__(self,other):
        l=min(len(self.vectors),len(other.vectors))
        return Vector(*list(map(lambda x,y:x+y,self.vectors[:l],other.vectors[:l])))
 

a=Vector(1,2,3)  
b=Vector(3,4,5,6)
c=a+b
print(c.vectors)

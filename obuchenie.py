
class Vector:
    def __init__(self,*args) -> None:
        self.vectors=list(args)
        

    def __add__(self,other):
        if len(self.vectors)!=len(other.vectors):
            raise ArithmeticError('размерности векторов не совпадают')
        return Vector(*list(map(lambda x,y:x+y,self.vectors,other.vectors)))
 
    def __iadd__(self,other):
        if isinstance(other,Vector):
            if len(self.vectors)!=len(other.vectors):
                raise ArithmeticError('размерности векторов не совпадают')        
            self.vectors=list(map(lambda x,y:x+y,self.vectors,other.vectors))
        else:
            self.vectors=list(map(lambda x:x+other,self.vectors))
        return self



    def __sub__(self,other):
        if len(self.vectors)!=len(other.vectors):
            raise ArithmeticError('размерности векторов не совпадают')
        return Vector(*list(map(lambda x,y:x-y,self.vectors,other.vectors)))
    
    def __isub__(self,other):
        if isinstance(other,Vector):
            if len(self.vectors)!=len(other.vectors):
                raise ArithmeticError('размерности векторов не совпадают')        
            self.vectors=list(map(lambda x,y:x-y,self.vectors,other.vectors))
        else:
            self.vectors=list(map(lambda x:x-other,self.vectors))
        return self

    def __mul__(self,other):
        if len(self.vectors)!=len(other.vectors):
            raise ArithmeticError('размерности векторов не совпадают')
        return Vector(*list(map(lambda x,y:x*y,self.vectors,other.vectors)))

    def __eq__(self, other) -> bool:
        return all(map(lambda x,y:x==y,self.vectors,other.vectors))

    # def __imul__(self,other):
    #     if isinstance(other,Vector):
    #         if len(self.vectors)!=len(other.vectors):
    #             raise ArithmeticError('размерности векторов не совпадают')        
    #         self.vectors=list(map(lambda x,y:x*y,self.vectors,other.vectors))
    #     else:
    #         self.vectors=list(map(lambda x:x*other,self.vectors))
    #     return self 
    

v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
print((v1 + v2).vectors)  # [5, 7, 9]
print((v1 - v2).vectors)  # [-3, -3, -3]
print((v1 * v2).vectors)  # [4, 10, 18]

v1 += 10
print(v1.vectors)  # [11, 12, 13]
v1 -= 10
print(v1.vectors)  # [1, 2, 3]
v1 += v2
print(v1.vectors)  # [5, 7, 9]
v2 -= v1
print(v2.vectors)  # [-1, -2, -3]

print(v1 == v2)  # False
print(v1 != v2)  # True

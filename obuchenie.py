class NewList:
    def __init__(self,ls:list=None) -> None:
        if ls is None:
            self.ls=[]
        else:
            self.ls=list(ls)

    def __str__(self) -> str:
        return ' '.join([str(x) for x in self.ls])

    def get_list(self):
        return self.ls

    def __pop(self,a,b):
        for x in b:
            if x in a:
                if type(x)==type(a[a.index(x)]):
                    del(a[a.index(x)])
                else:
                    continue
        return a


    def __sub__(self,other):
        if isinstance(other,NewList):
            b=other.ls
        elif isinstance(other,list):
            b=other
        else:
            TypeError
        a=list(self.ls)
        return NewList(self.__pop(a,b))


      
    
    def __rsub__(self,other):
        a=list(self.ls)
        return NewList(self.__pop(other,a))

    def __isub__(self,other):
        if isinstance(other,NewList):
            b=other.ls
        elif isinstance(other,list):
            b=other
        else:
            TypeError
        a=list(self.ls)
        return NewList(self.__pop(a,b))

                

lst = NewList()
lst1 = NewList([0, 1, -3.4, "abc", True])
lst2 = NewList([1, 0, True])


assert lst1.get_list() == [0, 1, -3.4, "abc", True] and lst.get_list() == [], "метод get_list вернул неверный список"
res1 = lst1 - lst2
res2 = lst1 - [0, True]
(print(res2))
res3 = [1, 2, 3, 4.5] - lst2
lst1 -= lst2

assert res1.get_list() == [-3.4, "abc"], "метод get_list вернул неверный список"
assert res2.get_list() == [1, -3.4, "abc"], "метод get_list вернул неверный список"

assert res3.get_list() == [2, 3, 4.5], "метод get_list вернул неверный список"
assert lst1.get_list() == [-3.4, "abc"], "метод get_list вернул неверный список"

lst_1 = NewList([1, 0, True, False, 5.0, True, 1, True, -7.87])
lst_2 = NewList([10, True, False, True, 1, 7.87])
res = lst_1 - lst_2
assert res.get_list() == [0, 5.0, 1, True, -7.87], "метод get_list вернул неверный список"

a = NewList([2, 3])
res_4 = [1, 2, 2, 3] - a # NewList: [1, 2]
assert res_4.get_list() == [1, 2], "метод get_list вернул неверный список"
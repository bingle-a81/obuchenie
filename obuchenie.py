class StackObj:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
    @property
    def next(self):
        return self.__next
    @next.setter
    def next(self,val):
        self.__next=val

class Stack:
    def __init__(self) -> None:
        self.top=None

    def __getitem__(self,item):
        if 0>item or item>len(self)-1:
            raise IndexError('неверный индекс')
        n=self.top
        i=0
        while i<item:
            n=n.next
            i+=1
        return n
    
    def __setitem__(self,item,obj:StackObj):
        if 0>item or item>len(self)-1:
            raise IndexError('неверный индекс')       
        n=self.top
        i=0
        while i<item:
            n=n.next
            i+=1
        n.data=obj.data     


    def push(self, obj:StackObj):
        if self.top is None:
            self.top=obj
            return
        n=self.top
        while n.next is not None:
            n=n.next
        n.next=obj
        return  
    
    def pop(self):
        if self.top is None:
            raise ValueError
        if self.top.next is None:
            self.top=None
            return
        else:
            n=self.top
            while n.next is not None:
                a=n
                n=n.next
            a.next=None
            return n
        

    def __len__(self):
        i=0
        n=self.top
        while n:
            i+=1
            n=n.next
        return i      
    
st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
st[1] = StackObj("new obj2")
print(st[2].data) # obj3
print(st[1].data) # new obj2



st = Stack()
st.push(StackObj("obj11"))
st.push(StackObj("obj12"))
st.push(StackObj("obj13"))
st[1] = StackObj("obj2-new")
assert st[0].data == "obj11" and st[1].data == "obj2-new", "атрибут data объекта класса StackObj содержит неверные данные"

try:
    obj = st[3]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

obj = st.pop()
assert obj.data == "obj13", "метод pop должен удалять последний объект стека и возвращать его"

n = 0
h = st.top
while h:
    assert isinstance(h, StackObj), "объект стека должен быть экземпляром класса StackObj"
    n += 1
    h = h.next
    
assert n == 2, "неверное число объектов в стеке (возможно, нарушена его структура)"

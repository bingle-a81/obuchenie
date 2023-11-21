class StackObj:
    def __init__(self,data):
        self.__data = data
        self.__next = None

    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self,data):
        print(data)
        self.__data = data

    @property
    def next(self):
        return self.__next
    
    @next.setter
    def next(self,next):
        if  isinstance(next,(StackObj)) or next is None:
            self.__next = next

            

class Stack:
    def __init__(self):
        self.top = None

    def push(self,obj:StackObj):
        if self.top is None:
            self.top = obj  
            return
        n=self.top
        while n.next :
            n=n.next      
        n.next=obj      

    def pop(self):
        if self.top is None:
            return []
        
        if self.top.next is None:
            a=self.top
            self.top=None
            return a
        else:
            n = self.top
            n1=self.top
            while n.next :                
                n1=n
                n=n.next
            a=n
            n1.next=None
            return a
        
    def get_data(self):
        a=[]
        if self.top is None:
            return []
        else:            
            n = self.top
            a.append(n.data)
            while n.next :   
                n=n.next             
                a.append(n.data)                
            return a

s = Stack()

top = StackObj("obj_1")
s.push(top)
s.push(StackObj("obj_2"))
s.push(StackObj("obj_3"))
s.pop()

res = s.get_data()
assert res == ["obj_1", "obj_2"], f"метод get_data вернул неверные данные: {res}"
assert s.top == top, "атрибут top объекта класса Stack содержит неверное значение"

h = s.top
while h:
    res = h.data
    h = h.next

s = Stack()
top = StackObj("obj_1")
s.push(top)
s.pop()
assert s.get_data() == [], f"метод get_data вернул неверные данные: {s.get_data()}"

n = 0
h = s.top
while h:
    h = h.next
    n += 1
    
assert n == 0, "при удалении всех объектов, стек-подобная стурктура оказалась не пустой"

s = Stack()
top = StackObj("name_1")
s.push(top)
obj = s.pop()
assert obj == top, "метод pop() должен возвращать удаляемый объект"
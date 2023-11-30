class ObjList:
    def __init__(self,data,next=None,prev=None):
        self.data=data
        self.next=next
        self.prev=prev

    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self,data):
        self.__data=data

    @property
    def next(self):
        return self.__next
    @next.setter
    def next(self, obj):
        self.__next = obj

    @property
    def prev(self):
        return self.__prev
    @prev.setter
    def prev(self, obj):
        self.__prev = obj

       

 

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def __len__(self):
        i=0
        n=self.head
        while n:
            i+=1
            n=n.next
        return i       

    def add_obj(self, obj:ObjList):
        if self.head is None:
            self.head=obj
            self.tail=obj
            return
        n=self.head
        while n.next is not None:
            n=n.next
        new_obj=obj
        n.next=new_obj
        self.tail=new_obj
        new_obj.prev=n
        return  

    def remove_obj(self,indx):
        if indx>(len(self)-1):
            raise IndexError
        if indx==0:
            if self.head.next is None:
                self.head = None
                self.tail = None
                return
            self.head = self.head.next
            if self.head.next is None:
                self.tail=self.head
            self.head.prev = None
            return
        i=1
        n = self.head.next
        while i<indx:
            i+=1
            n=n.next
        if n.next is None:
            n.prev.next=None
            self.tail=n.prev
        else:
            n.prev.next=n.next
            n.next.prev=n.prev




    def get_data(self):
        d=[]
        if self.head is None:
            return []
        else:
            n=self.head
            d.append(n.data)
            while n.next:
                n=n.next
                d.append(n.data)
        return d



    def __call__(self, indx) :
        if indx>(len(self)-1):
            raise IndexError
        i=0
        n=self.head      
        while i<indx:
            i+=1            
            n=n.next
            a=n.data
        return a       

  
  
ln = LinkedList()
ln.add_obj(ObjList("Сергей"))
ln.add_obj(ObjList("Балакирев"))
ln.add_obj(ObjList("Python ООП"))
ln.remove_obj(2)
assert len(ln) == 2, "функция len вернула неверное число объектов в списке, возможно, неверно работает метод remove_obj()"
ln.add_obj(ObjList("Python"))


assert ln(2) == "Python", "неверное значение атрибута __data, взятое по индексу"
assert len(ln) == 3, "функция len вернула неверное число объектов в списке"

assert ln(1) == "Балакирев", "неверное значение атрибута __data, взятое по индексу"

n = 0
h = ln.head
while h:
    assert isinstance(h, ObjList)
    h = h._ObjList__next
    n += 1

assert n == 3, "при перемещении по списку через __next не все объекты перебрались"

n = 0
h = ln.tail
while h:
    assert isinstance(h, ObjList)
    h = h._ObjList__prev
    n += 1

assert n == 3, "при перемещении по списку через __prev не все объекты перебрались"
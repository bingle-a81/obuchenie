class StackObj:
    def __init__(self,data,next=None):
        self.__data = data
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
            return
        

    def __len__(self):
        i=0
        n=self.top
        while n:
            i+=1
            n=n.next
        return i      
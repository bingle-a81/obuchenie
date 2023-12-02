class StackObj:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self) -> None:
        self.top=None

    def push_back(self, obj:StackObj):
        if self.top is None:
            self.top=obj
            return
        n=self.top
        while n.next is not None:
            n=n.next
        n.next=obj
        return  
    
    def pop_back(self):
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


st = Stack()
st.push_back(StackObj('jj'))
st.push_back(StackObj('jj'))
st.push_back(StackObj('jj'))
st.push_back(StackObj('jj'))
st.pop_back()
print(len(st))
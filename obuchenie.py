class StackObj:
    def __init__(self,data,next=None):
        self.__data = data
        self.__next = next

class Stack:
    def __init__(self) -> None:
        self.__top=None

    def push_back(self, obj:StackObj):
        if self.__top==None:
            self.__top=obj
            print(self.__top.next)
        else:
            self.__top.next=obj

            # n=self.__top
            # print(self.__top)
            # while n:
            #     n=n.next
            # n.next=obj


st = Stack()
st.push_back(StackObj('jj'))
st.push_back(StackObj('jj'))
print(st)
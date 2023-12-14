class Record :
    def __init__(self,**kwargs) -> None:
        self.__dict__.update(kwargs)
        

    def __getitem__(self,item):
        if item>len(self.__dict__)-1:
            raise IndexError('неверный индекс поля') 
        ls=list(self.__dict__.keys())       
        return self.__dict__.get(ls[item])

    def __setitem__(self,item,val):
        if item>len(self.__dict__)-1:
            raise IndexError('неверный индекс поля')
        ls=list(self.__dict__.keys())
        self.__dict__[ls[item]]=val
            


pk=1
print(type(pk))

r = (pk=1, title='Python ООП', author='Балакирев',pk1=1, title1='Python ООП', author1='Балакирев')
# r[0] = 2 # доступ к полю pk
# r[1] = 'Супер курс по ООП' # доступ к полю title
# r[2] = 'Балакирев С.М.' # доступ к полю author
# print(r.__dict__)
# print(r[1]) # Супер курс по ООП





list1 = [[1, 8, 7, 4], [1, 3, 4, 5], [2, 7, 2], [2, 6, 7, 8]]
list1.reverse()
print(list1)
class TreeObj:
    def __init__(self,indx:int,value=None,):
        self.indx = indx
        self.value = value
        self.__left=None
        self.__right=None

    @property
    def left(self):        
         return self.__left

    @left.setter
    def left(self,value):
        self.__left = value


    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self,value):
        self.__right = value


class DecisionTree :
    
    @classmethod
    def predict(cls, root, x):
        if root is None:
            return None
        n=root
        while n:
            obj_next=cls.get_next(n,x)
            if obj_next is None:
                break
            n=obj_next
        return n.value


    @classmethod
    def add_obj(cls, obj, node=None, left=True):
        if node:
            if left:
                node.left=obj
            else:
                node.right=obj
        return obj

    @classmethod
    def get_next(cls, obj:TreeObj, x):
        if x[obj.indx]==1:
            return obj.left
        else:
            return obj.right


# ВСЕ ПРОЦЕДУРЫ ПРОИСХОДЯТ через КЛАСС DecisionTree

# Класс DecisionTree через метод add_obj и передаваемый ему класс TreeObj
# с параметрами создает объект TreeObj со свойствами.

# В примере 3 объекта (это синие прямоугольники схемы)
# делаем ссылку на переменную занятой ЯЧЕЙИ ПАМЯТИ этого нового объекта, для того, чтобы данной созданный объект
# передавать (подкладывать) другому создаваемому объекту

# ИЗНАЧАЛЬНО ПЕРЕДАВАЕМЫЙ ИНДЕКС В ОБЪЕКТЫ ДОЛЖЕН СООТВЕТСТВОВАТЬ ИЕРАРХИИ СТРОЕНИЯ ДЕРЕВА, Т.Е. ИЕРАРХИИ
# СЛЕДОВАНИЯ ЭЛЕМЕНТОВ СПИСКА.
root = DecisionTree.add_obj(TreeObj(0))
print(type(root), root.__dict__)
print()
v_11 = DecisionTree.add_obj(TreeObj(1), root)
print(type(root), root.__dict__)
print(type(v_11), v_11.__dict__)
print()
v_12 = DecisionTree.add_obj(TreeObj(2), root, False)
print(type(root), root.__dict__)  # тут уже видно, что присвоились 2 ветки
print(type(v_11), v_11.__dict__)
print(type(v_12), v_12.__dict__)
# Эти 3 объекта существуют независимо друг от друга, но между ними есть ссылки
# друг на друга. НЕ ПУТАТЬ с односвязным списком, где объекты хоть и были независимые,
# НО ВОСПРИНИМАЛИСЬ МАТРЕШКОЙ объекта класса

# аналогично создаются еще 4 независимых объекта (рыжие прямоугольники). Тут объекты - СОЗДАВАЕМЫЕ
# ЯЧЕЙКИ ПАМЯТИ не присваиваем переменным как ссылки. Нет надобности им обращаться друг к другу.
# При создании ссылки подкладываются от ранее созданных объектов (синие прямоугольники)
DecisionTree.add_obj(TreeObj(-1, "будет программистом"), v_11)
DecisionTree.add_obj(TreeObj(-1, "будет кодером"), v_11, False)
DecisionTree.add_obj(TreeObj(-1, "не все потеряно"), v_12)
DecisionTree.add_obj(TreeObj(-1, "безнадежен"), v_12, False)

# здесь схема разбора(прохода) списка НЕ ПОСЛЕДОВАТЕЛЬНАЯ.
# СПИСОК - позиционная структура дерева. Где каждому индексу соответствует свой уровень объектов
# Если индекс 0 со значением 1, то переходим на индекс 1 и смотрим его значение (здесь 1)
# Ели индекс 0 со значением 0, то переходим сразу на индекс 2 и смотрим его значение (здесь 0)
x = [1, 1, 0]
res = DecisionTree.predict(root, x)

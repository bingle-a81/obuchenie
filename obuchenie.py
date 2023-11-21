list1 = [[1, 8, 7, 4], [1, 3, 4, 5], [2, 7, 2], [2, 6, 7, 8]]
list1.reverse()
print(list1)
class TreeObj:
    def __init__(self,indx,value=None,):
        self._indx = indx
        self.__value = value
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
        if x[root._indx] < root.value:
            return cls.predict(root.left, x)
        else:
            return cls.predict(root.right, x)

    @classmethod
    def add_obj(cls, obj, node=None, left=True):
        if node is None:
            node = TreeObj(obj)
        else:
            if obj[node._indx] < node.value:
                cls.add_obj(obj, node.left, False)
            else:
                cls.add_obj(obj, node.right, True)
        return node


root = DecisionTree.add_obj(TreeObj(0))
v_11 = DecisionTree.add_obj(TreeObj(1), root)
v_12 = DecisionTree.add_obj(TreeObj(2), root, False)
DecisionTree.add_obj(TreeObj(-1, "будет программистом"), v_11)
DecisionTree.add_obj(TreeObj(-1, "будет кодером"), v_11, False)
DecisionTree.add_obj(TreeObj(-1, "не все потеряно"), v_12)
DecisionTree.add_obj(TreeObj(-1, "безнадежен"), v_12, False)

x = [1, 1, 0]
res = DecisionTree.predict(root, x)

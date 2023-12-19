class Cell:
    def __init__(self,data) -> None:
        self.data=data


class SparseTable:
    def __init__(self,rows=0,cols=0) -> None:
        self.rows=rows
        self.cols=cols
        self.dict_={}

    def add_data(self,row, col, data):
        self.dict_[(row,col)]=data
        pass
        # raise IndexError('ячейка с указанными индексами не существует')

    def remove_data(self,row, col) :
        pass

    def __getitem__(self,item):
        pass

    def __setitem__(self,item,val):
        pass
    # raise ValueError('данные по указанным индексам отсутствуют')



st = SparseTable()
st.add_data(2, 5, Cell("cell_25"))
print(st.dict_)
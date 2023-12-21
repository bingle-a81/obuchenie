class Cell:
    def __init__(self,data) -> None:
        self.data=data

    @property
    def data(self):
        return self.data
    @data.setter
    def data(self,val):
        self.data=val

class TableValues:
    def __init__(self,rows, cols, type_data) -> None:
        self.rows=rows
        self.cols=cols
        self.type_data=type_data
        
    
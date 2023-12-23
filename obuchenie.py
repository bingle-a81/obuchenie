class Matrix:
    def __init__(self,*args) -> None:
        print(type(args))
        if type(args)==tuple:
            self._check(args)
            self.ls=list(args)
        else:
            self.rows=args[0]
            self.cols=args[1]
            self.fill_value=args[2]

    def _check(self,ls:tuple):
        f=[x*2 for row in ls for x in row]
        print(f)

        # if len(ls[0])!=len(ls[1]) and all(type(x) not in (int,float) for row in ls for x in row):
            # raise TypeError('список должен быть прямоугольным, состоящим из чисел')


mt = Matrix([[1, 2], [3, 4]])
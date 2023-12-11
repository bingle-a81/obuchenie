class Record:
    pk=0

    def __init__(self,fio, descr, old,) -> None:
        __class__.pk+=1
        self.pk=__class__.pk
        self.fio=fio
        self.descr=descr
        self.old=int(old)

    def __hash__(self) -> int:
        return hash((self.fio,self.old))

    def __eq__(self, __o: object) -> bool:
        return hash(self)==hash(__o)


class DataBase :

    def __init__(self,path) -> None:
        self.path=path
        self.dict_db ={}

    def write(self, record):
        self.dict_db.setdefault(record,[]).append(hash(record))


    def read(self, pk):
        pass
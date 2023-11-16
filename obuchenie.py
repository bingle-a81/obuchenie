class Data:
    def __init__(self,data:str,ip:int):
        self.data=data
        self.ip=ip

class Server :
    IP=0
    def __init__(self):
        self.IP=__class__.getIP()
        self.buffer=[]
        self.router=None


    @classmethod
    def getIP(cls)->str:
        cls.IP+=1
        return cls.IP  

    def send_data(self,data:Data):
        Router.buffer.append(data)


class Router :
    buffer=[]

    def link(self,server:Server):
        server.router=self

    def unlink(self,server:Server):
        server.router=None
    
    def send_data(self,data:Data):
        



    







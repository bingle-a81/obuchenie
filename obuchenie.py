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
    def getIP(cls)->int:
        cls.IP+=1
        return cls.IP  

    def send_data(self,data:Data):

        self.router.buffer.append(data)


    def get_data(self):
        a=self.buffer[:]
        self.buffer.clear()
        return a


    def   get_ip(self):
        return self.IP


class Router :
    def __init__(self) :
        self.buffer=[]
        self.servers=[]

    def link(self,server:Server):
        server.router=self
        self.servers.append(server)


    def unlink(self,server:Server):
        server.router=None
        self.servers.remove(server)
    
    def send_data(self):
        for data in self.buffer:
            for server in self.servers:
                if data.ip==server.get_ip():
                    server.buffer.append(data)
        self.buffer.clear()

# router = Router()
# sv_from = Server()

# router.link(sv_from)
# print(sv_from.router)
# router.unlink(sv_from)

# print(sv_from.router)


# quit (-1)  

# router = Router()
# sv_from = Server()
# sv_from2 = Server()

# router.link(sv_from)

# router.link(sv_from2)
# router.link(Server())
# router.link(Server())
# sv_to = Server()
# router.link(sv_to)
# sv_from.send_data(Data("Hello", sv_to.get_ip()))
# sv_from2.send_data(Data("Hello", sv_to.get_ip()))
# sv_from2.send_data(Data("Hello", sv_to.get_ip()))
# sv_from2.send_data(Data("Hello", sv_to.get_ip()))

# sv_to.send_data(Data("Hi", sv_from.get_ip()))
# router.send_data()


# msg_lst_from = sv_from.get_data()
# msg_lst_to = sv_to.get_data()
# print(sv_to.get_data())
# print(sv_from.get_data())

    



assert hasattr(Router, 'link') and hasattr(Router, 'unlink') and hasattr(Router, 'send_data'), "в классе Router присутсвутю не все методы, указанные в задании"
assert hasattr(Server, 'send_data') and hasattr(Server, 'get_data') and hasattr(Server, 'get_ip'), "в классе Server присутсвутю не все методы, указанные в задании"

router = Router()
sv_from = Server()
sv_from2 = Server()
router.link(sv_from)
router.link(sv_from2)
router.link(Server())
router.link(Server())
sv_to = Server()
router.link(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
sv_from2.send_data(Data("Hello", sv_to.get_ip()))
sv_to.send_data(Data("Hi", sv_from.get_ip()))
router.send_data()
msg_lst_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()

assert len(router.buffer) == 0, "после отправки сообщений буфер в роутере должен очищаться"
assert len(sv_from.buffer) == 0, "после получения сообщений буфер сервера должен очищаться"

assert len(msg_lst_to) == 2, "метод get_data вернул неверное число пакетов"

assert msg_lst_from[0].data == "Hi" and msg_lst_to[0].data == "Hello", "данные не прошли по сети, классы не функционируют должным образом"

assert hasattr(router, 'buffer') and hasattr(sv_to, 'buffer'), "в объектах классов Router и/или Server отсутствует локальный атрибут buffer"

router.unlink(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
router.send_data()
msg_lst_to = sv_to.get_data()
assert msg_lst_to == [], "метод get_data() вернул неверные данные, возможно, неправильно работает метод unlink()"



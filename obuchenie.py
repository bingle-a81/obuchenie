class AppVK :
    def __init__(self):
        self.name = "ВКонтакте"

class AppYouTube:
    def __init__(self,memory_max):
        self.name = "YouTube"
        self.memory_max=memory_max

class AppPhone:
    def __init__(self,**kwargs):
        self.name = "Phone"
        self.phone_list = kwargs


class SmartPhone:
    def __init__(self,model):
        self.model=model
        self.apps=[]


    def add_app(self,app):
        for x in self.apps:
            if x.name == app.name:
                return
        self.apps.append(app)

    def remove_app(self,app):
        self.apps.remove(app)

sm = SmartPhone("Honor 1.0")
sm.add_app(AppVK())
sm.add_app(AppVK())
sm.add_app(AppVK())  # второй раз добавляться не должно
sm.add_app(AppYouTube(2048))
for a in sm.apps:
    print(a.name)        



# TEST-TASK___________________________________
try:
    smart = SmartPhone("Honor 1.0")
except:
    print("шибка при создании объекта класса SmartPhone")

try:
    app_vk = AppVK()
except:
    print("шибка при создании объекта класса AppVK")

try:
    app_you_tube = AppYouTube(2048)
except:
    print("шибка при создании объекта класса AppYouTube")

try:
    app_phone = AppPhone({"Балакирев": 1234567890, "Сергей": 98450647365, "Работа": 112})
except:
    print("шибка при создании объекта класса AppPhone")

assert hasattr(smart, "model") and hasattr(smart, "apps") and hasattr(smart, "add_app") and \
       hasattr(smart, "remove_app"), "не все атрибуты и методы есть в объекте класса SmartPhone"

assert hasattr(app_vk, "name"), "не все атрибуты и методы есть в объекте класса AppVK"

assert hasattr(app_you_tube, "name") and hasattr(app_you_tube, "memory_max"), \
    "не все атрибуты и методы есть в объекте класса AppYouTube"

assert hasattr(app_phone, "name") and hasattr(app_phone, "phone_list"), \
    "не все атрибуты и методы есть в объекте класса AppYouTube"

assert type(app_phone.phone_list) is dict, "тип phone_list некорректный"

assert type(smart.model) is str, "название должно быть строкой"
assert type(smart.apps) is list, "apps должен быть списком"

smart.add_app(app_vk)
assert smart.apps[0] == app_vk, "некоректно сработал метод add_app"

smart.remove_app(app_vk)
assert len(smart.apps) == 0, "некоректно сработал метод remove_app"

# При добавлении нового приложения проверять, что оно отсутствует в списке apps (отсутствует объект соответствующего класса).
smart.add_app(app_vk)
smart.add_app(AppVK())

assert smart.apps.count(app_vk) == 1, \
    "метод add_app отработал с ошибкой в списке несколько объектов одного и того же класса"
print("Правильный ответ !!")
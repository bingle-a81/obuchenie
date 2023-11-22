# Может кому пригодиться))

'''Общая схема работы дескриптора для класса Point3D'''




class Point3D:
    class Integer:  # Дескриптор
        def __set_name__(self, owner, name):
            # Метод автоматически вызывается когда создается экземпляр класса
            # self - ссылка на экземпляр класса, owner - ссылка на класс Point3D'''
            self.name = '_' + name

        def __get__(self, instance, owner):
            # self - ссылка на экземпляр класса
            # instance - ссылка на экзампляр класса из которого был вызван
            # owner - ссылка на класс Point3D
            return instance.__dict__[self.name]

        def __set__(self, instance, value):
            # Срабатывает в момент присваивания из инициализатора
            # self - ссылка на экземпляр класса
            # instance - ссылка на экзампляр класса из которого был вызван
            # Value - значение которое будет присвоено
            print(f"__set__:{self.name} = {value}")
            instance.__dict__[self.name] = value

    x = Integer()
    y = Integer()
    z = Integer()

    def __init__(self, x, y, z):
        # В инициализаторе идет обращение к дескрипторам x, y, z
        self.x = x
        self.y = y
        self.z = z


pt = Point3D(1, 2, 3)


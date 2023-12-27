class Singleton:
    __instance = None
    __instance_base = None

    def __new__(cls, *args, **kwargs):
        if cls == Singleton:
            if cls.__instance_base is None:
                cls.__instance_base = super().__new__(cls)
            return cls.__instance_base
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance


class Game(Singleton):
    def __init__(self, name) -> None:
        if "name" not in self.__dict__:
            self.name = name


t = Singleton("m")
p1 = Game("first")
p2 = Game("second")
p3 = Game("3")
print(p1.name)
print(p2.name)
print(p3.name)

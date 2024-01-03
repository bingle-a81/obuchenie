# здесь объявляйте функцию-декоратор
def integer_params_decorated(func):
    def wrap(self, *args, **kwargs):
        for x in args:
            if type(x) != int:
                raise TypeError("аргументы должны быть целыми числами")
        d = kwargs.values()
        for x in d:
            if type(x) != int:
                raise TypeError("аргументы должны быть целыми числами")
        return func(self, *args, **kwargs)

    return wrap


def integer_params(cls):
    methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
    for k, v in methods.items():
        setattr(cls, k, integer_params_decorated(v))

    return cls


@integer_params
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __call__(self, func):
        self.router_cls.add_callback(self.path, func)

        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapper


@Callback("/about", Router)
def about():
    return "<h1>About</h1>"


route = Router.get("/about")
ret = route()
print(ret)
assert ret == "<h1>About</h1>", "декорированная функция вернула неверные данные"

route = Router.get("/")
assert route is None, "Класс Router, при вызове метода get, вернул неверные данные"
class VideoItem:
    def __init__(self, title, descr, path) -> None:
        self.title = title
        self.descr = descr
        self.path = path
        self.rating = VideoRating()


class VideoRating:
    def __init__(self, rating=0) -> None:
        self.rating = rating

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, val):
        if not (-1 < val < 6):
            raise ValueError("неверное присваиваемое значение")
        self.__rating = val


v = VideoItem(
    "Курс по Python ООП", "Подробный курс по Python ООР", "D:/videos/python_oop.mp4"
)
print(v.rating.rating)  # 0
v.rating.rating = 5
print(v.rating.rating)  # 5
title = v.title
descr = v.descr
v.rating.rating = 6  # ValueError

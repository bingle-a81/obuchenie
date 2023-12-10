class CentralBank:
    def __new__(cls) :
        return None
    
    rates={}

    @classmethod
    def register(cls, money):
        money.cb=cls


class MoneyR:
    def __init__(self,volume=0) -> None:
        self.cb=None
        if volume:
            self.volume=volume
        else:
            self.volume=0

    @property
    def cb(self):
        return self.__cb
    @cb.setter
    def cb(self, __value):
        self.__cb = __value

    @property
    def volume(self):
        return self.__volume
    @volume.setter
    def volume(self, __value):
        self.__volume = __value

    # def __eq__(self, other):
    #     if self.cb is None or other.cb is None:
    #         raise ValueError("Неизвестен курс валют.")
    #     if self.currency == "rub":
    #         v_1 = self.volume
    #         v_2 = other.volume * other.cb.rates["rub"]
    #         return abs(v_1 - v_2) < 0.1
    #     else:
    #         v_1 = self.volume * self.cb.rates["rub"]
    #         v_2 = other.volume * other.cb.rates["rub"]
    #         return abs(v_1 - v_2) < 0.1

    def __str__(self) -> str:
        return f'{self.volume*self.cb.rates["rub"]}'


CentralBank.rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

r = MoneyR(100)

CentralBank.register(r)
print(r)

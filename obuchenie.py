from functools import total_ordering

class CentralBank:
    def __new__(cls) :
        return None
    
    rates={}

    @classmethod
    def register(cls, money):
        money.cb=cls


@total_ordering
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

    def __eq__(self, __value) -> bool:
        if self.cb is None or __value.cb is None:
            raise ValueError("Неизвестен курс валют.")
        other=__value.volume
        if not isinstance(__value,MoneyR):
            other*=__value.cb.rates["rub"]
        return abs(self.volume-other)<0.1
    
    def __gt__(self, __value) -> bool:
        if self.cb is None or __value.cb is None:
            raise ValueError("Неизвестен курс валют.")
        other=__value.volume
        if not isinstance(__value,MoneyR):
            other*=__value.cb.rates["rub"]
        return self.volume>other

    def __str__(self) -> str:
        if self.cb is None :
            raise ValueError("Неизвестен курс валют.")       
        return f'{self.volume}'  
    
@total_ordering
class MoneyD:
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

    def __eq__(self, __value) -> bool:
        if self.cb is None or __value.cb is None:
            raise ValueError("Неизвестен курс валют.")        
        vol=self.volume*self.cb.rates["rub"]
        other=__value.volume
        if not isinstance(__value,MoneyR):
            other*=__value.cb.rates["rub"]
        return abs(vol-other)<0.1
    
    def __gt__(self, __value) -> bool:
        if self.cb is None or __value.cb is None:
            raise ValueError("Неизвестен курс валют.")
        vol=self.volume*self.cb.rates["rub"]
        other=__value.volume
        if not isinstance(__value,MoneyR):
            other*=__value.cb.rates["rub"]
        return vol>other

    def __str__(self) -> str:
        if self.cb is None :
            raise ValueError("Неизвестен курс валют.")       
        return f'{self.volume*self.cb.rates["rub"]}'   

@total_ordering
class MoneyE:
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

    def __eq__(self, __value) -> bool:
        if self.cb is None or __value.cb is None:
            raise ValueError("Неизвестен курс валют.")        
        vol=self.volume*self.cb.rates["rub"]
        other=__value.volume
        if not isinstance(__value,MoneyR):
            other*=__value.cb.rates["rub"]
        return abs(vol-other)<0.1
    
    def __gt__(self, __value) -> bool:
        if self.cb is None or __value.cb is None:
            raise ValueError("Неизвестен курс валют.")
        vol=self.volume*self.cb.rates["rub"]
        other=__value.volume
        if not isinstance(__value,MoneyR):
            other*=__value.cb.rates["rub"]
        return vol>other

    def __str__(self) -> str:
        if self.cb is None :
            raise ValueError("Неизвестен курс валют.")       
        return f'{self.volume*self.cb.rates["rub"]}'   
    
CentralBank.rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

CentralBank.rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

r = MoneyR(45000)
d = MoneyD(500)

CentralBank.register(r)
CentralBank.register(d)

if r > d:
    print("неплохо")
else:
    print("нужно поднажать")

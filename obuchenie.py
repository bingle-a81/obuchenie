from abc import ABC, abstractmethod


class Model:
    @abstractmethod
    def get_pk(self):
        pass

    def get_info(self):
        return "Базовый класс Model"


class ModelForm(Model):
    _id = 0

    def __init__(self, login, password) -> None:
        __class__._id += 1
        self._id = __class__._id
        self.login = login
        self.password = password

    def get_pk(self):
        return self._id


form = ModelForm("Логин", "Пароль")
form = ModelForm("Логин", "Пароль")
form = ModelForm("Логин", "Пароль")
print(form.get_pk())

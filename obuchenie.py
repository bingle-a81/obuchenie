from string import ascii_letters,digits
import random

CHARS=ascii_letters+ascii_letters.upper()+digits+'_.'

class EmailValidator():
    def __new__(cls,*args,**kwargs) :
        return None
        
    @classmethod
    def get_random_email(cls):
        return ''.join(CHARS[random.randint(0,len(CHARS)-1)] for x in range(random.randint(1,100)))+'@gmail.com'

    @classmethod
    def check_email(cls, email):
        if not EmailValidator.__is_email_str(email):
            return False
        a=email.split('@')
        b=a[1].split('.')
        c='..' in a[0]
        if all([len(a)==2,1<len(a[0])<101,1<len(a[1])<51,len(b)==2,not c]):
            return True
        return False
        

    @staticmethod
    def __is_email_str(email):
        return True if type(email)==str else False

assert EmailValidator.check_email("sc_lib@list.ru") == True and EmailValidator.check_email("sc_lib@list_ru") == False and EmailValidator.check_email("sc@lib@list_ru") == False and EmailValidator.check_email("sc.lib@list_ru") == False and EmailValidator.check_email("sclib@list.ru") == True and EmailValidator.check_email("sc.lib@listru") == False and EmailValidator.check_email("sc..lib@list.ru") == False, "метод check_email отработал некорректно"

m = EmailValidator.get_random_email()
assert EmailValidator.check_email(m) == True, "метод check_email забраковал сгенерированный email методом get_random_email"

assert EmailValidator() is None, "при создании объекта класса EmailValidator возвратилось значение отличное от None"

assert EmailValidator._EmailValidator__is_email_str('abc'), "метод __is_email_str() вернул False для строки"
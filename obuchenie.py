from string import ascii_lowercase, digits

CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
CHARS_CORRECT = CHARS + CHARS.upper() + digits

class TextInput:
    
    def __init__(self,name,size=10,):
        self.name = name
        self.size = size
        if not (self.check_name(self.name) and 3<self.size<50):
            raise ValueError("некорректное поле name")

    def get_html(self):
        return f"<p class='login'>{self.name}: <input type='text' size={self.size} />"
    
    @classmethod
    def check_name(cls, name):
        if not all(x for x in name if x in CHARS_CORRECT):
            return

    

class PasswordInput:

    def __init__(self,name,size=10,):
        self.name = name
        self.size = size

    def get_html(self):
        return f"<p class='password'>{self.name}: <input type='text' size={self.size} />"

# здесь объявляйте классы TextInput и PasswordInput


class FormLogin:
    def __init__(self, lgn, psw):
        self.login = lgn
        self.password = psw

    def render_template(self):
        return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])


# эти строчки не менять
login = FormLogin(TextInput("Логин"), PasswordInput("Пароль"))
html = login.render_template()
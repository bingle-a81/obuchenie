
class InputValues:
    def __init__(self, render):     # render - ссылка на функцию или объект для преобразования
        self.render=render

    def __call__(self, func):     # func - ссылка на декорируемую функцию
        def wrapper(*args, **kwargs):
            return list(map(self.render,func().split()))
        return wrapper
    

class RenderDigit:
    def __call__(self, x) :
            try:
                a=int(x)
                return a
            except:
                return None
            
@InputValues(RenderDigit())
def input_dg():
    return input()

res = input_dg()
print(res)
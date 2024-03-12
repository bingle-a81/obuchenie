<<<<<<< HEAD
class PrinterError(Exception):
    """Класс общих ошибок принтера"""
=======
import re
>>>>>>> 16373c4 (4)

pat=r'(?P<protocol>http[s]?)+\:\/\/(?P<domen>[a-z.]*?)\/[a-z\d\_\-\/]*(?P<param>\?[^# ]*)?(?P<yakor>#[a-z]*)?'
p1=r'(.{2})(.{4})'

<<<<<<< HEAD
class PrinterConnectionError(PrinterError):
    """Ошибка соединения с принтером"""
=======
st='''В этом https://stepik.org/lesson/704265/step/2?unit=704697#test '''
res=re.findall(p1,st)
>>>>>>> 16373c4 (4)

print(res)

<<<<<<< HEAD
class PrinterPageError(PrinterError):
    """Ошибка отсутствия бумаги в принтере"""


try:
    raise PrinterConnectionError("соединение с принтером отсутствует")
except (PrinterConnectionError, PrinterPageError) as e:
    print(e)
except PrinterError as e:
    print(e)
=======
# for x in res:
#     print(f'Полная ссылка: {x[1]}')
    # print(f'Протокол: {x["protocol"]} | Домен: {x["domen"]} | Параметры: {x["param"]} | Якорь: {x["yakor"]}')
    # print('')
>>>>>>> 16373c4 (4)

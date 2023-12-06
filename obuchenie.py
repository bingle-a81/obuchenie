from functools import total_ordering

stich = ["Я к вам пишу – чего же боле?",
        "Что я могу еще сказать?",
        "Теперь, я знаю, в вашей воле",
        "Меня презреньем наказать.",
        "Но вы, к моей несчастной доле",
        "Хоть каплю жалости храня,",
        "Вы не оставите меня."]

@total_ordering
class StringText :
    def __init__(self,lst_words:list) -> None:
        self.lst_words=lst_words

    def __eq__(self, __value) -> bool:
        return len(self.lst_words)==len(__value.lst_words)
    
    def __gt__(self, __value) -> bool:
        return len(self.lst_words)>len(__value.lst_words)
    
    def __str__(self) -> str:
        return ' '.join(x for x in self.lst_words)

lst_text=[StringText(list(filter(lambda y:y.strip('–?!,.;', (x.split() for x in stich))) ))]
print(lst_text)
lst_text_sorted=sorted(lst_text,reverse=True)
lst_text_sorted=[str(x) for x in lst_text_sorted]
print(lst_text_sorted)

assert all([[True if i in _ else False for i in "–?!,.;"] for _ in stich]), \
    "в stich есть знаки которые нужно удалить - (–?!,.;)"
assert len(lst_text) == 7 and all(
    True if isinstance(_, StringText) else False for _ in lst_text), "ошибка в lst_text"

assert lst_text_sorted == ['Я к вам пишу чего же боле',
                           'Теперь я знаю в вашей воле',
                           'Но вы к моей несчастной доле',
                           'Что я могу еще сказать',
                           'Хоть каплю жалости храня',
                           'Вы не оставите меня',
                           'Меня презреньем наказать'], "неверно отсортирован список lst_text_sorted"

assert lst_text[0] > lst_text[4] and lst_text[4] > lst_text[1], "метод > работает неверно"
assert lst_text[1] < lst_text[4], "метод < работает неверно"

assert lst_text[2] >= lst_text[4], "метод >= работает неверно"
assert lst_text[2] <= lst_text[4], "метод >= работает неверно"

print("Правильный ответ.")
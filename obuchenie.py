import re
import pyperclip


def replace_sign(letter, text):
    pat = letter + r"([\d\-\.]+)"
    return re.sub(pat, lambda x: letter + str(float(x[1]) * (-1)), text)


def halve_value_letter(letter, text) -> str:
    pat = letter + r"([\d\-\.]+)"
    return re.sub(pat, lambda x: letter + str(float(x[1]) / 2), text)


def replace_letters(what_change, change_for, text) -> str:
    return re.sub(what_change, change_for, text)


def cross_substitution(ferst_change, second_change, text) -> str:
    a = replace_letters(ferst_change, "@@", text)
    a = replace_letters(second_change, ferst_change, a)
    a = replace_letters("@@", second_change, a)
    return a


s: str = pyperclip.paste()
res = ""
for i in s.splitlines():
    a: str = replace_letters("CM", "Y", i)
    a = cross_substitution("G3", "G2", a)
    a = replace_sign("Y", a)
    a = halve_value_letter("X", a)
    res += a + "\n"

print(res)
pyperclip.copy(res)

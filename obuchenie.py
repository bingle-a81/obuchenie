from string import digits


def func(f: str):
    try:
        res = int(f)
    except:
        try:
            res = float(f)
        except:
            res = str(f)
    return res


lst_in = "8 11 abcd -7.5 2.0 -5".split()
print(list(map(lambda x: func(x), lst_in)))

print("1" in digits)

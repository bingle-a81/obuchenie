from string import digits


def func(f: str):
    for i in list(f):
        if i not in ("-" + digits):
            return False
    return True


lst_in = "8 11 abcd -7.5 2.0 -5".split()
print(sum(list(map(int, list(filter(lambda x: func(x), lst_in))))))

print("1" in digits)

from itertools import count


s = "a b c a a d c".split()
# print(s)


def outer():
    c = 0
    def inner():
        nonlocal c
        c = c + 1
        return c

    return inner


ls = []
co=outer()

for x in s:
    if x in ls:
        a =co()
        print(f'{x} {a}')
    ls.append(x)
print(ls)

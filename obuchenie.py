

def input_int_numbers():
    try:
        return tuple(map(int, input().split()))
    except:
        raise TypeError("все числа должны быть целыми")


while True:
    try:
        print(*input_int_numbers())
        break
    except:
        continue


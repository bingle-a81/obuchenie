dig = {
    "CS101": {"audience_number": "3004", "teacher": "Хайнс", "time": "8:00"},
    "CS102": {"audience_number": "4501", "teacher": "Альварадо", "time": "9:00"},
    "CS103": {"audience_number": "6755", "teacher": "Рич", "time": "10:00"},
    "NT110": {"audience_number": "1244", "teacher": "Берк", "time": "11:00"},
    "CM241": {"audience_number": "1411", "teacher": "Ли", "time": "13:00"},
}
n = input()

ls = list(dig.get(n).values())
print(f'{n}: ',end='')
print(*ls,sep=', ')

import re

s = """G0 X-0.200 Z10.000"""
# G1 Z0.000
# G1 X9.800
# G2 X10.000 Z0.200 R0.200
# G1 Z10.117
# G1 X17.012 Z17.130
# G2 X17.071 Z17.271 R0.200
# G1 Z27.188
# G1 X24.084 Z34.201
# G2 X24.142 Z34.342 R0.200
# G1 Z44.342
# G0 X34.142
# '''

p = r"(\w)([\d\-\.]+)"

ls = []
d = dict()

a = re.findall(p, s)
d = {x[0]: x[1] for x in a}



print(d.get('X'))
x11 = 0
y11 = 20
x12 = 5
y12 = 20

x21 = 20
y21 = 20
x22 = 28
y22 = 21

xx1 = x11 - x12
yy1 = y11 - y12

xx2 = x21 - x22
yy2 = y21 - y22


if xx1 == 0:
    a1 = 1
    b1 = 0
    c1 = x11
elif yy1 == 0:
    a1 = 0
    b1 = 1
    c1 = y11
else:
    a1 = 1 / (xx1)
    b1 = (-1) / (yy1)
    c1 = (x11 / (xx1)) - (y11 / (yy1))


a2 = 1 / (xx2)
b2 = (-1) / (yy2)
c2 = (x21 / (xx2)) - (y21 / (yy2))


x = (c1 * b2 - c2 * b1) / (a1 * b2 - a2 * b1)
y = (c2 * a1 - c1 * a2) / (a1 * b2 - a2 * b1)

print(x, y)

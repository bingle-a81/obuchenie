import re

s = """G0 X-0.400 Z-10.000
G1 Z-0.000
G1 X1.470
G2 X1.811 Z0.096 R0.200
G1 X4.621 Z2.388
G2 X4.680 Z2.493 R0.200
G1 Z4.888
G0 X24.680
"""
p = r"(\w)([\d\-\.]+)"
ls: list[dict[str, float]] = [
    {x[0]: float(x[1]) for x in re.findall(p, x)} for x in s.splitlines()
]


ls_lines_points = []
for i in range(1, len(ls)):

    p1 = ls[i - 1]
    p2 = ls[i]
    if p2.get("G") != 1:
        continue
    px1 = p1.get("X")
    if px1 is None:
        px1 = ls_lines_points[-1][0]
    pz1 = p1.get("Z")
    if pz1 is None:
        pz1 = ls_lines_points[-1][1]
    px2 = p2.get("X")
    if px2 is None:
        px2 = px1
    pz2 = p2.get("Z")
    if pz2 is None:
        pz2 = pz1
    line = (px1, pz1, px2, pz2)

    ls_lines_points.append(line)


# print(ls_lines_points)



def new_func(line1: tuple, line2: tuple) -> tuple[float, float]:

    x11, y11, x12, y12 = line1
    x21, y21, x22, y22 = line2

    xx1: float = x11 - x12
    yy1: float = y11 - y12

    xx2: float = x21 - x22
    yy2: float = y21 - y22

    if xx1 == 0:
        a1 = 1
        b1 = 0
        c1: float = x11
    elif yy1 == 0:
        a1 = 0
        b1 = 1
        c1 = y11
    else:
        a1: float = 1 / (xx1)
        b1: float = (-1) / (yy1)
        c1 = (x11 / (xx1)) - (y11 / (yy1))

    if xx2 == 0:
        a2 = 1
        b2 = 0
        c2: float = x21
    elif yy2 == 0:
        a2 = 0
        b2 = 1
        c2 = y21
    else:
        a2: float = 1 / (xx2)
        b2: float = (-1) / (yy2)
        c2: float = (x21 / (xx2)) - (y21 / (yy2))

    res_x: float = (c1 * b2 - c2 * b1) / (a1 * b2 - a2 * b1)
    res_y: float = (c2 * a1 - c1 * a2) / (a1 * b2 - a2 * b1)
    return res_x, res_y


for i in range(1, len(ls_lines_points)):
    print(new_func(ls_lines_points[i - 1], ls_lines_points[i]))



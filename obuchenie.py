st = "g i v e t h h i i s m a a a n a g u u n"
ls = st.split()
a = []
i1 = ls[0]
a1 = 0
for i in ls:
    if i == i1:
        a1 += 1
    else:
        a.append([i1] * a1)
        a1 = 1
    i1 = i
else:
    a.append([i] * a1)

print(a)

import re

# st='''G0 X-0.200 Z10.000
# G1 Z0.000
# G1 X9.800
# G2 X9.948 Z0.066 R0.200
# G1 X23.370 Z14.851
# G1 X40.664 Z24.835
# G2 X40.764 Z25.008 R0.200
# G1 Z45.008
# G0 X50.764'''

# pat=r'\w[\d\.-]+'

# d=[]
# for x in st.splitlines():
#     d.append(x)
# # print(d)


# res=re.findall(pat,st)
# print(res)


st='Уфо по Воронежской области МО РФ  отделение 1 (короткое название, л/с 4578А521453 )'

# pat=r'л[\.]?с[\s]?([\d]+)'
pat=r'л[^\w]?с\s?([\d\w]+)'

res=re.findall(pat,st)
print(res)
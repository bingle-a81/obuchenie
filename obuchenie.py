class Morph:
    def __init__(self,*args) -> None:
        if args is not None:
            self._lst=set(args)
        
    def add_word(self, word):
        if word.lower() not in self._lst:
            self._lst.append(word.lower())

    def get_words(self):
        return tuple(self._lst)

    def __eq__(self, __o:str) -> bool:
        return __o.lower() in self._lst

    def __ne__(self, __o: object) -> bool:
        return __o.lower() not in self._lst


st='''- связь, связи, связью, связей, связям, связями, связях
- формула, формулы, формуле, формулу, формулой, формул, формулам, формулами, формулах
- вектор, вектора, вектору, вектором, векторе, векторы, векторов, векторам, векторами, векторах
- эффект, эффекта, эффекту, эффектом, эффекте, эффекты, эффектов, эффектам, эффектами, эффектах
- день, дня, дню, днем, дне, дни, дням, днями, днях'''

dict_words =[Morph(*[x.strip('-] ') for x in line.split(',')]) for line in st.splitlines()]

a=Morph('связи')
print(a=='СВЯЗИ')
quit(-1)
text = 'СВЯЗИ'   # эту строчку не менять
text=text.lower().strip('.')
ls=[]
for x in set(text.split()):
    for y in dict_words:
        if x == y:
            ls.append(x)

print(len(ls))

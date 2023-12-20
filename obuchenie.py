class Person:
    i=0

    def __init__(self,fio, job, old, salary, year_job):
        self.fio,self.job,self.old,self.salary,self.year_job=fio, job, old, salary, year_job
        self.lst=[self.fio,self.job,self.old,self.salary,self.year_job]

    def __iter__(self):
        return self        
    
    def __next__(self):        
        if self.i<len(self.lst):
            res=self.lst[self.i]
            self.i+=1
            return res
        else:
            raise StopIteration
    


pers = Person('Гейтс Б.', 'бизнесмен', 61, 1000000, 46)
# pers[0] = 'Балакирев С.М.'
# print(pers[1])
for v in pers:
    print(v)
# pers[5] = 123 # IndexError
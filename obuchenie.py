from functools import reduce
import re

pat=r'\b\w+?\b'
uo='Milk is white and so is glue, Ghosts are white and they say BOO!'
b=set(re.findall(pat,uo))
print(len(b))

# c=reduce(lambda a,b: set(a)|set(b),uo)
# print(c)
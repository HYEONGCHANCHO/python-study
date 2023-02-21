#reduce()
from functools import reduce
n=[4,3,2,1,5]
print(reduce(lambda x,y :x+y,n))
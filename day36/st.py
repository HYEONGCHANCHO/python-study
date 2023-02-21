print('Hello'.rjust(10))
print('Hello'.ljust(10,'-'))
print('Hello'.center(10,'-'))

fruits={'apple':5,'banana':10,'orange':5}

for i,j in fruits.items():
    print(i.ljust(15,"-")+str(j).rjust(3))
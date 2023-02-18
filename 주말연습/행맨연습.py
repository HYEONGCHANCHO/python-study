aa=['abcdef','dadad']
a=aa[0]
print(a)
wword=''
cword=''
b='k'
c='l'
d='b'

if b in a :
    cword+=b
else:
    wword+=b 

if c in a :
    cword+=c
else:
    wword+=c

if d in a :
    cword+=d
else:
    wword+=d

print(cword)  
print(wword)  
secretword='panda'
cword=''
guess=input('입력')

for i in range(5):
    if guess == secretword[i]:
        cword=cword+guess
print(cword)
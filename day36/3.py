#string
a='아이언맨은'
b="Ironman"
print(a,b)
c="그는 대기업 사장'samsung' 이다"
d='''스파이더맨은 지금 학생이다'''
print(c)
print(d)

print(type(a))
print(len(b))
print(b.split())
print(len(b.split()))

u='Her book is called "The Magician'
print(u.split('a')) #a 글자 기준으로 문자열이 분리
print('you,are,so,pretty'.split(",")) #,를 기준으로 분리, 결과는 리스트형
print(' '.join(['just','do','it'])) #각 단어를 공백을 넣고 합침
print('-'.join(['just','do','it'])) #각 단어를 공백없이 '-'를 넣고 합침

s="Spider man"
print('dog' in s)
print('p' in s)
print('p' not in s)
print(s.startswith('Spider'))
print(s.endswith('man'))

t='''Captain Rogers'''
t=t.replace('Rogers','America')
print(t)

z='Anton has three cars. Javier has four'
numbers={'one':'1','two':'2','three':'3','four':'4','five':'5'}
for i,j in numbers.items():
    z=z.replace(i,j)

print(z)

tt="Captain roGers"
print(tt.lower())
print(tt.upper())
print(tt.capitalize())

#isupper,islower,istitle,isalnum 
print('hulk'.isupper()) #False 대문자인가?
print('Hulk'.islower()) #False 소문자인가?
print('Hulk'.istitle()) #True 첫글자가 대문자인가
print('covid19'.isalnum()) #True 알파벳 또는 숫자로 구성되어 있는가?

#isalpha, isnumberic,isdigit,isdeciman
print('Thor'.isalpha())
print('3.14'.isnumeric())
print('314'.isdigit())
print('3.14'.isdecimal())

import string
#digits은 숫자를 말함,여기서 string은 변수가 아니고 라이브러리
print(string.digits)
print(string.punctuation)
print(string.ascii_lowercase)
print(string.ascii_uppercase)

#공백제거
w='\n Natasha is a spy \n'
x='\nShe has red hair \n'
print(w.strip()+'.')
print(w.lstrip())
print(w.rstrip())
print(w.strip()+'.'+ x.strip()+'.')

import string
y='What do you wnat?!!&?'
print(y.rstrip(string.punctuation))

ww='Natasha is a spy'
print(ww.count('a'))
z='0123456789'
print(z[1])
print(z[5:8])
print(z[:3])
print(z[7:])
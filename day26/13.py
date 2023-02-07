print('섭씨(C)/화씨(F) 온도 변환 프로그램입니다.')
print('온도가 섭씨이면 C 또는 c, 화씨이면 F 또는 f를 입력하세요.')

cel_fah = input('\n섭씨(C) or 화씨(F) ==> ')
degree =int(input('온도를 입력하세요 ==> '))

if(cel_fah == 'C' or 'c'):
    Fah_temp = (9/5*degree) +32
    print('섭씨 %dº를 화씨로 변환하면 %.1fº 입니다.'%(degree,Fah_temp))
else:
    cel_fah=(degree-32) *5/9
    print('화씨 %dº를 섭씨로 변환하면 %.1fº입니다.' %(degree,cel_fah))
# if(cel_fah == 'C'):
#     Fah_temp = (9/5*degree) +32
#     print('섭씨 %dº를 화씨로 변환하면 %.1fº 입니다.'%(degree,Fah_temp))
# elif(cel_fah == 'c'):
#     Fah_temp = (9/5*degree) +32
#     print('섭씨 %dº를 화씨로 변환하면 %.1fº 입니다.'%(degree,Fah_temp))
# else:
#     cel_fah=(degree-32) *5/9
#     print('화씨 %dº를 섭씨로 변환하면 %.1fº입니다.' %(degree,cel_fah))
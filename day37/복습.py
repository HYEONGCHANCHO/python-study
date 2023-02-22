# #if not 변수
# name=' '
# if not name:
#     print("+")
# else:
#     print("-")

# #enumerate()

# for i,letter in enumerate(['a','b','c']):
#     print(i)
#     print(letter)

a=input("이름 입력")

if not a:
    print("입력값이 없습니다")
for i,j in enumerate(a):
    print("입력한 이름의 인덱스는{} 값은{}".format(i,j))






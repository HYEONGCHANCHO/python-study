'''
집합은 set 키워드를 사용하며 중괄호{} 사이에 정의된다.
집합의 각 요소는 고유하고 불변해야 하며 중복요소를 가지면 안된다
집합은 변경가능하므로 생성 후에 수정이 가능하다
set은 정렬되지 않는 항목 또는 데이터 유형의 모음으로 저장된 요소의 순서가 고정되어 있지 않아서 인덱스를 이용한 접근이 불가능하다
int,float,tuple유형의 요소를 포함할 수 있지만 가변요소(리시트, 딕셔너리, 집합)은 집합의 요소가 될 수 없습니다.
교집합, 합집합, 차집합을 구하는데 용이하다

'''
days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}
print(type(days))
print('set의 요소를 출력')

for i in days:
    print(i)
day1=set(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
print(day1)
print(type(day1))
for i in day1:
    print(i)

set1={1,2,3,"python",20.5,14}
print('type(set1)',type(set1))
print(set1)

# set2={1,2,3,["python",4]}
# print('type(set2)',type(set2))

setA=set()
print(setA)
str='lets learn Python from here'
setA=set(str)
print(setA)

['lets','learn','python','from','hreo']
setb=set(['lets','learn','python','from','hreo']
)
print(setb)
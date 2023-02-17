#person 클래스 선언 , 속성 3가지 요소 ,변수 3개에 해당 클래스 할당, 값을 입력한 뒤에 각 요소 출력
class Person:
    def __init__ (self,age,height,hobby):
        self.age=age
        self.height=height
        self.hobby=hobby

mike=Person(20,170,'tennis')
smith=Person(23,180,'cooking')
john=Person(25,178,'coding')

print(mike.age)
print(mike.height)
print(mike.hobby)

print(smith.age)
print(smith.height)
print(smith.hobby)

print(john.age)
print(john.height)
print(john.hobby)
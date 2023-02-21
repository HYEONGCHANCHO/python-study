#overriding에 대해 
#상속을 받은 클래스가 부모가 가진 메서드를 재정의해서 사용할 때 발생

class Animal:
    def eat(self):
        print('This animal is eating')
    
class Rabbit(Animal):
    def eat(self):
        print('Rabbit is eating carrot')

rabbit=Rabbit()
rabbit.eat()

#만약에 재정의된 것과 

class A:
    def disp(self):
        print('This is parent method')

class B(A):
    def disp(self):
        super().disp()  
        print('This is child method')
obj=B()
obj.disp()  

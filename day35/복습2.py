class Calculator:
    def plus(self,x,y):
        return x+y
    def minus(self,x,y):
        return x-y
    def multiply(self,x,y):
        return x*y
    def divide(self,x,y):
        return x/y

calc=Calculator()
# print(calc.plus(1,2))
# print(calc.minus(1,2))
# print(calc.multiply(1,2))
# print(calc.divide(1,2))

#input 2개의 값을 입력받아서 사용자에게 어떤 연산을 할지 입력받아서 계산하도록

cal=(input("어떤 연산을 사용하겠습니까? +,-,*,/\n")).strip(" ")
x=int(input("숫자1 입력"))
y=int(input("숫자2 입력"))

if cal=='+':
    print(calc.plus(x,y))
elif cal=='-':
    print(calc.minus(x,y))
elif cal=='*':
    print(calc.multiply(x,y))
elif cal=='/':
    print(calc.divide(x,y))

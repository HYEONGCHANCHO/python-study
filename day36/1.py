#input문 2개의 값 입력받고 사칙연산
class Calculator:
    def __init__(self):
        self.x1=int(input("첫번째 값을 입력하세요"))
        self.x2=int(input("두번째 값을 입력하세요"))
    def calc(self):
        a=input("적용할 계산을 입력하세요 +,-,*,/").split(" ")
        # print(self.x1)
        # print(self.x2)
        # print(a)
        if a==['+']:
           print(f"{self.x1}+{self.x2}={self.x1+self.x2}")
        elif a==['-']:
           print(f"{self.x1}-{self.x2}={self.x1-self.x2}")
        elif a==['*']:
           print(f"{self.x1}*{self.x2}={self.x1*self.x2}")
        elif a==['/']:
           print(f"{self.x1}/{self.x2}={self.x1/self.x2}")

calc=Calculator()
calc.calc()


#속성을 나중에 지정
#붕어빵 재료를 제공해주는 업체
class Car:
    def drive(self):
        self.speed=60

myCar=Car()
myCar.model="e-class"
myCar.year=2017
myCar.color='blue'
# print(myCar.model)
# print(myCar.year)
# print(myCar.color)
print(myCar)
myCar.drive()
print(myCar.speed)

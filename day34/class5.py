# #렌트가 업체
# class Car:
#     def __init__(self):
#         self.license=0
#     def driving(self,driver):
#         print("이 차의 운전자는"+driver+"씨는 운전가능,",end="")
#         self.license +=1
#         print("라이센스가 {}사용되었습니다 ".format(self.license))

# kia =Car()
# hyundai=Car()
# kia.driving('kim')
# kia.driving('Hong')
# hyundai.driving('Hong')
# hyundai.driving('kim')


class Car:
    def __init__(self):
        self.license=0
    def usecar(self,name):
        self.license+=1
        print(f"운전자{name}가 운전하였습니다. license는 {self.license}입니다.")
kia=Car()
bmw=Car()
kia.usecar('kim')
kia.usecar('Hong')
bmw.usecar('a')
bmw.usecar('b')
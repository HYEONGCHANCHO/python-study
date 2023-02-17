class Person:
    def __init__(self,height,address,age):
        self.height=height
        self.address=address
        self.age=age

mike=Person(170,'Seoul',26)
smith=Person(182,'Suwon',31)
John=Person(160,'Seoul',23)

print('-'*30)
print("첫번째 등록한 사람의 이름은",mike.address)
print(smith.height,"입니다")
print(John.age)


# class Person:
#     def __init__(self,age,job,hobby):
#         self.age=age
#         self.job=job
#         self.hobby=hobby

# mike=Person(20,'student','cooking')
# print(mike.age)
# print("mike의 취미는",mike.hobby)

# smith=Person(26,'developer','coding')
# print(smith.job,"입니다")
# print("smith의 취미는",smith.hobby,"입니다")
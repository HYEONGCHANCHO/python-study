# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
class Person:
    def __init__(me,name,age):
        me.name=name
        me.age=age
    def __str__(self):
        return f"{self.name}({self.age})"

p1=Person('john',30)
print(p1)
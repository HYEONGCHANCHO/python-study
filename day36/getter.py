#속성 지정, 속성 가져오기
# class Employee:
#     name='David'
#     salary=55000
#     job='Developer'

# p1=Employee()
# print('David의 연봉은 ',getattr(p1,'salary'))
# print('David의 연봉은 ',p1.salary)
# setattr(p1,'age',33)
# print('David의 나이는', getattr(p1,'age'))

class Details:
    name='Sam'
    age=24

d=Details()
print(d.name,d.age)
d.name='Timmy'
d.age=27
print(d.name,d.age)

setattr(d,'name','Tim')
setattr(d,'age',1)

print(d.name,d.age)
number=3
day="three"
print("I ate %d apples. so I was sick for %s days" %(number,day))


print("I ate {0} apples. so I was sick for {1} days" .format(number,day))
print("I ate {number} apples. so I was sick for {day} days" .format(number=10,day=3))
print("I ate {0} apples. so I was sick for {day} days" .format(10,day=3))

# print("{0:<10}".format("hi"))
# print("{0:>10}".format("hi"))
# print("{0:^10}".format("hi"))
# print("{0:=^10}".format("hi"))
# print("{0:!<10}".format("hi"))

# print("{:<10}".format("hi"))
# print("{:>10}".format("hi"))
# print("{:^10}".format("hi"))
# print("{:=^10}".format("hi"))
# print("{:!<10}".format("hi"))

name="hong"
age=30
house="Suwon"
print("나는 %s이고 나이는 %d 집은 %s 입니다" %(name,age,house))
print("나는 {0}이고 나이는 {1} 집은 {2} 입니다" .format(name,age,house))
print(f"나는 {name}이고 나이는 {age} 집은 {house} 입니다")


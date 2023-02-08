thatdict= dict(name="John",age=32,country="Norway")
print(thatdict)

# 딕셔너리에 접근 key로 접근
# get()함수 이용해서 접근

# x=thatdict.get("name")
# print(x)

# 기존의 값을 변경
thatdict["name"]="Smith"
print(thatdict)

# # 변경, key와 value값을 함꼐
thatdict.update({"country":"korea"})
print(thatdict)
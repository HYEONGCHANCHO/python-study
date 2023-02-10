# 공식 3.14*반지름 **2

# radius=float(input("반지름을 입력하세요 :"))

# def circle(radius):
#     print(f"원의 둘레는 : {3.14*radius**2}")    

# circle(radius)
# r=float(input("반지름을 입력하세요 :"))

# def circle(radius):
#     result = 3.14*radius**2
#     return result

# print(circle(r))

# global 변수로 만듦
def cal_area(radius):
    global area
    area= 3.14 * radius ** 2
    return

r = float(input("원의 반지름 입력 :"))
cal_area(r)
print(area)








































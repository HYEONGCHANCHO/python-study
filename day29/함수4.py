# 덧셈 함수
def add_num(*args):
    result = 0
    for i in args:
        result +=i
    return result
    
print(add_num(1,2,3))
print(add_num(1,2,3,4,5,6,7,8,9))
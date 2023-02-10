# 합계를 구하는 프로그램 예)1~10까지 합을 구해서 출력까지 함수로 정의

# def get_sum(x,y):
#     sum=0
#     for i in range(x,y+1):
#         sum+=i
#     return sum

# def get_sum(x,y):
#     sum=0
#     for a in range(x,y+1):
#         sum += a
#     return sum

# def get_sum(x,y):
#     sum=0
#     for _ in range(x,y+1):
#         sum+=_
#     return sum

# def get_sum(x,y):
#     sum=0
#     for b in range(x,y+1):
#         sum += b
#     return sum

# def get_sum(x,y) :
#     sum=0
#     for q in range(x,y+1):
#         sum +=q
#     return sum

# def get_sum(x,y):
#     sum=0
#     for w in range(x,y+1):
#         sum +=w
#     return sum

def get_sum(a,b):
    sum=0
    for x in range(a,b+1):
        sum+=x
    return sum



print(get_sum(1,10))
        
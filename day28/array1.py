# 배열의 초기화 하는 방법
# range()이용

# a=[0,0,0,0]

score=[0 for x in range(5)] 
print(score)

score=[[2 for _ in range(4)] for _ in range(5)    ]
print(score)

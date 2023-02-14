#행과 열을 계산
a=[[0,0,0,0],\
    [0,0,0,0]
]

for i in range(0,2):
    for j in range(0,4):
        a[i][j]=(i+1)+(j+1)
print(a)

sum=0
for i in range(0,2):
    for j in range(0,4):
        sum=sum+a[i][j]

print(sum)
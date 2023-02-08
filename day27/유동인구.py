total=[300,200,300,400,500]
male=[130,100,130,200,300]

people={
    '수요일':{f"전체 인구:{total[0]}",f"30대 남성:{male[0]}"},
    '목요일':{f"전체 인구:{total[1]}",f"30대 남성:{male[1]}"},
    '금요일':{f"전체 인구:{total[2]}",f"30대 남성:{male[2]}"},
    '토요일':{f"전체 인구:{total[3]}",f"30대 남성:{male[3]}"},
    '일요일':{f"전체 인구:{total[4]}",f"30대 남성:{male[4]}"},
}

totalpeople=sum(total)
totalave=float(totalpeople/len(total))

totalmale=sum(male)
totalmaleave=float(sum(male)/len(male))

print(f"수~일 전체 유동인구는{totalpeople}명이고 평균은{totalave}명 이다. 수~일 30대 남자 유동인구는{totalmale}명이고 평균은 {totalmaleave}이다\n")

# 그래프 추가

from matplotlib import pyplot as plt
ylabel=[100,200,300,400,500]
xlabel=['WED','THR','FRI','SAT','SUN']
plt.plot([300,200,300,400,500])
plt.plot([130,100,130,200,300])
plt.xlabel('day of the week')
plt.ylabel('dating population')
plt.title('Weekly Floating Population Data')
plt.legend(['total','male'])
plt.bar(xlabel,ylabel,width=0)
plt.show()

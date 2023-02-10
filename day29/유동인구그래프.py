import csv

a=[[],[],[],[],[]]
i=j=0
with open(r"C:\web\day29\people.csv",'r',encoding='utf-8') as f:
    reader=csv.DictReader(f)
    for row in reader:
        a[i].append(row)
        j=j+1
        if j%15==0:
            i=i+1

avgp,avgm=[],[]
sump=summ=0

for j in range(15):
    for i in range(5):
        sump+=int(a[i][j]['num'])
        summ+=int(a[i][j]['nummale'])
    avgp.append(sump/5)                       #이부분을 계속 헷갈렸음
    avgm.append(summ/5)


time_table=['08','09','10','11','12','13','14','15','16','17','18','19','20','21','22']

import matplotlib.pyplot as plt

plt.title("time,people")
plt.xlabel("time")
plt.ylabel("people")

plt.plot(time_table,avgp)
# plt.plot(time_table,avgm)
# plt.legend()
plt.show()



import csv
a=[[],[],[],[],[]] 

with open(r'C:\web\day29\people.csv','r',encoding='utf-8') as f:
    reader=csv.DictReader(f)
    i=j=0
    for row in reader:
        a[i].append(row)
        j=j+1
        if(j%15==0):
            i=i+1

#시간대별 주간 평균값 구하기
avgh,avghm=[],[]

for j in range(0,15):
    day_sum=0
    day_msum=0
    for i in range(0,5):
        day_sum = day_sum +int(a[i][j]['num'])
        day_msum = day_msum +int(a[i][j]['nummale'])

    avgh.append(day_sum/5)
    avghm.append(day_msum/5)

day_title=['WED','THR',"FRI",'SAT','SUN']
hour_title=['08','09','10','11','12','13','14','15','16','17','18','19','20','21','22']

import matplotlib.pyplot as plt

plt.title("Hourly passerby data")
plt.xlabel("Hour")
plt.ylabel("Number of passerby")

plt.plot(hour_title,avgh,c="green",label="whole pople")
plt.plot(hour_title,avghm,c="red",label="30male")

plt.scatter(hour_title,avgh)
plt.scatter(hour_title,avghm)
plt.legend()
# plt.bar(hour_title,day_title,width=0)
plt.show()
import csv
a=[[],[],[],[],[],[],[]]
i=0
j=0
with open(r"C:\web\day28\passby_data.CSV",'r') as f:
    reader=csv.DictReader(f)
    for row in reader:
        a[i].append(row)
        j=j+1
        if(j%24==0):
            i=i+1


day_title=['MON','TUE','WED','THR','FRI','SAT','SUN']
hour_title=['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24']
avgh=[]
# j번째 시간대의 주간 총합

for j in range(0,24):
    day_sum=0
    for i in range(0,7):
        day_sum=day_sum+int(a[i][j]['num'])
    
    avgh.append(day_sum/7)

# 시간대별 평균 유동인구 출력
for j in range(0,24):
    print("[~{0}:00]:{1:4}".format(hour_title[j],int(avgh[j])))

for j in range(0,24):
    print("[~{0}:00]시 평균 {1:>6}명".format(hour_title[j],int(avgh[j])))

import matplotlib.pyplot as plt

plt.title("hourly passerby data")
plt.xlabel("hour")
plt.ylabel("number of passerby")

plt.scatter(hour_title,avgh)
plt.plot(hour_title,avgh)
plt.show()
        
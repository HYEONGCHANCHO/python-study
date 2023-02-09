import csv
a=[[],[],[],[],[]]
i=0
j=0
with open(r"C:\web\day28\people.CSV",'r',encoding='utf-8') as f:
    reader=csv.DictReader(f)
    for row in reader:
        a[i].append(row)
        j=j+1
        if(j%15==0):
            i=i+1


day_title=['WED','THR','FRI','SAT','SUN']
hour_title=['08','09','10','11','12','13','14','15','16','17','18','19','20','21','22']
avgh=[]

for j in range(0,15):
    day_sum=0
    for i in range(0,5):
        day_sum=day_sum+int(a[i][j]['num'])
    
    avgh.append(day_sum/5)

# 시간별 인구 수 평균
for j in range(0,15):
    print("[~{0}:00]:{1:4}".format(hour_title[j],int(avgh[j])))

# 요일, 시간별 인구 수
for i in range(0,5):
    print(f"{day_title[i]}")
    for j in range(0,15):
        print("[~{0}:00]:{1:4}".format(hour_title[j],int(a[i][j]['num'])))

for j in range(0,15):
    print("[~{0}:00]시 평균 {1:>6}명".format(hour_title[j],int(avgh[j])))


import matplotlib.pyplot as plt

plt.title("hourly passerby data")
plt.xlabel("hour")
plt.ylabel("number of passerby")

plt.scatter(hour_title,avgh)
plt.plot(hour_title,avgh)
plt.show()
        


        

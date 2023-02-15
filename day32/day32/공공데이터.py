import csv
import matplotlib.pyplot as plt

f=open(r'C:\web\naver_datalab_shoppingInsight_category_월간_data_20230215154440.csv',encoding="utf-8")
data=csv.reader(f)
next(data)
mandata=[]
womandata=[]
date=[]
for row in data:
    if row[1] !="":
        mandata.append(float(row[1]))
    if row[2] !="":
        womandata.append(float(row[2]))
    if row[0] !="":
        date.append(row[0])

# print(type(mandata[0]))
# print(womandata)
# print(date)

# # plt.hist(weekNoteSearchdata,bins=12)
plt.xlabel("date")
plt.ylabel("Search")
plt.plot(date,mandata,label='mandata')
plt.plot(date,womandata,label='womandata')
plt.legend()
plt.show()
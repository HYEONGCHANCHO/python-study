import csv
import matplotlib.pyplot as plt

# #---------------------여성의 맥북케이스 검색량-------------------------------------------------
# f4=open(r'C:\web\mac.csv',encoding="utf-8")
# data4=csv.reader(f4)
# next(data4)
# macsearch=[]
# date4=[]
# for row in data4:
#     if row[1] !="":
#         macsearch.append(float(row[1]))
#     if row[0] !="":
#         date4.append(row[0])

# plt.subplot(221)
# plt.title("How many search 'Macbook case'")
# plt.xlabel("Date")
# plt.ylabel("How many Search")
# plt.plot(date4,macsearch,label="Woman, search 'Macbook case'")
# plt.legend()

# #---------------------여성의 삼성노트북케이스 검색량-------------------------------------------------
f5=open(r'C:\web\samsung.csv',encoding="utf-8")
data5=csv.reader(f5)
next(data5)
samsearch=[]
date5=[]
for row in data5:
    if row[1] !="":
        samsearch.append(float(row[1]))
    if row[0] !="":
        date5.append(row[0])

# plt.subplot(222)
plt.title("How many search 'Samsung notebook case'")
plt.xlabel("Date")
plt.ylabel("How many Search")
plt.plot(date5,samsearch,label="Woman, search 'Samsung notebook case'")
plt.legend()
plt.show()
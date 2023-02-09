# f1=open("score.txt",'w')
# print("국어 : 100",file=f1)
# print("수학 : 100",file=f1)
# f1.close

# f2=open("myscore.txt",'w')
# print("국어 : 80",file=f2)
# print("영어 : 20",file=f2)
# print("수학 : 80",file=f2)
# print("사회 : 40",file=f2)
# f2.close

# f1=open("demotxt1.txt",'w',encoding="utf-8")
# f1.write("korea : 100")
# f1.write("computer : 100")
# f1.write("english : 100")
# f1.close

# f2=open("demotxt1.txt",'a',encoding="utf-8")
# f2.write("\n science : 80")
# f2.write("\n math : 80")
# f2.close

# f1=open("score.txt",'r')
# print(f1.read())
# f1.close

# while f1.readline() !="EOF":
#     print(f1.readline(), end="")
# if f1.readline !="":
#     print(f1.readline(), end="")
# f1=open("demotxt1.txt",'r')
# while True:
#     line=f1.readline()
#     if not line:
#         break
#     print(line, end="")
# f1.close()
# import os
# os.remove('score.txt')

# f1=open("test.txt",'a')
# f1.write('\nfirst')
# print("second",file=f1)
# print("third",file=f1)
# print("forth",file=f1)
# f1.close()

# f2=open("test.txt",'r')
# print(f2.read())
# f2.close()
# print("--------------------")
# f2=open("test.txt",'r')
# print(f2.read(),end="")
# f2.close()
# print("--------------------")
# print(f2.readline())
# print(f2.readline())
# print("--------------------")
# 
f2=open("test.txt",'r')
while True:
    line=f2.readline()
    if not line:
        break
    print(line,end="")
f2.close()










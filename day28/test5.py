# with 문  사용하지 않았을 때
# f1=open("demotxt1.txt",'r','utf-8')
# text =f1.read()
# print(text)
# f1.close()

with open('demotxt1.txt','r') as f: 
    text=f.read()
    print(text)
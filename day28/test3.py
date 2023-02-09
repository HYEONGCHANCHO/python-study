f1=open("C:\\Users\\a11\\Desktop\\서문.txt",'r',encoding="utf-8")
EOF=''
line = f1.readline()

while line != EOF:
    print(line)
    line=f1.readline()

f1.close()
fname=input("[내용 확인하고 싶은 파일 이름을 입력하세요] > ")

# while fname:
#     myfile=open(fname,'r')
#     print(myfile.read())
#     fname=input('>\n[내용 확인하고 싶은 파일이름을 입력하세요]')

# while fname:
#     try:
#         myfile=open(fname,'r')
#         print(myfile.read())
#         fname = input('>\n[내용 확인하고 싶은 파일이름을 입력하세요]')
#     except FileNotFoundError:
#         print('원하시는 파일이 존재하지 않습니다')
#         fname=''

while fname:
    try:
        myfile=open('demo.txt','r')
    except FileNotFoundError:
        fname=input('[오류] 파일 이름을 다시 입력하세요: >')
    else:
        print(myfile.read())
        fname = input('>\n[내용 확인하고 싶은 파일이름을 입력하세요]')
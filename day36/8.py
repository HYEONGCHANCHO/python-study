'''
try ~ except( ~ else)문 형식
try: 프로그램에서 발생가능성이 있는 작업을 실행해 보는 부분
except : 예외가 발생했을 때 처리하는 코드

'''

date=True
while date: #date의 값이 null이 들어오면 false로 종료
    try:
        date=input('월,일을 입력하세요')
        mm,dd=date.split()
        mm,dd=int(mm),int(dd)
    except:
        print("잘못된 입력입니다")
    else:
        print('%d 월 %d 일'%(mm,dd))
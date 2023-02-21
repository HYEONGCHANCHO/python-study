#Dates, Time 사용하기
'''
파이썬에서 시간, 날짜 사용
Use datetime.date.today()
datetime.date class는 date(year,month,day) (integer 속성)
date.weekday()에서 월요일은 0이다
ISO 포맷은 yyyy-mm-dd형태이다.
'''
# from datetime import date
# todays_date=date.today()
# print(todays_date)
# print(todays_date.month,todays_date.day,todays_date.year)
# print(todays_date.weekday()) #월요일 0, 화요일 1 ... 출력
# from datetime import date
# todays_date=date.fromisoformat('2023-03-01')
# print(todays_date)
# print(str(todays_date)) #이것은 date.fromisoformat('2023-03-01')와 동일하다.
# print(todays_date.isoformat())

#날짜 비교가능, 이후날짜는 이전날짜보다 크다.
#날짜 덧셈 및 뺄셈은 datetime.timedalta 객체로 결과를 제공한다.
#날짜를 비교, 더하기/빼기 연산을 시간객체에 사용할 수 있다.

# from datetime import date
# todays_date=date.today()
# d1=date(2020,5,14)
# print(todays_date > d1)
# print(todays_date - d1)

#시간(시,분,초,microsecond,tzinfo)를 제공한다.
# from datetime import time
# t1=time(14,25,36,18625)
# print(t1)
# t2=time(2,19)
# print(t2)
# print(t1<t2)

#datetime.datetime 객체는 날짜와 시간을 datetime객체에 연결한다
#형식 datetime.datetime(년,월,일,시간,분,초,마이크로초,tzinfo)
#datetime.datetime 객체는 딕셔너리의 키로 사용할 수 있다
#date(), time() 함수 제공

# from datetime import datetime
# # datetime(년 , 월 , 일 , 시간 , 분 , 초 마이크로초, tzinfo)
# dt1 = datetime(1941, 12, 7, 7, 53)
# print(dt1)
# print(dt1.date())
# print(dt1.time())

# #datetime.datetime.now()는 현재의 날짜와 시간
from datetime import datetime
print(' datetime.now() ')
t3=datetime.now()
print(t3.time())
print(t3.date())
print(t3.hour,t3.minute)
print(str(t3.month)+"-"+str(t3.day)+"-"+str(t3.year))
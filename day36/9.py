days=(31,29,31,30,31,30,31,31,30,31,30,31)
date=True

while date:
    try:
        date=input("날짜 <월 일>을 입력하세요: > ")
        mm,dd=date.split()
        mm,dd=int(mm),int(dd)
        while mm<1 or mm>12 or dd<1 or dd>days[mm-1]: #mm달수이니 1~12월 사이, dd는 월따라 마지막 날수가 바뀌니 days에서 해당 인덱스가 해당 월수로 간주되어 마지막 날수를 체크 days[1]은 2월의 날수 29일이 마지막, 인덱스는 0부터 시작하니 2번째 요소는 days[1]로 하기 위해서 -1한다.
            date=input('[월/일-오류] 다시 입력하세요: > ')
            mm,dd=date.split()
            mm,dd=int(mm),int(dd)
    
    except:
        print('입력오류입니다')
    else:
        print('%d월 %d일'%(mm,dd))

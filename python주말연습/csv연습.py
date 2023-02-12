with open('parking.csv','w') as f:
    num,usetime=0,0
    print(f'carnum : {num} time : {usetime}',file=f)

    while(1):
        intro=int(input("번호를 입력하세요. 1. 주차 번호 등록 2. 할인 옵션 선택 3. 주차 요금 확인"))
        if intro==1:
            num=int(input("차 번호를 입력하세요"))
            usetime=int(input("사용 시간을 입력하세요"))
        elif intro==2:
            discount=int(input("1.저탄소 차량 2.장애인 차량 3.수원시민 차량 4. 해당 없음"))
            print("할인이 입력되었습니다.")
        elif intro==3:
            price=usetime*3000
            lowPrice=int(price/30)
            disablePrice=int(price/80)
            SuwonPrice=int(price/50)
            if discount==4:
                print(f"주차 요금은 {price}입니다.")
            elif discount==1:
                print(f"주차 요금은 {lowPrice}입니다.")
            elif discount==2:
                print(f"주차 요금은 {disablePrice}입니다.")
            elif discount==3:
                print(f"주차 요금은 {SuwonPrice}입니다.")
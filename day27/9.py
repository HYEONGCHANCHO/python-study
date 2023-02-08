myMenu ={
    '김치찌개':6000,
    '된장찌개':6000,
    '제육볶음':8000
}


while(1):
    print("(1)전체 메뉴 보기, (2) 메뉴 가격 보기, (3)메뉴 추가/수정, (4)메뉴 삭제, (9)종료 \n")
    num=int(input(" 번호를 선택하세요 :"))

    if (num==1):
        print(myMenu)   
    elif (num==2):
        menu=str(input(" 가격을 확인하고 싶은 메뉴를 입력하세요 : "))
        menuprice=myMenu[f"{menu}"]
        print(f"*{menu}의 가격은 {menuprice}원 입니다.")
    elif (num==3):
        addMenu=str(input(" 추가할 식사 메뉴를 입력하세요 : "))
        addMenupri=int(input(" 새로운 식사 메뉴의 가격을 입력하세요 : "))
        myMenu[f"{addMenu}"]=addMenupri
        print("메뉴 수정 완료")
    elif (num==4):
        delmenu=str(input(" 삭제할 식사 메뉴를 입력하세요 : "))
        if delmenu not in myMenu.keys():
            print(f"현재 메뉴에서는{delmenu}가 없습니다")
        else :
            myMenu.pop(delmenu)
            print("* 메뉴 수정 완료")
    elif (num==9):
        print("종료합니다")
        break
    






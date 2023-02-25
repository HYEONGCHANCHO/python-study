'''
 게임 시작

 컴퓨터 문자열 가위바위보 만들고 각각 나누기
 랜덤 인포트 해서 하나씩 가져오기 
 총 2개 가져올것
 사용자에게 두개 받기 가위 바위 보 중에
컴퓨터 선택 2개 보여주기
사용자가 선택한 2개중에 하나 빼도록 하기
컴퓨터도 하나 빼서 남은거 보여주기
선택된 것들의 결과 보여주고 점수 올리기
반복하기
점수가 일정 점수 이상이되면 승리

'''
import random

rsp=['가위','바위','보']

def radCom(com):
    radIndex=random.randint(0,len(com)-1)
    return com[radIndex]

def makeUser(rsp):
    user=input('2가지 입력 예)1,2 1.가위, 2.바위, 3.보)').split(',')
    userPick=rsp[int(user[0])-1],rsp[int(user[1])-1]
    return userPick

def delPick(userPick):
    userDel=int(input('하나빼기 선택 예) 1 or 2'))
    userPickList=list(userPick)
    finalUserPick=userPickList.pop(userDel)
    return finalUserPick

def delComPick(comPick):
    radIndex=random.randint(0,len(comPick)-1)
    comPickList=list(comPick)
    finalComPick=comPickList.pop(radIndex+1)
    return finalComPick


# ============================

comPick=[]

# ============================
print("하나빼기 게임 시작")
comPick=radCom(rsp),radCom(rsp)
userPick=makeUser(rsp)
print(f"컴퓨터의 선택{comPick}")
print(f"당신의 선택{userPick}")
finalUserPick=delPick(userPick)
finalComPick=delComPick(comPick)
print(f"컴퓨터의 선택 {finalComPick}")
print(f"당신의 선택 {finalUserPick}")


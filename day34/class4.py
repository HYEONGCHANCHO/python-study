class Calculator:
    def __init__(self):
        self.result=0
    def add(self,num):
        self.result += num
        return self.result

cal1=Calculator()
cal2=Calculator()
print(cal1.add(3))  #result=3으로 바꾸어 기억함
print(cal1.add(4))  #result=0이 아니라 3으로 기억한 상태에서 4를 더하는 거라 7이 출력됨
print(cal2.add(3))  #result가 저장되어 있는건 cal1이기 때문에 cal2를 부르면 다시 0부터 시작함


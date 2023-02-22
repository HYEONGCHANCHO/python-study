from numpy import sort
sum=[]
def makeSum():
    for i in range(5):
        korean=int(input(f"{i+1}번째 학생 국어점수 입력"))
        english=int(input(f"{i+1}번째 학생 영어점수 입력"))
        math=int(input(f"{i+1}번째 학생 수학점수 입력"))
        sum.append(korean+english+math)
    return sum

def printSum(finalSum):
    for i in range(5):
        print(f'성적 {5-i}위는 {finalSum[i]}')

sum=makeSum()
finalSum=sort(sum)
printSum(finalSum)
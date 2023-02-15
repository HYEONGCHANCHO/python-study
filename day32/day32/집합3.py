# my_set={1,2,3,4,5,6,12,24}
# n=int(input("Enter the number you want to remove :"))
# my_set.discard(n)
# print("After Removing:",my_set)
#set에 새로운 여러 요소를 추가하기
# set1=set([1,2,4,"John",'cs'])
# set1.update(["Apple","Mango","Grapes"])
# print(set1)

# set1=set(["peter","Joseph",65,59,98])
# set2=set(["peter","Joseph",1,2])
# print(set1.intersection(set2))
# print(set1&set2)

# set1={23,44,56,67,90,45,"Javapoint"}
# set2={13,23,56,76,"nt"}
# print(set1.symmetric_difference(set2))
# print(set1^set2)

set1 = set(["Peter","James","Camroon","Ricky","Donald"])
set2 = set(["Camroon","Washington","Peter"])
set3 = set(["Peter"])

issubset=set1>=set2
print(issubset)
#왼쪽집합이 오른쪽 집합의 상위집합인지, =가 있을 때는 만약 같다면 true로 간주
issuperset=set1<=set2
print(issubset)
#왼쪽집합이 오른쪽 집합의 부분집합인지, =가 있을 때는 만약 같다면 true로 간주

# #set이 같은지 다른지 비교
# a={1,2,3,4}
# print(a=={1,2,3,4})
# print(a=={1,2,4,3})

# #set에 겹치는 요소가 있는지 없는지 확인하기
# print(a.isdisjoint({5,6,7,8}))
# print(a.isdisjoint({3,4,5,8}))

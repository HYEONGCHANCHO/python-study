#union of two sets

#using |
# days1={"monday","Tuesday",'We',"Th","Sun"}
# days2={"Fri","Sat",'Sun'}
# print('days1과 day2를 합치면',days1|days2)

#intersection of two sets
#using & 연산자
# days1={"monday","Tuesday",'We',"Th","Sun"}
# days2={"monday","Tuesday",'We',"abc"}
# # print('days1과 day2의 겹치는 요소들만',days1&days2)
# # print(days1.intersection(days2))

# set1={1,2,3,4,5,6,7}
# set2={1,2,20,32,5,9}
# set3=set1.intersection(set2)
# print(set3)

# #intersection_update()메소드는 원하지 않는 항목을 제거하여 원래 집합을 수정하지만 intersection()메서드는 새로운 집합을 반환한다.
# #intersection_update() 메서드는 다른 두 집합 모두에 없는 요소를 a집합에서 제거하여 원래 a집합의 내용을 수정
# a = {"Devansh", "bob", "castle"}
# b = {"castle", "dude", "emyway","bob"}
# c = {"fuson", "gaurav", "castle"}
# a.intersection_update(b,c)
# print('intersection_update후 a',a)
# print('intersection_update후 b',b)
# print('intersection_update후 c',c)

#Using - 기호
# days1 = {"Monday",  "Tuesday", "Wednesday", "Thursday"}
# days2 = {"Monday", "Tuesday", "Sunday"}
# print(days1-days2)
# print(days1.difference(days2))

#기호 ^ 두집합에서 중복된 부분을 제외
a={1,2,3,4,5,6}
b={1,2,9,8,10}
c=a^b
print(c)
d=a.symmetric_difference(b)
print(d)
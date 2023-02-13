# s1=set([1,2,3,1,2,3])
# s2=set("Hello")
# print(s1)
# print(s2)

# list_s1=list(s1)
# list_s2=list(s2)
# print(list_s1)
# print(list_s2)
# print(list_s1[1])
# print(list_s2[1])

s1=set([1,2,3,4,5,6])
s2=set([4,5,6,7,8,9])

print(s1 &s2)
print(s1.intersection(s2))

print(s1|s2)
print(s1.union(s2))

print(s1-s2)
print(s1.difference(s2))
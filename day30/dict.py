# dict1={"name":"jawon","age":20,"phone":"010-1111-2222"}
# dict2={1:"hello"}
# dict3={"a":[1,2,3]}
# dict4={}
# dict5={1:'a'}
# dict5[2] = "b"
# print(dict5)
# dict5['name']='Hong'
# print(dict5)
# dict5['age']=20
# print(dict5)

# dict6={3:[1,2,3,4]}
# print(dict6)

# dict2={"name":"jaewon","age":"20","location":"seoul",1:"a","list_a":[1,2,3,4,5]}
# del dict2[1]
# print(dict2)

# mylist={1:"a",2:"b","name":"Smith","age":20,"a":[1,2,3,4,5]}
# print(mylist[1])
# print(mylist["name"])
# print(mylist["age"])
# print(mylist["a"])

#get()
# a={'name':'Smith','phone':'01012345678','birth':'1990'}
# print("a['name']=",a['name'])
# print("a.get('name')=",a.get('name'))

# # print(a["location"]) #없는 key를 물어보면 오류
# print(a.get("location")) #없는 key를 물어보면 none출력
# print(a.get("location",'not found')) 
# c={'name':'Smith','phone':'01012345678','birth':'1990'}
# # for i in c.keys():
# #     print(i)
# list_c=list(c.keys())
# print(list_c)

# list_d=list(c.values())
# print(list_d)

# list_e=list(c.items())
# print(list_e)

# d={'name':'Smith','phone':'01012345678','birth':'1990'}

# d.clear()
# print(d)


a={'name':'pey','phone':'01012345678','birth':'1990'}
print("name" in a)
print("pey" in a)

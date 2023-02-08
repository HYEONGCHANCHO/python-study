thisdict ={
    "brand" : "Ford", 
    "model" : "Mustang",
    "year" : 2023,
    # "year" : 1990 
    # key가 여러개 중복될 경우 나중에 있는 것이 나온다.
    "colors" : ['red','wjite','blue']
}

print(thisdict)
print(thisdict["brand"])
print(thisdict["model"])
print(thisdict["year"]) 
print(thisdict)
print(len(thisdict))
print(type(thisdict))
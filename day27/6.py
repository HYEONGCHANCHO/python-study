thisdict ={
    "brand" : "Ford", 
    "model" : "Mustang",
    "year" : 2023
}

# print("--> 복사 1")
# udict = thisdict
# print(udict)


# print("--> 복사 2")
# udict = thisdict
# thisdict["brand"]="kia"
# print(thisdict)
# print(udict)


print("--> 복사 2")
udict = thisdict.copy()
thisdict["brand"]="kia"
print(thisdict)
print(udict)

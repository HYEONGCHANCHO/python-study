mylength='Hello World'
print(len(mylength))

myindexing="Life is too short, You need python"
print(myindexing[2])
print(myindexing[-1])

str="Life is too short, You need python"
print(str[0:4])
print(str[:])
print(str[:4])
print(str[18:])
print(str[:-1])
print(str[2:34:3])

count_str="adgveaeaagegeg"
print(count_str.count('e'))

find_str='python'
print(find_str.find('o'))
print(find_str.find('!'))

a='hello'
print(a.upper)
b="PYthon"
print(b.lower())

str1="python"
print(".".join(str1))
print("-".join(str1))

#공백없애기

print('0123456789')
a="          hi           "
print(a.lstrip()+"*") 
print(a.rstrip()+"*")
print(a.strip()+"*")

str3="Life is too short"
print(str3.replace("short","long"))

str4="Life is too short"
print(str4.split())

str5="Life : is : too : short"
print(str4.split(":S"))
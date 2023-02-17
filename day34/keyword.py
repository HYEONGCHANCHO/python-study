import keyword
key=list(keyword.kwlist)
print(key)

for i in range(len(key)):
    print("[{:^10}]".format(key[i]),end="")
    if (i+1)%5==0:
        print('\n')


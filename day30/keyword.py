import keyword
# print(keyword.kwlist)

rebesed_word=keyword.kwlist

# for x in range(int(len(rebesed_word)/5)):
#     print(rebesed_word[x:x+5])
for x in range(int(len(rebesed_word))):
    print("[{:^10}]".format(rebesed_word[x]),end="")
    if (x+1)%5==0:
        print("\n")


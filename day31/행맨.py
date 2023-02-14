secretWord="hload"
print(secretWord[0])
print(secretWord[1])
print(secretWord[2])

correctLetter="hello"
for i in range(len(correctLetter)):
    print("\n i->",i,end='')
    if secretWord[i] not in 'hello':
        print("없음")
        break

# if 'e' not in 'hello':
#     print('-')
# else :
#     print
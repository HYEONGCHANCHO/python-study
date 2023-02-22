import random

words="elephant,human,rabbit,rhinocerose,whale,bat,eel,hagfish,lamprey,minnow,ray,salmon,seahorse,shark,chicken,hummingbird,falcon,flamingoe,ostriche,owl,parrot,penguin,pigeonsw".split(',')
# =========================================================
def makeSecret(words):
    secretWord=words[random.randint(0,len(words)-1)]
    return secretWord

def firstshow():
    print("==게임 시작")
    secretWord=makeSecret(words)
    print(secretWord)

def pickWord(alguess):
    while True:
        guess=input("알파벳 한글자 입력")
        if len(guess) != 1:
            print("한글자만 입력하세요")
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print("알파벳만 입력하세요")
        elif guess in alguess:
            print("이미 물어본 알파벳입니다")
        else :
            return guess

def checkWord(guess,secretWord,cWord,wWord):
    if guess in secretWord:
        cWord+=guess
    else:
        wWord+=guess
    return cWord,wWord
    

# =========================================================
alguess='+'
cWord=''
wWord=''
secretWord=''

# =========================================================

# firstshow()
# for i in range(5):
#     guess=pickWord(alguess)
#     print('guess',guess)
#     cWord,wWord=checkWord(guess,secretWord,cWord,wWord)
#     print('cWord',cWord)
#     print('wWord',wWord)
firstshow()
while True:
    guess=pickWord(alguess)
    #cWord,wWord=
    checkWord(guess,secretWord,cWord,wWord)
    print('cWord',cWord)
    print('wWord',wWord)


    


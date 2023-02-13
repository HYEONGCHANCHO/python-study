import random
words="elephant,human,rabbit,rhinocerose,whale,bat,eel,hagfish,lamprey,minnow,ray,salmon,seahorse,shark,chicken,hummingbird,falcon,flamingoe,ostriche,owl,parrot,penguin,pigeonsw".split(',')

def wordselet(x):
    wordIndex=random.randint(0,len(x)-1)
    return x[wordIndex]

secretWord=wordselet(words)
# print(secretWord)
alreadyGuessed=''

while True:
    # guess=input('>>>').lower
    guess = input('>>>')
    guess = guess.lower()


    def wordCheck() :
        if len(guess) != 1 :
            print("한 단어만 입력하세요")
        elif guess in alreadyGuessed :
            print("이미 입력한 단어입니다.")
            print(f"입력한 단어 목록 {alreadyGuessed}")
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print("알파벳으로 입력하세요")
        else :
            return guess
        
    wordCheck()
    alreadyGuessed +=guess

import random
import os
HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\  |
 / \  |
     ===''']
words="elephant,human,rabbit,rhinocerose,whale,bat,eel,hagfish,lamprey,minnow,ray,salmon,seahorse,shark,chicken,hummingbird,falcon,flamingoe,ostriche,owl,parrot,penguin,pigeonsw".split(',')
# ==============선언 부분=============================
oldguess=''
newGuess=''
wword=''
cword=''
Gameset=False
# ==============함수 부분============================
def makesecret(words):
    x=random.randint(0,len(words))
    return words[x]

def makeguess(oldguess):
    while True:
        guess=input("알파벳을 입력하세요")
        if len(guess) !=1:
            print("한글자만 입력하세요")
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print("알파벳으로 입력하세요")
        elif guess in oldguess:
            print("이미 물어본 내용입니다.")
        else:
            return guess

def displayMan(newGuess,wword,secretWord,cword,blank,Gameset):
   while True:
    for i in range(len(secretWord)):
        if newGuess==secretWord[i]:
            blank=blank[:i]+secretWord[i]+blank[i+1:]
            cword+=newGuess
    if newGuess not in secretWord:
        wword+=newGuess
    print(HANGMAN_PICS[len(wword)])
    print(f"정답 : {blank}\n")
    print(f"오답 : {wword}\n")
    if secretWord not in cword:
        pass
    else:
        Q=input("게임 승리! 다시 하시겠습니까? (yes or no)")
        if Q.lower().startswith('y'):
            oldguess=''
            newGuess=''
            wword=''
            cword=''
            Gameset=False
        else :
            Gameset=True
            break
    if len(wword)==len(HANGMAN_PICS)-1:
        Q2=input("게임 패배 다시 하시겠습니까? (yes or no)")
        if Q2.lower().startswith('y'):
            oldguess=''
            newGuess=''
            wword=''
            cword=''
            Gameset=False
        else :
            Gameset=True
            break

# def playAgain(secretWord,cword,wword):
    if secretWord not in cword:
        pass
    else:
        Q=input("게임 승리! 다시 하시겠습니까? (yes or no)")
        if Q.lower().startswith('y'):
            oldguess=''
            newGuess=''
            wword=''
            cword=''
            Gameset=False
        else :
            Gameset=True
    if len(wword)==len(HANGMAN_PICS)-1:
        Q2=input("게임 패배 다시 하시겠습니까? (yes or no)")
        if Q2.lower().startswith('y'):
            oldguess=''
            newGuess=''
            wword=''
            cword=''
            Gameset=False
        else :
            Gameset=True
        


# ==============실행 부분=============================
secretWord=makesecret(words)
blank='-'*len(secretWord)
print("=======게임을 시작합니다")
print("H A N G M A N")
print(words)
print(f"해당단어는{secretWord}")
print(HANGMAN_PICS[0])

while True:


    newGuess=makeguess(oldguess)
    displayMan(newGuess,wword,secretWord,cword,blank,Gameset)
    # playAgain(secretWord,cword,wword)
    if Gameset==True:
        break
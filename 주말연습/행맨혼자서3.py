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
# =========================================================
oldguess=''
newGuess=''
wword=''
cword=''
Gameset=False
# =========================================================
def makesecret(words):
    x=random.randint(0,len(words))
    return words[x-1]

def makeguess(oldguess):
    while True:
        guess=input("알파벳을 입력하세요")
        if len(guess) !=1:
            print("한글자만 입력하세요")
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print("알파벳으로 입력하세요")
        elif guess in oldguess:
            print("이미 물어본 글자입니다.")
        else:
            return guess
        
def cwWordCheck(newGuess,secretWord,cword,wword):
    if newGuess in secretWord:
        cword+=newGuess
    else:
        wword+=newGuess
    return cword,wword

def makeBlank(secretWord,newGuess,blank):
    for i in range(len(secretWord)):
        if newGuess==secretWord[i]:
            blank= blank[:i]+secretWord[i]+blank[i+1:]
    return blank

def displayMan(wword,blank):
    print(HANGMAN_PICS[len(wword)])
    print(f"정답 : {blank}\n")
    print(f"오답 : {wword}\n")

def firstshow(words):
    print("=======게임을 시작합니다=======")
    print("H A N G M A N")
    print(words)
    print(f"시크릿 단어:{secretWord}")
    print(HANGMAN_PICS[0])

# =========================================================
secretWord=makesecret(words)
blank='-'*len(secretWord)
firstshow(words)

while True:

    newGuess=makeguess(oldguess)
    # if newGuess in secretWord:
    #     cword+=newGuess
    # else:
    #     wword+=newGuess
    cword,wword=cwWordCheck(newGuess,secretWord,cword,wword)
    print("cword",cword)
    print("wword",wword)
    blank=makeBlank(secretWord,newGuess,blank)
    # for i in range(len(secretWord)):
    #     if newGuess==secretWord[i]:
    #         blank=blank[:i]+secretWord[i]+blank[i+1:]
    displayMan(wword,blank)
    if secretWord not in cword:
        pass
    else:
        Q=input("게임 승리! 게임을 다시 하시겠습니까? (yes or no)")
        if Q.lower().startswith('y'):
            secretWord=makesecret(words)
            blank='-'*len(secretWord)
            oldguess=''
            newGuess=''
            wword=''
            cword=''
            Gameset=False
            firstshow(words)
        else :
            Gameset=True
            
    if len(wword)==len(HANGMAN_PICS)-1:
        Q2=input("게임 패배! 게임을 다시 하시겠습니까? (yes or no)")
        if Q2.lower().startswith('y'):
            secretWord=makesecret(words)
            blank='-'*len(secretWord)
            oldguess=''
            newGuess=''
            wword=''
            cword=''
            Gameset=False
            firstshow(words)
        else :
            Gameset=True
    if Gameset==True:
        break




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

def getsecretWord(wordfile):
    wordIndex=random.randint(0,len(wordfile)-1)
    return wordfile[wordIndex]



def displayBoard(missLetters):
    missedIndex=len(missLetters)
    print(HANGMAN_PICS[missedIndex])

#--------------------------문제 없음-----------------------------------------


def WordCheck(alreadyGuessed):
    while True:
        guess=input("알파벳을 하나 입력하세요 : ").lower()
        if len(guess) != 1:
            print("알파벳을 하나만 입력하세요 :")
        elif guess in alreadyGuessed:
            print("이미 선택한 알파벳입니다.")
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print("알파벳을 선택하세요")
        else :
            # alreadyGuessed+=guess
            return guess

#----------alreadyGuessed 설정안함

def playAgain():
    answer=input('다시 시작하시겠습니까? (yes or no)')
    return answer.lower().startswith('y')

#-------------yes누르면 True반환-----

print("행맨 게임 시작")
secretWord=getsecretWord(words)
print(secretWord)
missLetters=''
alreadyGuessed=''
correctLetters=''
blank=str('-'*(len(secretWord)))

#----------------문제 없음------

while True:
    displayBoard(missLetters)
    # WordCheck(alreadyGuessed)
    guess=WordCheck(alreadyGuessed)
    
    if guess not in secretWord:
        missLetters+=guess
        print(f"틀린문자 : {missLetters}",end='')
        print(f"정답 :{blank}",end='')
        if len(missLetters)==len(HANGMAN_PICS):
            print('패배하였습니다.')
            if playAgain():
                missLetters=''
                alreadyGuessed=''
                correctLetters=''
                secretWord=getsecretWord(words)
            else:
                break    
    else :
        correctLetters=guess+correctLetters
        for i in range(len(secretWord)):
            if guess in secretWord[i]:
                blank=blank[:i]+secretWord[i]+blank[i+1:]
        print(f"틀린문자 : {missLetters}",end='')
        print(f"정답 :{blank}",end='')
        if blank==secretWord:
            print('승리하셨습니다.') 
            if playAgain():
                missLetters=''
                alreadyGuessed=''
                correctLetters=''
                secretWord=getsecretWord(words)
            else:
                break




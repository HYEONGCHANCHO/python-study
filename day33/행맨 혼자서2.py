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

def randomword(wordleng):
   wordIndex=random.randint(0,len(wordleng)-1)
   return wordleng[wordIndex]

def checkword(alreadyGuessed):
   while True:
      guess=input("알파벳을 입력하시오 :").lower()
      if len(guess)!=1:
         print("한 글자만 입력하세요")
      elif guess in alreadyGuessed:
         print("이미 입력된 글자입니다.\n")
         print(f"이미 입력된 글자{alreadyGuessed}")
      elif guess not in 'abcdefghijklmnopqrstuvwxyz':
         print("알파벳으로 입력하세요")
      else :
         alreadyGuessed+=guess
         return guess

def displayBoard(wrongWord,secretWord,blank,correctword):
   print(HANGMAN_PICS[len(wrongWord)])
   for i in range(len(secretWord)):
      if secretWord[i] in correctword:
         blank=blank[:i]+secretWord[i]+blank[i+1:]
   print(f'틀린 단어 : {wrongWord}\n')
   print(f"정답 : {blank}")
   
def lastcheck(wrongWord,secretWord,blank,outkey,correctword):
        
   if guess not in secretWord:   
      wrongWord+=guess
      if len(wrongWord)==len(HANGMAN_PICS)-1:
         displayBoard(wrongWord,secretWord,blank,correctword)
         print("패배하셨습니다")
         outkey=True
   else:
      correctword+=guess
      if blank==secretWord:
         print("승리하였습니다")
         outkey=True
         
def playAgain():
   print("다시 시작하시겠습니까? (yes or no)")
   return input().lower().startswith('y')

guess=''     
secretWord=randomword(words)
correctword=''
wrongWord=''
outkey=False
blank='-'*len(secretWord)

print('행맨 게임 시작')
print(secretWord)
while True:
   # secretWord=randomword(words)
   displayBoard(wrongWord,secretWord,blank,correctword)
   guess=checkword(correctword+wrongWord)
   lastcheck(wrongWord,secretWord,blank,outkey,correctword)
   
   if outkey:
      if playAgain():
         secretWord=randomword(words)
         correctword=''
         wrongWord=''
      else:
         break

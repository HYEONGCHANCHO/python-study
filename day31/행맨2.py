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
print(words)
# print(HANGMAN_PICS[])

def getRandomWord(wordList):
    wordIndex=random.randint(0,len(wordList)-1)
    print("선택한 인덱스는 ",wordIndex)
    print("해당 단어는 ",wordList[wordIndex])
    return wordList[wordIndex]

def getGuess(alreadyGuessed):
    while True:
        print("원하는 알파벳을 입력 : ")
        guess=input().lower()
        if len(guess) != 1:
            print("알파벳 1개 입력하세요")
        elif guess in alreadyGuessed:
            print("이미 입력했던 알파벳입니다")
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('알파벳을 입력하세요')
        else :
            return guess

def displayBoard(missedLetters,secretWord,correctLetters):
    print(HANGMAN_PICS[len(missedLetters)])
    print('\n')
    print("틀린글자 : ",end='')
    for letter in missedLetters:
        print(letter,end="")
    blank = '-'*len(secretWord)+'\n'
    # print(blank)
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blank=blank[:i]+secretWord[i]+blank[i+1:]
            # print(blank)
    print("맞힌글자 : ",end='')
    for letter in blank:
        print(letter,end='')

def playAgain():
    print("다시 게임을 하시겠습니까 (yes or no)")
    return input().lower().startswith('y')


print('==========게임을 시작합니다==========\n')
print('H A N G M A N')
missedLetters=''
correctLetters=''
secretWord=getRandomWord(words)
gameIsDone=False

while True :
    displayBoard(missedLetters,secretWord,correctLetters)
    guess=getGuess(missedLetters+correctLetters)

    if guess in secretWord:
        correctLetters +=guess
        foundAllLetters=True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters=False
                break
        if foundAllLetters:
            print('게임에 이겼습니다'+secretWord)
            gameIsDone = True

    else :
        missedLetters+=guess
        if len(missedLetters)==len(HANGMAN_PICS)-1:
            displayBoard(missedLetters,secretWord,correctLetters)
            print('주어진 기회를 모두 사용했습니다')
            gameIsDone=True

    if gameIsDone:
        if playAgain():
            missedLetters=''
            correctLetters=''
            gameIsDone=False
            secretWord=getRandomWord(words)
        else:
            break




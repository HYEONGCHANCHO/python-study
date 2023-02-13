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
# print(words)
# print('words[0]',words[0])


#----------------- 랜덤으로 문제 생성------------------
def getRandomWord(wordList):
    wordIndex=random.randint(0,len(wordList)-1)
    return wordList[wordIndex]
# ------------------행맨 그림--------------------------
def displayBoard(missedLetters,correctLetters,secretWord):
    print(HANGMAN_PICS[missedLetters]) #못맞춘 알파벳,missedLetters
    print()

    print('missed letter :',end='')
    for letter in missedLetters:
        print(letter,end='')
    print()
    blank = '-'*len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blank = blank[:i]+secretWord[i]+blank[i+1:]         
    
    for letter in blank:
        print(letter,end='')

# ======================여기까지가 displayBoard()---------------------
def getGuess(alreadyGuessed):
    while True:
        guess = input('>>>')
        guess = guess.lower()
        def wordCheck():
            print("----------")
            if len(guess) != 1:
                print('Please enter a single letter')
            elif guess in alreadyGuessed:
                print("이미 입력한 단어입니다. 다른 알파벳을 입력하세요")    
                print("이미 입력한 단어목록{}.".format(alreadyGuessed))
            elif guess not in 'abcdefghijklmnopqrstuvwxyz':
                print('Please enter a alpabet')
            else :
                return guess



# -------------여기까지 getGuess()--------------------------------------------------
def playAgain():
    print("게임을 계속 하시겠습니까 (yes or no)")
    return input().lower().startswith('y') #true or false로 나옴

print('==============게임을 시작합니다============\n')
print('H A N G M A N')
missedLetters=''
correctLetters=''
secretWord=getRandomWord(words)
# print('secretWord',secretWord)
# -------------------------------------------------------------------------------------------------------------------------

while True:
    displayBoard(missedLetters,correctLetters,secretWord)
    guess=getGuess(missedLetters+correctLetters)


# ==========올바른 단어 입력 체크===============================================================
while True:
    guess = input('>>>')
    guess = guess.lower()
    def wordCheck():
        print("----------")
        if len(guess) != 1:
            print('Please enter a single letter')
        elif guess in alreadyGuessed:
            print("이미 입력한 단어입니다. 다른 알파벳을 입력하세요")    
            print("이미 입력한 단어목록{}.".format(alreadyGuessed))
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a alpabet')
        else :
            return guess
    wordCheck()
    alreadyGuessed +=guess

# ==============정답 체크 ======================================
    if guess in secretWord:
        print("단어가 들어갑니다")
        correctLetters +=guess
        foundAllLetter=True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetter=False
                break
            print("-->{}번째 알파벳 {}, foundAllLetter : {}".format(i+1,secretWord[i],foundAllLetter))
        if foundAllLetter:
            print("모든 알파벳을 찾았습니다"+secretWord+"!")
            break


                
    else :
        print("***")    
#사용자가 입력한 글자가 1글자 인지 확인
#썼던 내용 or 특수문자를 적었을 때 알리기



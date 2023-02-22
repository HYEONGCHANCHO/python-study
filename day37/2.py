import random

# =================================================================
alreadyGuessed=''
secretWord=''
missedLetters=''
guess=''
correctLetters=''
# =================================================================
words='ant baboon badger bat cat cobra crow deer dog donkey duck eagle ferret fox frog goat goose lion monkey mouse owl panda pigeon python rabbit rat salmon seal shark sheep snake spider swan tiger turkey turtle whale wolf zebra'.split()

def getRandomWord(wordList):
    wordIndex=int(random.randint(0,len(wordList)-1))
    return wordList[wordIndex]

def checkLetter(guess,alreadyGuessed):
    while True:
        guess=input('>>>').lower()
        if len(guess) != 1:
            print('Please enter a single letter')
        elif guess in alreadyGuessed:
            print('이미 입력된 글자들입니다. 다른 알파벳을 입력하세요 :')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER')
        else:
            return guess


# =================================================================
secretWord=getRandomWord(words)
print(secretWord)

while True:
    print("원하는 알파벳을 입력하세요")
    guess=checkLetter(guess,alreadyGuessed)
    alreadyGuessed+=guess

    if guess in secretWord:
        foundAllLetters=True
        for i in range(int(len(secretWord))):
            if secretWord[i] not in correctLetters:
                foundAllLetters=False
                break
        for i in range(int(len(secretWord))):
            if guess == secretWord[i]:
                correctLetters=correctLetters+guess
        print('맞는 글자입니다. 현재까지 맞춘 글자는 {}\n'.format(correctLetters))
        if len(secretWord) == len(correctLetters):
            print(f'Yes! The secret word is "{secretWord}"! You have won!')
            gameIsDone=True
            break
    else:
        missedLetters += guess
        print('틀린 글자입니다. 현재까지 못 맞춘 글자는 {} \n'.format(missedLetters))
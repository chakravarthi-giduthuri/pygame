import random
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

words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()

def getrandomwords(wordlist):
  wordindex = random.randint(0,len(wordlist)-1)
  return wordlist[wordindex]


def displayboard(missedletters,correctletters,secretword):
  print(HANGMAN_PICS[len(missedletters)])
  print()
  print('missedletters:',end=' ')
  for letter in missedletters:
    print(letter,end=' ')

  print()
  blanks = '_'*len(secretword)
  for i in range(len(secretword)):
    if secretword[i] in correctletters:
      blanks = blanks[:i] + secretword[i] + blanks[i+1:]
  for letter in blanks:
    print(letter,end=' ')

  print()
def getguess(alreadyguessed):
  while  True:
    print('guess a letter')
    guess = input()
    guess = guess.lower()
    if len(guess)!=1:
      print('please enter a single letter')
    elif guess in alreadyguessed:
      print('you have already guessed that letter choose again')
    elif guess not in 'abcdefghijklmnopqurstuvwxyz':
      print('please enter a letter')
    else:
      return guess
def playagain():
  print('do you want to play again')
  return input().lower().startswith('y')

print('HANGMAN')
missedletters=''
correctletters=''
secretword = getrandomwords(words)
gameisdone = False

while True:
  displayboard(missedletters,correctletters,secretword)
  guess = getguess(missedletters + correctletters)
  if guess in secretword:
    correctletters = correctletters+guess
    foundalllettters = True
    for i in range(len(secretword)):
      if secretword[i] not in correctletters:
        foundalllettters = False
        break
    if foundalllettters:
      print('yes! the secretword is '+ secretword+'ypu have won')
      gameisdone = True
  else:
      missedletters = missedletters +guess
      if len(missedletters) == len(HANGMAN_PICS)-1:
        print('you have run out of guess!\n after'+str(len(missedletters))+str(len(correctletters))+'correctletters, the word is '+secretword)

        gameisdone = True
  if gameisdone:
      if playagain():
          missedletters = ''
          correctletters = ''
          gameisdone = False
          secretword = getrandomwords(words)

      else:
          break

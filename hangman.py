from word import secret
from clear import clearConsole

newWord = []

guessLeft = 9
guessChar = ""

def checkSolved():
  for i in secret:
    if i in newWord:
      pass
    else:
      return False
  return True

def checkChar(x):
  global guessLeft
  for i in secret:
    if x == i:
      newWord.append(x)
      print("That's right!")
      break
  else:
    guessLeft -= 1
    print("That's wrong!")

def printWord():
  if len(newWord) == 0:
    for i in secret:
      print("_", end="")
  else:
    for i in secret:
      for j in newWord:
        if j == i:
          print(i, end="")
          break
      else:
        print("_", end="")
  print("", end=" -> ")

def printHangman(lifes):
  print("You have", lifes ,"guesses left")

clearConsole()
print("Welcome to the game, find the",len(secret)," char long word")

while checkSolved() == False and guessLeft > 0:
  printWord()
  printHangman(guessLeft)
  guessChar = input("Guess a character: ").upper()
  clearConsole()
  checkChar(guessChar)
  if checkSolved() == True:
    clearConsole()
    print("Congrats, you won! -> word to find:", secret)
  elif guessLeft == 0:
    clearConsole()
    print("That's bad, you lose :(")



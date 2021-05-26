
import random
randNumber = random.randint(1, 5)
print(randNumber)
userGuess = None
guesses = 0
while(userGuess != randNumber):    
      userGuess = int(input("Enter yout guess"))

      if (userGuess == randNumber):
            print("Entry matched")
      else:
            if(userGuess>randNumber):
                  print("Entry not mached, Enter a smaller number ")
            else:
                  print("Entry not mached, Enter a largerer number ")
                  

print(f"Your guess the number in {guesses} guesses")

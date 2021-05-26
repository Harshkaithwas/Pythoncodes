#fun game to guess a random number
import random
randNumber = random.randint(1, 10)
# print(randNumber)
userGuess = None
guesses = 0
while(userGuess != randNumber):    
      userGuess = int(input("Enter yout guess"))
      guesses +=1

      if (userGuess == randNumber):
            print("Entry matched")
      else:
            if(userGuess>randNumber):
                  print("Entry not mached, Enter a smaller number ")
            else:
                  print("Entry not mached, Enter a largerer number ")
                  

print(f"Your guess the number in {guesses} guesses")
with open("hiscore.txt","r") as f:
      hiscore = int(f.read())

if(guesses < hiscore):
      print("its a new highscore")
      with open("hiscore.txt","w") as f:
            f.write(str(guesses))
      

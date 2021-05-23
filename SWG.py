# funTask
import random


print("Player 1 turn :  Snake(s) Water(w), Gun(g) ? ")
randm = random.randint(1, 3)
if randm== 1:
      comp ="s"
elif randm==2:
      comp ="w"
elif randm==3:
      comp ="g"

you = input("Player 2 turn :  Snake(s) Water(w), Gun(g) " )



def game(comp, you):
      if comp==you:
            return None
      elif comp=='s' :
            if you == 'w':
                  return False
            elif you=='g' :
                  return True
      elif comp=='w':
            if you=='s':
                  return True
            elif you=='g':
                  return False
      elif comp=='g':
            if you=='s':
                  return False
            elif you=='w':
                  return True
      else:
              return "not allowed"



a = game(comp, you)

print(f"Computer chooses {comp} ")
print(f"you chooses {you}")


if a == None:
      print("The game is tie ")
elif a:
      print("You won")
else:
      print(print("You lose"))

import random
print("NUMBER Guessing game")
Number=random.randint(1, 9)
chances=0
print("guess a number between 1 and 9:")

while chances < 5:
      guess = int(input("enter your guess"))
      if guess==Number:
            print("congratulations, you won!")
            break
      elif guess<Number:
            print("your guess was too low: guess a number higher than", guess)
      else :
            print("your guess was too high: guess a number lower than", guess)

      chances+=1
if not chances<5:
      print("you lose, please try again, the number is", Number)



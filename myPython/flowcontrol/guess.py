print("Please guess number between 1 to 10")
guess = int(input())
answer = 5
for i in range (0,10) :
  if guess < answer :
      print("Please guess higher")
      guess = int(input())
  elif guess > answer :
      print("Please guess lower")
      guess = int(input())
  else :
      print("Its 5")
      break
if guess == answer :
    print ("You won the lottery")
else :
    print ("Game Over")

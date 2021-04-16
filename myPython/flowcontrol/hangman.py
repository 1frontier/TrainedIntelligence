secret        = "diamondiskey"
winning_word  = secret
chances       = 5
mistakes      = 0
correct_count = 0 
answer        = input("Enter a character  ")
guessed       = ""

for i in range (0, 26):
  if answer in secret :
      print ("U got it")
      print ("U guessed : {0}".format(answer))
      correct_count += 1
      secret = secret.replace(answer, "")
      print("keep it up, u have {0} chances left ".format(5 - mistakes))
      guessed += answer
      if(secret == "") :
          print ("secret word is {0}".format(winning_word))
          break 
      answer = input("Enter next character  ")
  elif answer in guessed : # player already guessed the letter, so, no deduction in chances
    print("U already guessed {0}".format(guessed))
    answer = input("Enter next character  ")
  else : 
      mistakes += 1
      chances  -= 1
      if chances > 0 and answer not in secret :
        answer = input ("guess again, u have {0} chances left ".format(chances))
      else :
        print ("U lost")
        break

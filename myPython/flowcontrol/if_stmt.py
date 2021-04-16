name = input("tero naam k ho")
age  = int (input ("kati umer vo {0} ?".format(name)))

if age > 0 and age >= 18 and age < 100 :
  print ("vote halna pais")
  print ("bihe ni handey hunsa")
elif age > 200 :
    print("talai dinosaur !!!")
else: 
  print("bacchai resa")
  print ("naabalig hos, kurr {0} barsa".format(18-age))

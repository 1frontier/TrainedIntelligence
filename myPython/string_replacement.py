print("There are {0} days , {1} months in a year " .format(30,12))

for i in range (1, 20) :
    print("No. {0:2} squared is {1:4} and cubed is {2:4}".format(i, i ** 2, i ** 3))

print (f"Pi is equal to {22/7 :<100.50f}")
print (f"Pi is equal to {22/7 :^50.5f}")
print (f"Pi is equal to {22/7}")

data = "1:A, 2:B, 3:C, 4:D, 5:E, 6:F, 7:G, 8:H"

print(data[::5])
print(data[0:-1:5])
print(data[:-1:5])
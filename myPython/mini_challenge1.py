test = "we win"
for i in range (0,6):
    print ( i , test[i])
print('\n')

for i in range (6,0):
    print (i, test[i - 6])
print('\n')

print(test[0:6])
print(test[:6])

print("negative slicing \n") 
print(test[-1])
print(test[:-1])
#print(test[-4:6])
print(test[-4:6])

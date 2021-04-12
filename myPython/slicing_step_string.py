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


print("step \n") 
print(test[0:6:2])


number = "0:111,222:333:444;555"
sep    = number[1::4]
print(sep)

values = "".join(char if char not in sep else " " for char in number).split()
print(values)
print()
print([int(val) for val in values] )
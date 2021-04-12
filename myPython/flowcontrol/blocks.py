x= 0
y= 1
print("Printing 20 fibonacci series \n")
print(f"No.{0}  {0:<10}")
print(f"No.{1}  {1:<10}")
for i in range (2,20):
    z=x+y
    print(f"No.{i}  {z:<10}")
    x=y
    y=z
print("**" * 50)
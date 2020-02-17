import random
r=0
print("welcome")
print("you got 5 chances to get the number")
for e in range(0,5):
    b=int(input("enter the a number"))
    print("random numberis",end=" ")
    a=random.randint(1,6)
    print(a)
    if (a==b):
        print("you won")
        r=1
        break
    else:
        r=0
        pass
if (r==0):
    print("you loose")
else:
    pass

from random import randint

x = randint(1, 100)
max = x
for i in range(1,100):

    x = randint(1, 100)
    if max > x:

        print(x)
    elif x > max:
        max=x
        print(x,"<--UPD")
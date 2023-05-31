x = int(input("Input number: "))

while x !=0 :
    while x !=1:
        if x%2 == 0:
            x = x//2
        else:
            x = (x*3)+1
        print(x)
    x =  int(input("Input x: "))
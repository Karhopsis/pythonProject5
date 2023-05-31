
num = 0

for i in range(100):
    num+=1
    if num%3 == 0 and num%5 == 0:
        print("Bombass")
    elif num%3 == 0:
        print("Fizz")
    elif num%5 ==0:
        print("Buzz")
    else:
        print("My num is: ", num)
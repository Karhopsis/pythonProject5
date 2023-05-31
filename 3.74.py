import math
x = float(input("Input x: "))
guess = x/2


for i in range(1,100):
    guess = (guess+(x/guess))/2
    print("Guess: ",guess)

y = math.sqrt(x)
print(y)
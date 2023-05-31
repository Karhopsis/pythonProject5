import random

n = random.randint(-1,36)

print("your number: ",n)

numbers = {'Green' : range(-1,0), 'Red':(1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34)}

if n in numbers['Green'] and n == -1:
    print("00")
    print("Winning number: ",n)
    print("Winning color is Green ")
elif n in numbers['Green'] and  n == 0:
    print("0")
    print("Winning number: ", n)
    print("Winning color is Green ")
elif n in numbers['Red'] and n%2 == 0:
    print("Even")
    print("Winning number: ", n)
    print("Red")
elif n in numbers['Red'] and n%2 == 1:
    print("Odd")
    print("Winning number: ", n)
    print("Red")
elif n not in numbers and n%2 == 0:
    print("Even")
    print("Winning number: ", n)
    print("Black")
elif n not in numbers and n % 2 == 1:
    print("Odd")
    print("Winning number: ", n)
    print("Black")

if n in range(1,18):
    print("1 to 18")
else:
    print("19 to 36")
name = input("Input value: ")

letters_one = ['a','c','e','g']
letter = name[0]
letters_two = ['b','d','f','h']
number = int(name[1])



if number<=8 and number%2 == 0 and letter in letters_one:
    print("Your collor is white")
elif number<=8 and number%2 == 0 and letter in letters_two:
    print("black")
else:
    print("error")
#elif number%2 == 1 and letter == 'b' and number <=8 and number >0 or letter == 'd' or letter == 'f' or letter == 'h':
   # print("Your collor is black")





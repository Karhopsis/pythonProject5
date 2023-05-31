def nextprime(num):
    counter = 0
    for i in range(2, num):
        if num % i == 0:
            counter += 1
    if counter <= 0:
        return True
    else:
        return False

test = 67
if nextprime(test) == True:
    while True:
        test+=1
        nextprime(test)
        if nextprime(test) == True:
            print(test)
            break
        else:
            test = test
else:
    print('ne proste')
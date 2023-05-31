import random

def znak():
    result = ''
    min_lenght = 3
    max_lenght = 4
    newold = random.randint(0,1)
    if newold == 0:
        for i in range(random.randint(min_lenght, max_lenght)):
            res = random.randint(1,9)
            result += str(res)
        for i in range(3):
            res = random.randint(65,90)
            result += chr(res)
        return result
    else:
        for i in range(3):
            res = random.randint(65,90)
            result += chr(res)
        for i in range(3):
            res = random.randint(1,9)
            result += str(res)
        return result

print(znak())
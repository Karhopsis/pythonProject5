import random

def password():
    result = ''
    min_lenght = 7
    max_lenght = 10
    for i in range(random.randint(min_lenght,max_lenght)):
        res = random.randint(36,126)
        res = chr(res)
        result+=res
    return result

print(password())

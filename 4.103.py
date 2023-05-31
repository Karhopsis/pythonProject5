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


def checkpass(s):
    counter=0
    counter1 = 0
    counter2 = 0
    counter3 = 0
    for i in range(len(s)):
        if len(s) == 8:
            counter+=1
        else:
            print('need 8 char')
            break
        if s[i].isupper() == True:
            counter1+=1
        if s[i].islower() == True:
            counter2+=1
        if s[i].isdigit() == True:
            counter3+=1

    if counter1>=1 and counter2>=1 and counter3>=1:
        return 'safe'
    else:
        return 'error'
n = 1
s = password()
while checkpass(s)!='safe':
    s = password()
    n+=1

print('chances: ',n,s)
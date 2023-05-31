numbers = {0:"first",1:"second",2:"third"}
gifts = {0:"",1:" two turtle doves", 2:" three french hens"}

def verse(day):
    p =''
    o = 0
    if day > 0:
        for i in range(day-1):
            p = gifts[day-1]
    s = " On the "+numbers[day]+"\n"+" my true love sent to me "+p+gifts[day]+' and a partrige in a peartree'
    return s

for j in range(3):
    print(verse(j))

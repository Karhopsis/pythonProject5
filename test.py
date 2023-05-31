numbers = {0:"first",1:"second",2:"third"}
gifts = {0:"",1:" two turtle doves", 2:" three french hens"}

def verse(day):
    s = " On the "+numbers[day]+"\n"+" my true love sent to me "+gifts[day]+' and a partrige in a peartree'
    #if day > 1:
        #for i in range(day-1):
            #p = gifts[i]
    return s


print(verse(2))

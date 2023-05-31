from random import randint


s = ''
n = 0
avg = 0
coin = randint(0, 1)
sum = 0

for i in range(10):
    while 'OOO' not in s and 'PPP' not in s:
        if coin == 0:
            s= s+ 'O'
        else:
            s= s+ 'P'
        coin = randint(0,1)
        n += 1
    print(s, n, "tries")
    sum = sum +n
    n = 0
    s = ''
print("avg = %.2f"%(sum/i))
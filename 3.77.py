list = [1,2,3,4,5,6,7,8,9,10]
res = 0
multiplier = 1

for j in range(len(list)):
    print(multiplier,end="")
    for i in list:
        res = i * multiplier
        print("%4d" %res,end="")
    print("")
    multiplier += 1
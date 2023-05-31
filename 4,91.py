def ordinaldate(month,day,year):
    res = day
    count = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:30,9:30,10:31,11:30,21:31}

    if day >31:
        print("Day must be in range 1-31")
        quit()
    if year%400:
        count[2] = 29

    for i in range(1,month+1):
        if i > 1:
            res = res + count[i-1]

    return res

print(ordinaldate(12,31,1900))

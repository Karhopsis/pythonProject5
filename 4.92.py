def ordinaldate(day):

    count = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:30,9:30,10:31,11:30,12:32}
    dayg = 0
    monthg = 0
    res = ''
    for i in range(1,len(count)+1):
        if day <= count[i]:
            dayg = day
            monthg = i
            res = str(day-1) + ' ' + str(monthg)
            break
        else:
                day = day - count[i]


    return res

print(ordinaldate(364))

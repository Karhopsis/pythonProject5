def magicdate(d,m,y):
    yd=y%10+(y%100-y%10)

    if yd == d * m:
        return True
    else:
        return False




print(magicdate(10,6,1960) )
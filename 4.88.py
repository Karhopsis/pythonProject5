def med(a,b,c):
    med = 0
    if a > b and a < c:
        med = a
    elif b>a and b<c:
        med = b
    else:
        med = c
    return med

print(med(5,1,3))
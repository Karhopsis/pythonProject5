def prostoe(num):
    counter = 0
    for i in range(2,num):
        if num % i == 0:
            counter+=1
    if counter<=2:
        return True
    else:
        return False




print(prostoe(67))
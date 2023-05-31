
def addtoolist(n):
    s = int(input("Input number: "))
    l = []
    while s != 0:
        l.append(s)
        s = int(input("Input next number: "))
    l = sorted(l)
    if len(l) > 4:
        for i in range(n):
            l.remove(max(l))
            l.remove(min(l))
    else:
        raise TypeError('Error')

    return l


print(addtoolist(3))


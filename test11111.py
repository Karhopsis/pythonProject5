def plusOne(digits):

    l = []
    s = ''.join(str(x) for x in digits)
    result = int(s) + 1
    result = str(result)
    for i in result:
        l.append(int(i))

    return l

print(plusOne([1,2,3]))
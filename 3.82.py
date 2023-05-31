s = int(input())

res = ''
r = 0
print(bin(s))
while s !=0:
    r = s%2
    res = str(r)+res
    s = s//2
    print(s)
print(res)



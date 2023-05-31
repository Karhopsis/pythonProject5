x = int(input("Input x: "))
y = int(input("Input y: "))

d = x
n = x%d
s = y%d
while n != 0 or s != 0:
    d = d-1
    n = x % d
    s = y % d
    print(d)

print((x/d),(y/d))




s = int(input("Input number: "))
l = []
while s !=0:
     l.append(s)
     s = int(input("Input next number: "))

l = reversed(sorted(l))

for i in l:
    print(i)
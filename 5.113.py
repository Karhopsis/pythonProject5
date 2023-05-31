s = input("Input word: ")
l = []
while s != '':
    l.append(s)
    s = input("Input next word: ")



for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i] == l[j]:
            del l[j]


.
for i in l:
    print(i)

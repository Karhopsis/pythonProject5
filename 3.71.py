pi = 0
i=1
pitotal=0
for x in range(100):
    i +=1
    pi =4/((i)*(i+1)*(i+2))
    if x % 2 == 1:
        i +=1
        pitotal=pitotal-pi
    else:
        i += 1
        pitotal = pitotal+pi
    print(pitotal + 3)


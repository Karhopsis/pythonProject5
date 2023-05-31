angles = int(input("enter number of angles "))

if angles>3 and  angles<9 :
    print("this figure does not exist")
elif angles == 3:
    print("this is triangle")
elif angles == 4:
    print("this is tetragon")
elif angles == 5:
    print("this is pentagon")
elif angles == 6:
    print("this is hexagon")
elif angles == 7:
    print("this is heptagon")
elif angles == 8:
    print("this is octagon")
elif angles == 9:
    print("this is nonagon")
else:
    print("out of range")

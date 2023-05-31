name=float(input("Enter note: "))


C4_FREQ = 261.63
D4_FREQ = 293.66
E4_FREQ = 329.63
F4_FREQ = 349.23
G4_FREQ = 392.00
A4_FREQ = 440.00
B4_FREQ = 493.88

if name >=  C4_FREQ-1 and name <= C4_FREQ+1:
    print("note is C4")
elif name >=  D4_FREQ-1 and name <= D4_FREQ+1:
    print("note is D4")
elif name >=  E4_FREQ-1 and name <= E4_FREQ+1:
    print("note is E4")
elif name >=  F4_FREQ-1 and name <= F4_FREQ+1:
    print("note is F4")
elif name >=  G4_FREQ-1 and name <= G4_FREQ+1:
    print("note is G4")
elif name >=  A4_FREQ-1 and name <= A4_FREQ+1:
    print("note is A4")
elif name >=  B4_FREQ-1 and name <= B4_FREQ+1:
    print("note is B4")
else:
    print("Out of range")
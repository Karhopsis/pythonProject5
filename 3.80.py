x = int(input("Input x: "))

factor = 2

while factor <= x:
    if x%factor == 0:
        result = factor
        x = x//factor
    else:
        factor += 1
    print("Simple multilpliers: ", result)
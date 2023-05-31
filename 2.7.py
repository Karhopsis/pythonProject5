a = float(input("enter side A: "))
b = float(input("enter side B: "))
c = float(input("enter side C: "))

if a == b == c:
    print("trianglie is equillateral ")
elif a == b != c or a != b ==c:
    print("triangle is isosceles ")
elif a !=b != c:
    print("triangle is scalene")

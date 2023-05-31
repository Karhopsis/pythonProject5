import math

a=float(input("Input A constant: "))

b=float(input("Input B constant: "))

c=float(input("Input C constant: "))

discr=(b**2)-(4*a*c)
print(discr)
root1=(-b+math.sqrt(discr))/(2*a)
root2=(-b-math.sqrt(discr))/(2*a)

print((a*(-0.08**2)+((b*-0.08)+c)))
if discr <0:
    print("Error")
elif discr == 0:
    print("Root is: ", root1)
    print((a *(root1 ** 2)) + ((b * root1) + c))
elif discr >0:
    print("root", root1)
    print("root", root2)
    print((a *(round(root1,2) ** 2)) + ((b * (round(root1,2))) + c))
    print((a * (root2 ** 2)) + ((b * root2) + c))

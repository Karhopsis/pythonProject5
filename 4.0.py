

age1 = input("Input visitor age")

if age1 == "":
    print("Error")
else:
    age1 = int(age1)

costsum =0
age2 = age1

while age2 != "":

    age = int(age2)
    if age <= 2:
        cost = 0
    elif age >=3 and age <= 12:
        cost = 14
    elif age >= 65:
        cost = 18
    else:
        cost = 23
    age2 = input("Input visitor age")
    costsum = costsum + cost

print("All cost is %.2f"%costsum)
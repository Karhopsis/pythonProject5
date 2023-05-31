age=float(input("Human years?"))

if age <= 0:
    print("Error ya dawg")
elif age <= 2:
    d_age=age * 10.5
    print("Age is", d_age)
elif age >= 2:
    d_age=(age * 4) +13
    print("Age is", d_age)


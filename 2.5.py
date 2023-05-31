month=input("Month?; ")

M=['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
if month == M[0]:
    print("31")
elif month == M[1]:
    print("28 or 29")
elif month == M[2]:
    print("31")
elif month == M[3]:
    print("30")
elif month == M[4]:
    print("31")
elif month == M[5]:
    print("28")


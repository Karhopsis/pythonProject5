import sys


while True:
    s = input("Input bit (must be at least 8): ")
    s = list(s)
    if len(s) <8 or s == "" or len(s)>8:
        print("Error must be 8 elements only")
        break
    else:
        count = s.count("1")

    for i in s:
        if i != "0" and i != "1":
            print(i,"<--- Incorrect number, must be 0 or 1")
            sys.exit()
            print("Error try again")

    if count % 2 == 0:
        print("1")
    elif count % 2 == 1:
        print("0")


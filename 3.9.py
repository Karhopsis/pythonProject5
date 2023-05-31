letterfirst = input("enter mark")
letter = letterfirst
mark = 0
summmark = 0
i=0
while letter != "":

    if letter == "A" or letter == "A+":
        mark=4
    elif letter == "A-":
        mark=3.7
    elif letter == "B+":
        mark=3.3
    elif letter == "B":
         mark = 3
    elif letter == "B-":
        mark = 2.7
    elif letter == "C+":
        mark = 2.3
    elif letter == "C":
        mark=2
    elif letter == "C-":
        mark=1.7
    elif letter == "A-":
        mark=3.7
    elif letter == "D+":
        mark=1.3
    elif letter == "D":
        mark=1
    elif letter == "F":
        mark=0
    i+=1
    summmark=summmark + mark
    letter = input("enter mark")

print("everage mark:",summmark/i)
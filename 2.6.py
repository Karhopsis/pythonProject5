dblvl = int(input("Input noise lvl in db: "))

source = {"hammer":130, "mover":106, "alarm":70, "quiet_room":40}

key =["hammer","mover","alarm","quiet_room"]

if dblvl == source["hammer"]:
    print("hammer")
elif dblvl == source["mover"]:
    print("mover")
else:
    print("goodbye")
mon=input("Enter month: ")
dat=int(input("Enter date: "))

spring = {"Mar":range(20,32),"Apr":range(1,31),"May":range(1,32),"Jun":range(1,21)} #єбейший словник
summer = {"Jun":range(21,32),"Jul":range(1,32),"Oug":range(1,32),"Sep":range(1,22)}
autumn = {"Sep":range(22,31),"Oct":range(1,32),"Nov":range(1,31),"Dec":range(1,21)}
winter = {"Dec":range(21,31),"Jan":range(1,32),"Feb":range(1,29),"Mar":range(1,20)}

if mon in spring and mon == 'Mar' and dat in spring['Mar'] or mon == 'Apr' and dat in spring['Apr'] or mon == 'May' and dat in spring['May'] or mon == 'Jun' and dat in spring['Jun']:
    print("spring")
elif mon in summer and mon == 'Jun' and dat in summer['Jun'] or mon == 'Jul' and dat in summer['Jul'] or mon == 'Oug' and dat in summer['Oug'] or mon == 'Sep' and dat in summer['Sep']:
    print("summer")
elif mon in autumn and mon == 'Sep' and dat in autumn['Sep'] or mon == 'Oct' and dat in autumn['Oct'] or mon == 'Nov' and dat in autumn['Nov'] or mon == 'Dec' and dat in autumn['Dec']:
    print("autumn")
elif mon in winter and mon == 'Dec' and dat in winter['Dec'] or mon == 'Jan' and dat in winter['Jan'] or mon == 'Feb' and dat in winter['Feb'] or mon == 'Mar' and dat in winter['Mar']:
    print("winter")
else:
    print("boolshit")
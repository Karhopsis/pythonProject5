def integer(s):
    s = s.strip()
    k = 0
    for i in s:
        try:
            i = int(i)
            k+=1
        except:
            k=0
            return False
            break

    if k>0:
        return True
    else:
        return False


print(integer(' 31 '))
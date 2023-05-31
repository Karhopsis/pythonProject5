def int2hex(n):
    n = int(n)
    return hex(n)


def hex2int(n):
    try:
        return int(n,16)
    except:
        return 'incorrect number'


print(hex2int('sssssssss'))
import string

def string_function(s):
    arr = []
    check = '.,!?-:;'
    s = s.translate(str.maketrans({key: None for key in check}))

    for i in s:
        arr.append(i)

    for i in range(len(arr)-1):
        if arr[i] == "’" and arr[i-1]  in (string.ascii_lowercase) and arr[i+1] in (string.ascii_lowercase):
            pass
        elif arr[i] == "’" and arr[i-1] == " " and arr[i+1] in (string.ascii_lowercase):
            arr[i]=""
        elif arr[i] == "’" and arr[i+1] == " " and arr[i-1] in (string.ascii_lowercase):
            arr[i] = ""
        elif arr[i] == "’" and arr[i+1] == " " and arr[i-1] == " ":
            arr[i] = ""


    l = s.split()

    return ''.join(x for x in arr)



print(string_function('Hello is’nt!'))
#s[i-1] not in (string.ascii_lowercase) and s[i+1] not in (string.ascii_lowercase):
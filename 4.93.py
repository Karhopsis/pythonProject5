def centre_string(s,w):
    len_s = ((len(s) - w) // 2)*(-1)
    if len(s) >= w:
        print("Default string")
        s = s
    else:
        s = '1'*len_s + s + '1'*len_s
        return s
print(centre_string("wewee",25))


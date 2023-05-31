def letters(l):
    l+="  "
    symbols = ',.?!'
    s=list(l)
    for i in range(len(s)-1):
        if i == 0 or s[i-2] in '.?!':
            s[i]=s[i].upper()
        if s[i] in symbols:
            s[i+1]=s[i+1].upper()
        if s[i] == 'i' and s[i-1] == " " or s[i+1] == " " and s[i+1] in symbols:
            s[i] = s[i].upper()
    return ''.join(f for f in s)

print(letters('what time do i’ll have to be there? whats the adress?'))

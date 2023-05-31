s = input("Input your number")

n = len(s)-1
res = 0
for i in range(n,-1,-1):
    res = res + int(s[i])*2**(n-i)

print(res)

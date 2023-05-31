alpha = input("Input text: ")
n = len(alpha)-1
print(len(alpha),"",len(alpha))
y = 0
for i in range(n):
    if alpha[i] == alpha[n]:
        y = y+ 0
    else:
        y = y -1
    n = n-1
    #if i == n:
        #break
    print(i)
if y >= 0 :
    print("Palindrom")
else:
    print("Not ")

alpha1 = input("Input text: ")
alpha = alpha1.replace(" ","")
print(alpha)
n = len(alpha)-1
y = 0
for i in range(n):
    if alpha[i] == alpha[n]:
        y = y+ 0
    else:
        y = y -1
    n = n-1
if y >= 0 :
    print("Palindrom")
else:
    print("Not ")

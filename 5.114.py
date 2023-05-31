check = []
num = int(input())
summ = 0
for i in range(1,num):
    if num % i == 0:
        check.append(i)
print(check)
summ = sum(check)
print(summ)
if summ == num:
    print(num,"This is ideal number")
else:
    print(num, "This is not ideal number")












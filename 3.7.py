import math
price = float(input("Input price in doilars: "))

all_price = 0

while price != 0:
    all_price = all_price + price
    price = float(input("Input price in doilars: "))

sum_cent =(all_price*100) % 5
print("Default sum is: ",all_price)
if sum_cent <2.5:
    all_price = all_price-(sum_cent/100)
else:
    all_price = all_price-(sum_cent/100)+0.05
print("Your sum is: ", all_price)
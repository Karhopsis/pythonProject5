goods = [4.95,9.95,14.95,19.95,24.95]
print("price of goods:",goods)
print("with")
for i in goods:
    sale=i*0.6
    markd = i - sale
    print("mark dovn is:%.2f"%markd,"final price:%.2f"%sale)

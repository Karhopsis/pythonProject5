
def jortax(l):
    base_tax = 4.00
    flt = 0.25
    tax_price = (l/140*flt)+base_tax
    return tax_price

l1 = float(input("Length of journey"))
print(jortax(l1))


num1=(int(input("Number 1?")))
num2=(int(input("Number 2?")))
num3=(int(input("Number 3?")))
mini=min([num3,num1,num2])
maxi=max([num3,num1,num2])
summ=sum([num3,num1,num2])
midi=(summ-mini)-maxi
print("Escalating order:", mini, midi, maxi)
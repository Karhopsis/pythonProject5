alpha = 'ABCDEFGHIJKLMONPQRSTUVWXYZ'

input_list = input("Input phrase: ").strip()
input_number = int(input("Input number: "))

res = ''
for i in input_list:
    res+= alpha[(alpha.index(i)+input_number)%len(alpha)]
    print(alpha.index(i))
print(res)


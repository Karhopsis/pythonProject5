numbers = {1:"first",2:"second",3:"thirt",4:"fourth",5:"fifth"}
def convert(num):
    s=numbers[int(num)]
    return s

num = input()
print(convert(num))
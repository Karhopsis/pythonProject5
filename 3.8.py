import math

first_x = float(input("Input next x (For brake press Enter: "))
first_y = float(input("Input next y (For brake press Enter: "))
perim = 0
prev_x = first_x
prev_y = first_y
line = input("Input next x (For brake input 0: ")
while line != "":
    x = float(line)
    y = float(input("Input next y (For brake input 0: "))
    lenght = math.sqrt(((prev_x-x)**2)+((prev_y-y)**2))
    perim=perim + lenght
    prev_x = x
    prev_y = y
    line = input("Input next x (For brake input 0: ")
lenght = math.sqrt(((first_x-x)**2)+((first_x-y)**2))
perim=perim + lenght
print(perim)


import re


# working on regez to solve for blank lines
with open("input.txt", "r") as file:
    row = file.readline()
    for y in row:
        blank = re.findall(r'^\n$')
       
    # print(x)
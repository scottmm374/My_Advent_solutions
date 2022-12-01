

# 2254

weights = []
delim = '\n'

with open("input.txt", "r") as file:

    lines = file.readlines()
    total = 0
    for x in lines:
        if x != delim:
            total += int(x)
        else:
            weights.append(total)
            total = 0
sort_list = sorted(weights)
top_three = sum(sort_list[-3:])
print(top_three)
# print(sort_list.pop())


    


#     while weight:
        
#         each_supply = []
#         if row != '\n':
#             each_supply.append(int(row))
#         elif row == '\n':
            
#             weights.append(each_supply)
            
    
# print(weights)
    
#     for x in row:
#         if x != '\n':
#             weights.append(int(x))
#         else:
#             break
# print(weights)
        

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
# part 2
top_three = sum(sort_list[-3:])

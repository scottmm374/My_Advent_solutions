# SOLVED part 1
houses = [[0 for _ in range(2100)] for _ in range(2100)]
# count_dirs = {}

with open('input.txt', 'r') as file:
    data = file.read()
    row = 0
    col = 0
    for dir in data:
        if dir == '^':
            row -= 1
            houses[row][col] = 1
            
        if dir == 'v':
            row += 1
            houses[row][col] = 1
            
        if dir == '<':
            col -= 1
            houses[row][col] = 1
            
        if dir == '>':
            col += 1
            houses[row][col] = 1
    count = 1
    
    while len(houses) > 0:
        check = houses.pop()
        for visited in check:
            if visited == 1:
                count += 1
print(count)

    # Created to count max number in each direction, to create a 2d array
   


    # for dir in data:
    #     if dir not in count_dirs:
    #         count_dirs[dir] = 1
    #     else:
    #         count_dirs[dir] +=1







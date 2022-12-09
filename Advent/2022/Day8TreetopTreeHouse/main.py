
# forest = []

# with open("input.txt", "r") as file:
#     rows = file.readlines()
#     for x in rows:
#         print(len(x.strip()))
#         tree_line = []
#         for y in x.strip():
#             tree_line.append(int(y))
#         forest.append(tree_line)
        
forest = [[3,0,3,7,3], [2,5,5,1,2], [6,5,3,3,2], [3,3,5,4,9], [3,5,3,9,0]]
# get number of trees on edge
count_outside = ((len(forest) * 2) + (len(forest[0]) - 2) * 2)

visible = 0
not_visible = 0




for tree_row in range(len(forest)):
    
    for tree_col in range(len(forest[tree_row])):
        
        tree = forest[tree_row][tree_col]
       
        if tree_row >= 1 and tree_col >= 1 and tree_row < len(forest) - 1 and tree_col < len(forest[tree_row]) - 1:
           

            x = 1
            up = forest[tree_row - x][tree_col]
            print(up)
            down = forest[tree_row + x][tree_col]
            right = forest[tree_row][tree_col + x]
            left = forest[tree_row][tree_col - x]
        
            blocked = 0
            print(f'<-------Current coodinates {(tree_row, tree_col)}------->')
            print(up)
            # ! UP
            if tree <= up:
                blocked += 1
                print("No going up")
            
            else:
                while x != 0:
                    print(f'Tree:{tree} Up:{up}')
                    x = x - 1
                    if tree < up:
                        blocked +=1
                        break
            x = 1 
            print(up)  
                
            # ! DOWN
            if tree <= down:
                 blocked += 1
                 print("No going down")

            else:
                while x < len(forest):
                    print(f'Tree:{tree} Down:{down}')
                    x = x + 1 
                    if tree < down:
                        blocked +=1
                        break
            x = 1   
            print(up)   

                
            
            # ! RiGHT
            if tree <= right:
                    blocked += 1
                    print("No going right")
            else:
                while x < len(forest[tree_col]):
                    print(f'Tree:{tree} Right:{right}')
                    x = x + 1 
                  
                    if tree < right:
                        blocked +=1
                        break
            x = 1
            print(up)   


            #  ! LEFT
            if tree <= left:
                    blocked += 1
                    print("No going left")
            else:
                while x != 0:
                    print(f'Tree:{tree} Left:{left}')
                    x = x - 1
                    if tree < left:
                        blocked +=1
                        break
            x = 1
            print(up)   

            print(blocked)
            if blocked == 4:
                not_visible +=1
                print(f"{(tree_row, tree_col)} is blocked height {tree}")
            else:
                visible += 1
                print(f"{(tree_row, tree_col)} is VISIBLE height {tree}")
        

print(f'{visible} Visible and {not_visible} NOT Visible')

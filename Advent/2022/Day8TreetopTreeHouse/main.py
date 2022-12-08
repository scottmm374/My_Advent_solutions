
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

visible = []
not_visible = []




for tree_row in range(len(forest)):
    
    for tree in range(len(forest[tree_row])):
        

        if tree_row >= 1 and tree >= 1 and tree_row < len(forest) - 1 and tree < len(forest[tree_row]) - 1:

            up = forest[tree_row - 1][tree]
            down = forest[tree_row + 1][tree]
            right = forest[tree_row][tree + 1]
            left = forest[tree_row][tree - 1]
        
            blocked = 0
            print(f'<-------Current coodinates {(tree_row, tree)}------->')
            if forest[tree_row][tree] < up:
                blocked += 1
                print("No going up")
            else:
                print("keep traveling UP", (tree_row, tree))

        
            if forest[tree_row][tree] < down:
                 blocked += 1
                 print("No going down")
            else:
                print("keep traveling DOWN", (tree_row, tree))


            if forest[tree_row][tree] < right:
                    blocked += 1
                    print("No going right")
            else:
                print("keep traveling RIGHT", (tree_row, tree))
                
            if forest[tree_row][tree] < left:
                    blocked += 1
                    print("No going right")
            else:
                print("keep traveling LEFT", (tree_row, tree))



            if blocked == 4:
                print(f"{(tree_row, tree)} is blocked height {forest[tree_row][tree]}")
        

print(forest)

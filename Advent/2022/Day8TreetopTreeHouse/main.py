


def main():
   

    forest = []

    with open("input.txt", "r") as file:
        rows = file.readlines()
        for x in rows:
            # print(len(x.strip()))
            tree_line = []
            for y in x.strip():
                tree_line.append(int(y))
            forest.append(tree_line)
    
    # forest = [
    #     [9,9,9,9,9,9,9,9],
    #     [3,3,4,3,7,3,0,0], 
    #     [2,2,2,5,5,1,1,1], 
    #     [6,5,3,3,2,1,1,1], 
    #     [3,3,5,2,2,1,1,1], 
    #     [3,5,7,9,0,0,0,0],
    #     [9,9,9,9,9,9,9,9], 
    #     ]
    
    count_outside = ((len(forest) * 2) + (len(forest[0]) - 2) * 2)
    # area = len(forest) * len(forest[0])
    # print(area)
    visible = 0
   

    visible_coods = []
    not_visible_coods = []

# CHECK RIGHT
    def check_right(x=1):
        print(f'RIGHT: {curr_tree}')
        print("INDEX right", tree_col + x, "tree_col", tree_col, "x:", x)
        if tree_col + x == len(forest[0]) - 1:
            print("CHeck right if tree_col + x == len -1", tree_col + x)
            if curr_tree > forest[tree_row][tree_col + x]:
                # print(f' RIGHT Curr: {curr_tree}, CHeCKING: {forest[tree_row][tree_col + x]}')
                return True
            else:
                return False

        
        if curr_tree <= forest[tree_row][tree_col + x]:
            return False
        
        return check_right(x + 1)
    
# CHECK LEFT
    def check_left(x=1):
        
        print(f'Left: {curr_tree}')
        print("inx", tree_col - x, "Tree_col", tree_col, "X", x)

        if tree_col - x == 0:
            
            if curr_tree > forest[tree_row][tree_col - x]:
                # print(f' LEFT Curr: {curr_tree}, CHeCKING: {forest[tree_row][tree_col - x]}')
                return True
            else:
                # print("else",curr_tree, forest[tree_row][tree_col - x])
                return False
        
        
        if curr_tree <= forest[tree_row][tree_col - x]:
            return False
        
        return check_left(x + 1)

# CHECK UP
    def check_up(x=1):
        # x = tree_row
        print(f'UP: {curr_tree}')
        print("inx", tree_row - x, "Tree_row", tree_row, "X", x)
        if tree_row - x == 0:
            
            if curr_tree > forest[tree_row - x][tree_col]:
                print(f' UP Curr: {curr_tree}, CHeCKING: {forest[tree_row - x][tree_col]}')
                return True
            else:
                return False
        
        
        if curr_tree <= forest[tree_row - x][tree_col]:
            return False
        
        return check_up(x + 1)

# Check Down
    def check_down(x=1):
        print(f'Down: {curr_tree}')
        print("inx", tree_row + x, "Tree_row", tree_row, "X", x)
        if tree_row + x == len(forest) -1:
            
            if curr_tree > forest[tree_row + x][tree_col]:
                # print(f' Down Curr: {curr_tree}, CHeCKING: {forest[tree_row + x][tree_col]}')
                return True
            else:
                return False
       
        if curr_tree <= forest[tree_row + x][tree_col]:
            return False
        
        return check_down(x + 1)

    
    for tree_row in range(len(forest)):
    
        for tree_col in range(len(forest[0])):
    
            if tree_row > 0 and tree_row < len(forest) - 1 and tree_col > 0 and tree_col < len(forest[0]) - 1:

                curr_tree = forest[tree_row][tree_col]
                print(f'-------- CURRENT TREE: ({tree_row},{tree_col}) {curr_tree} ------------------ ')

                blocked = 0
                # print("Blocked, should be zero", blocked)
                is_right_visible = check_right()
                if is_right_visible == False:
                    blocked +=1
                    
                is_left_visible = check_left()
                if is_left_visible == False:
                    blocked +=1
                    
                is_up_visible = check_up()
                if is_up_visible == False:
                    blocked +=1
                   
                is_down_visible = check_down()
                if is_down_visible == False:
                    blocked +=1

                # print(blocked)
                if blocked != 4:
                    visible_coods.append((tree_row, tree_col))
                    visible +=1
                else:
                    not_visible_coods.append((tree_row, tree_col))
                   
           
    # print(f'Visible: {visible_coods}\n NOT: {not_visible_coods}')


    print(visible + count_outside)
    print(len(visible_coods), len(not_visible_coods))   
    # print(visible_coods)

if __name__ == "__main__":
    main()




def main():
   
    forest = []

    with open("input.txt", "r") as file:
        rows = file.readlines()
        for x in rows:
            tree_line = []
            for y in x.strip():
                tree_line.append(int(y))
            forest.append(tree_line)
    
    
    count_outside = ((len(forest) * 2) + (len(forest[0]) - 2) * 2)
    visible = 0
   

# CHECK RIGHT
    def check_right(x=1):
       
        if tree_col + x == len(forest[0]) - 1:
            if curr_tree > forest[tree_row][tree_col + x]:
                return True
            else:
                return False

        if curr_tree <= forest[tree_row][tree_col + x]:
            return False
        
        return check_right(x + 1)
    
# CHECK LEFT
    def check_left(x=1):
       
        if tree_col - x == 0:
            if curr_tree > forest[tree_row][tree_col - x]:
                return True
            else:
                return False
        
        if curr_tree <= forest[tree_row][tree_col - x]:
            return False
        return check_left(x + 1)

# CHECK UP
    def check_up(x=1):
       
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
       
        if tree_row + x == len(forest) -1:
            if curr_tree > forest[tree_row + x][tree_col]:
                return True
            else:
                return False
       
        if curr_tree <= forest[tree_row + x][tree_col]:
            return False
        return check_down(x + 1)

    
    for tree_row in range(len(forest)):
        for tree_col in range(len(forest[0])):
                # skip edges since they are all visible
            if tree_row > 0 and tree_row < len(forest) - 1 and tree_col > 0 and tree_col < len(forest[0]) - 1:

                curr_tree = forest[tree_row][tree_col]

                blocked = 0
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

                # check if blocked in all directions
                if blocked != 4:
                    visible +=1

    print(visible + count_outside)
   

if __name__ == "__main__":
    main()

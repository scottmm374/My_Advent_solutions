

def main():
    
    # import data from txt file
    with open("input.txt", 'r') as file:
        input = file.readlines()
        directions = input.pop()


    result_p1 = Not_Quite_Lisp_P1(directions)
    print(result_p1)
    result_p2 = Not_Quite_Lisp_P2(directions)
    print(result_p2)



def Not_Quite_Lisp_P1(data):

    floor = 0
 
    for x in range(len(data)):
        
        if data[x] == '(':
            floor += 1
        else:
            floor -= 1

    return floor
       
 
def Not_Quite_Lisp_P2(data):
    character = None
    stop = False
    floor = 0
 
    for x in range(len(data)):
        
        if data[x] == '(':
            floor += 1
        else:
            floor -= 1
    
        # Track first character to hit basement (Part 2)
            if floor == -1 and stop == False:
                character = x + 1
                stop = True


    return character


if __name__ == "__main__":
    main()



    
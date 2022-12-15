
my_stacks = {
    "1": ['G', 'D', 'V', 'Z', 'J', 'S', 'B'],
    "2": ['Z','S','M','G','V','P'],
    "3": ['C','L','B','S','W','T','Q','F'],
    "4": ['H','J','G','W','M','R','V','Q'],
    "5": ['C','L','S','N','F','M','D'],
    "6": ['R','G','C','D'],
    "7": ['H','G','T','R','J','D','S','Q'],
    "8": ['P','F','V'],
    "9": ['D','R','S','T','J'],
}


with open("input.txt") as f:
    data = f.read().splitlines()

    for crates in data[10:]:
        _ , qty, _, from_list, _, to_list = crates.split()

        count = int(qty)

        while count > 0:
            from_index = len(my_stacks[from_list]) - count
            move_crate = my_stacks[from_list].pop(from_index)
            add_crate = my_stacks[to_list].append(move_crate)
            count -= 1

        # PART !
        # while count > 0:
        #     move_crate = my_stacks[from_list].pop()
        #     add_crate = my_stacks[to_list].append(move_crate)
        #     count -= 1

            
print(my_stacks)

    


result_1 = {
    '1': ['J', 'V', 'S', 'D', 'C', 'F', 'Q', 'W'], 
    '2': ['C'], 
    '3': ['Z'], 
    '4': ['V', 'D', 'R', 'V', 'T', 'G', 'T'], 
    '5': ['H'], 
    '6': ['T'], 
    '7': ['J', 'Z', 'S', 'G', 'B', 'M', 'G', 'H', 'J', 'D', 'F', 'S', 'L', 'B', 'D', 'V', 'R', 'P', 'S', 'R', 'J', 'M'], 
    '8': ['W', 'S', 'Q', 'F', 'M', 'D', 'P'], 
    '9': ['L', 'N', 'G', 'G', 'R', 'C', 'Q', 'S']
    }


        
result_2 =  {
    '1': ['D', 'F', 'M', 'L', 'V', 'C', 'C', 'B'], 
    '2': ['L'], 
    '3': ['S'], 
    '4': ['B', 'N', 'V', 'P', 'S', 'R', 'G'], 
    '5': ['J'], 
    '6': ['S'], 
    '7': ['G', 'V', 'R', 'Q', 'R', 'C', 'M', 'G', 'T', 'D', 'T', 'J', 'W', 'Q', 'H', 'H', 'J', 'R', 'J', 'Z', 'D', 'D'], 
    '8': ['F', 'W', 'V', 'Z', 'P', 'G', 'T'], 
    '9': ['D', 'Q', 'M', 'S', 'G', 'F', 'S', 'S']
    }

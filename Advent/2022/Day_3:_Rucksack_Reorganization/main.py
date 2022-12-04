
def main():
    
    sacks = list()

    item_values = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
        "f": 6,
        "g": 7,
        "h": 8,
        "i": 9,
        "j": 10,
        "k": 11,
        "l": 12,
        "m": 13,
        "n": 14,
        "o": 15,
        "p": 16,
        "q": 17,
        "r": 18,
        "s": 19,
        "t": 20,
        "u": 21,
        "v": 22,
        "w": 23,
        "x": 24,
        "y": 25,
        "z": 26,
        "A": 27,
        "B": 28,
        "C": 29,
        "D": 30,
        "E": 31,
        "F": 32,
        "G": 33,
        "H": 34,
        "I": 35,
        "J": 36,
        "K": 37,
        "L": 38,
        "M": 39,
        "N": 40,
        "O": 41,
        "P": 42,
        "Q": 43,
        "R": 44,
        "S": 45,
        "T": 46,
        "U": 47,
        "V": 48,
        "W": 49,
        "X": 50,
        "Y": 51,
        "Z": 52,
        

    }
    
    sack_groups = list()
    with open("input.txt", "r") as f:

        for lines in f.readlines():
            sacks.append(lines.strip())

    while len(sacks) > 0:
        
        count = 0
        each_group = list()
        while count < 3:

            each_group.append(sacks.pop(0))
            count += 1
        sack_groups.append(each_group)
    a_list = []

    while len(sack_groups) > 0:
        group = sack_groups.pop(0)
        for x in group[0]:
            if x in group[1]:
                if x in group[2]:
                    a_list.append(item_values[x])
                    break
    total = sum(a_list)               
    print(total)
    
#? <-----PART 1----->
    # misplaced = []
    # for items in sacks:
       
    #     mid = len(items) // 2
    #     first_sack = items[:mid]
    #     second_sack = items[mid:]

        
    #     for item in first_sack:
    #         if item in second_sack:
    #             misplaced.append(item_values[item])
    #             print(first_sack, second_sack, item)
    #             break 
                
                

    # print(misplaced)  
    # total = sum(misplaced)
    # print(total)


    # print(sacks)


if __name__ == "__main__":
    main()
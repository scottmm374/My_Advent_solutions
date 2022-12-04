


def main():


    my_list = [
        [1, 2, 3], 
        [4, 5, 6], 
        [7, 8, 9]
        ]
    directions = [['U','L','L'], ['R', 'R','D','D','D' ], ['L','U','R','D','L'], ['U','U','U','U','D']]
    decoded_passcode = ""
    x, y = 1, 1

    decoded_digit = my_list[x][y]

    moves = directions.pop(0)

    while moves:

        passcode = break_code(moves, my_list)




    def break_code(decode_digit, keypad):
        # for move in 

        #     if move == "U" && if :
        #         button = my_list[x - 1][y]
        #     if move == "D":
        #         button = my_list[x + 1][y]
        #     if move == "R":
        #         button = my_list[x][y + 1]
        #     if move == "L":
        #         button = my_list[x + 1][y - 1]

        




if __name__ == "__main__":
    main()
def main():

    registers = dict()
   
    with open('input.txt', 'r') as file:
        data = file.readlines()
        for line in data:
   
            instructions = line.replace('-&gt;', "->").split()
            reg = instructions[-1]
            if reg not in registers:
                registers[reg] = 0
            else:
                continue
    do_things(registers, data)

def do_things(dictionary, arr):  
    update_reg = dictionary

    for line in arr:
        instructions = line.split()
        reg = instructions[-1]
        
        
        if len(instructions) == 3:
            if instructions[0].isnumeric():
                update_reg[reg] = int(instructions[0])
                print(update_reg[reg])
            else:
                x = update_reg[instructions[0]]
                update_reg[reg] += int(x)
                print(update_reg[reg])
            

        elif len(instructions) == 4:
            x = update_reg[instructions[1]]
            val = ~ int(x)
            print("Not", x, val)
            update_reg[reg] = val
        
        else: 
            if instructions[1] == "AND":
                if instructions[0].isnumeric():
                    x = instructions[0]
                    y = update_reg[instructions[2]]
                    val = int(x) & int(y)
                    update_reg[reg] = val
                else:
                    x = update_reg[instructions[0]]
                    y = update_reg[instructions[2]]
                    val = int(x) & int(y)
                # if reg not in registers:
                    update_reg[reg] = val
                # else:
                    # registers[reg] = val

            if instructions[1] == "OR":
                x = update_reg[instructions[0]]
                y = update_reg[instructions[2]]
                val = int(x) | int(y)
                update_reg[reg] = val
               

            if instructions[1] == "RSHIFT":
                x = update_reg[instructions[0]]
                num =  int(instructions[2])
                val = int(x) >> num
                # if reg not in registers:
                update_reg[reg] = val
                # else:
                    # registers[reg] = val

            if instructions[1] == "LSHIFT":
                x = update_reg[instructions[0]]
                num =  int(instructions[2])
                val = int(x) << num
                update_reg[reg] = val
                # else:
                    # registers[reg] = val

    print(update_reg['a'])
# print(registers)


        #    Check for AND
        #    Check for RSHIFT and LSHIFT
        #    Check for OR
        #    Check for NOT
        #    Check for -> only

# def calc_and(data):
#     pass

# def calc_or(data):
#     pass

# def calc_rshift(data):
#     pass

# def calc_lshift(data):
#     pass
# def calc_not(data):
#     pass


if __name__ == "__main__":
    main()


def main():
    cycle = 0
    finalX = []
    instructions = []
    noop_count = 0
    with open('input.txt', 'r') as file:
        line = file.read().split('\n')
        print(line)
        for x in line:
            if x == "noop":
                noop_count +=1
                instructions.append(0)
            else:
                y, num = x.split()
                instructions.append(int(num))
    lookup = {}
    cycle = 1
    sub_total = 1
    y = 0
    for x in instructions:
        if x == 0:
            cycle += 1
            lookup[cycle] = sub_total
        else:
            y = x
            cycle += 1
            lookup[cycle] = sub_total
            cycle +=1
            sub_total += y
            lookup[cycle] = sub_total
            y = 0

    print(lookup[20] * 20 + lookup[60] * 60 + lookup[100] * 100 + lookup[140] * 140 + lookup[180] * 180 + lookup[220] * 220)
      
    
        

main()



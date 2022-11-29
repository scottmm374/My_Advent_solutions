
def main():
    # Need to restructure for tests

    with open("input.txt", 'r') as f:
    
        horizontal = 0
        depth = 0
        aim = 0
        lines = f.readlines()
        for line in range(len(lines)):
            seperated = lines[line].split(' ')
            if seperated[0] == "forward":
                horizontal += int(seperated[1])
                depth += int(seperated[1]) * aim
            if seperated[0] =="down":
                aim += int(seperated[1])
            if seperated[0] =="up":
                aim -= int(seperated[1])

        result = horizontal * depth

        print(result)

#  Includes part 2 .  Part_1 answer 2039256  Part_2 answer  1856459736
if __name__ == "__main__":
    main()  

    
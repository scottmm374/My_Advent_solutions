
def main():
    count = calc_depth_increase()
    print(count)

    
def calc_depth_increase():
    count = 0
    with open("input.txt", 'r') as f:
        
        lines = f.readlines()
        for line in range(len(lines)):
            if line == len(lines) - 1:
                break
            if int(lines[line]) < int(lines[line + 1]):
                # print(f'{lines[line]} is < {lines[line + 1]}')
                count += 1
            else:
                continue

    return count

if __name__ == "__main__":
    main()


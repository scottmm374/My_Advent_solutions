

def main():
    check_stuff = []
    naughty = 0
    nice = 0
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        
        for x in lines:
            isNice = isNaughtOrNice(x.strip())
            if isNice == True:
                # print(f'Nice: {x}')
                nice +=1
            else:
                # print(f'Naughty: {x}')
                naughty += 1

    return naughty, nice       
        
def isNaughtOrNice(line):
    vowels = {"a", "e", "i", "o", "u"}
    exclude_subStrings = {"ab", "cd", "pq", "xy"}
        # must = 3
    count_vowels = 0
    double = 0

    for x in range(len(line)):
        
        if x < len(line) -1:
            # print(x + 1, len(line))
            seq = f'{line[x]}{line[x + 1]}'
            
            if seq in exclude_subStrings:
                # print(f'{line} :{seq}, Naughty')
                return False
            if line[x] == line[x + 1]:
                double +=1
            if line[x] in vowels:
                count_vowels +=1
    
    if line[-1] in vowels:
            count_vowels +=1

    if count_vowels > 2 and double >= 1:
        return True
    
    else:
        return False

print(main())
# (217, 783) 783 too high




count = 0
with open("input.txt", "r") as file:

    x = file.readlines()
    for line in x:
        measure = line.strip().split()
        measurements = [int(a) for a in measure]
        sides = sorted(measurements)
        print(sides)
        sum_sides = sides[0] + sides[1]
        if sum_sides > sides[2]:
            count += 1
        else:
            continue
        
       
print(count) 

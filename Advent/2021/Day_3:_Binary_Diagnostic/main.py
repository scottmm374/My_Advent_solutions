with open("input.txt", 'r') as f:
   
    my_dict = {}
    lines = f.readlines()
    gamma = ""
    epsilam = ""


    for line in range(len(lines)):
       
        for x in range(len(lines[line])-1):
            if x not in my_dict:
                my_dict[x] = 0

                if lines[line][x] == "1":
                    my_dict[x] += 1 
                else:
                    my_dict[x] -= 1

            if lines[line][x] == "1":
                my_dict[x] += 1 
            else:
                my_dict[x] -= 1


            
    for key, value in my_dict.items():
        print(f'key: {key}, value:  {value}')
        if value > 0:
            gamma += str(1)
            print(gamma)
            epsilam += str(0)
        if value <= 0:
            gamma += str(0)
            epsilam += str(1)
  
    power_consumption = int(gamma, 2) * int(epsilam, 2)

    print(power_consumption)


    # Part_1 answer 1025636
    

    
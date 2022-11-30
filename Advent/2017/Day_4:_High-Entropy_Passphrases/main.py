
total = 0
with open("input.txt", "r") as file:
    line = file.readlines()

    for x in line:
        row = x.split()
        my_set = set(row)
        if len(row) == len(my_set):
            total +=1
print(total) 


        

       


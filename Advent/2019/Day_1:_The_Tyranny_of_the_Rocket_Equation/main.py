# Answer: 3372695 Have to track down the code Part_2: 5056172
# Wrote these a couple years ago, tracked down in Repl.it. Need to clean up code WROTE IN JS
import math

def main():

     with open("input.txt", 'r') as file:
        puzzle_input = file.readlines()

        fuel_required, fuel_extra = calc_mass(puzzle_input)
        print(fuel_required)
        new_fuel_required = calc_missing_fuel(fuel_extra)



def calc_mass(data):

    fuel_total = 0
    each_fuel = []
    for num in data:
        sub_total = (math.floor(int(num) / 3)) - 2
        each_fuel.append(sub_total)
        fuel_total += sub_total

    return (fuel_total, each_fuel)

def calc_missing_fuel(fuel_list):

        fuel_total = []
        new_fuel_calc = 0

        for num in fuel_list[10:]:

            fuel_needed = (math.floor(int(num) / 3)) - 2
            
            if fuel_needed > 0:

            

    


        
        









if __name__ == "__main__":
    main()

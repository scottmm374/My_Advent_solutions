import json
import re

def main():
    numbers_list = []
    with open("input.txt", 'r') as file:
        puzzle_input = file.readline()
        numbers = re.findall('-?[0-9]+', puzzle_input)
        
        total = 0
        for num in numbers:
            total += int(num)
        print(total)

        
      

# (You guessed 126674.) . Too high Its not accounting for negatives

        
       




 
        #  numbers = puzzle_input.pop()
       
        


        #   2013 "e"
    

#    f = open('data_file.json',)
#    data = json.load(f)
#    for i in data ['e']:
#         print(i)
#    f.close()
        

#     numbers = sum_all_numbers(puzzle_data)
#     print(numbers)

# def sum_all_numbers(data):
#     return data
    

if __name__ == "__main__":
    main()

 # ? interesting errors

    #  with open('data_file.json', 'r') as read_file:
    #     puzzle_data = json.dump(json.loads(read_file), indent=4, sort_keys=True)
    #     print(puzzle_data)


#     /Users/michellescott/Documents/github/Advent_puzzles_scraper/env/bin/python /Users/michellescott/Documents/github/Advent_puzzles_scraper/2015/Day_
# 12:_JSAbacusFramework.io/main.py
# Traceback (most recent call last):
#   File "/Users/michellescott/Documents/github/Advent_puzzles_scraper/2015/Day_12:_JSAbacusFramework.io/main.py", line 25, in <module>
#     main()
#   File "/Users/michellescott/Documents/github/Advent_puzzles_scraper/2015/Day_12:_JSAbacusFramework.io/main.py", line 9, in main
#     puzzle_data = json.dump(json.loads(read_file), indent=4, sort_keys=True)
#   File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/json/__init__.py", line 339, in loads
#     raise TypeError(f'the JSON object must be str, bytes or bytearray, '
# TypeError: the JSON object must be str, bytes or bytearray, not TextIOWrapper

# <------------------------------------------------------------->

#  with open('data_file.json', 'r') as read_file:
#         puzzle_data = json.dump(read_file, indent=4, sort_keys=True)
#         print(puzzle_data)


# /Users/michellescott/Documents/github/Advent_puzzles_scraper/env/bin/python /Users/michellescott/Documents/github/Advent_puzzles_scraper/2015/Day_
# 12:_JSAbacusFramework.io/main.py
# Traceback (most recent call last):
#   File "/Users/michellescott/Documents/github/Advent_puzzles_scraper/2015/Day_12:_JSAbacusFramework.io/main.py", line 25, in <module>
#     main()
#   File "/Users/michellescott/Documents/github/Advent_puzzles_scraper/2015/Day_12:_JSAbacusFramework.io/main.py", line 9, in main
#     puzzle_data = json.dump(read_file, indent=4, sort_keys=True)
# TypeError: dump() missing 1 required positional argument: 'fp'

#  * Now Im wondering if there is an easter egg inside this puzzle??!!


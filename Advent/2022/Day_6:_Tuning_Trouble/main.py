

# seq_list = "nppdvjthqldpwncqszvftbrmjlhg"
# , "bvwbjplbgvbhsrlpgdmjqwftvncz", "nppdvjthqldpwncqszvftbrmjlhg", "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"]

seq_list = None


with open("input.txt", 'r') as f:
    line = f.readline()
    seq_list = line
   


start = 0
# end = 4
end = 14

while end < len(seq_list):
    window = seq_list[start:end]
    check_window = set()
    for x in window:

        check_window.add(x)
    # if len(check_window) != 4:
    if len(check_window) != 14:
        start += 1
        end += 1

        
    else:
        
        print("end", end)
        break
    
    


# My_Advent_solutions [solutions] git status
# On branch solutions
# Changes not staged for commit:
#   (use "git add <file>..." to update what will be committed)
#   (use "git restore <file>..." to discard changes in working directory)
#         modified:   Advent/2022/Day_6:_Tuning_Trouble/main.py


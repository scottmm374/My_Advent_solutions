


seq_list = None

with open("input.txt", 'r') as f:
    line = f.readline()
    seq_list = line

start = 0
# end = 4  -Part 1 uncomment
end = 14

while end < len(seq_list):
    window = seq_list[start:end]
    check_window = set()
    for x in window:

        check_window.add(x)
    # if len(check_window) != 4: -Part 1 uncomment
    if len(check_window) != 14:
        start += 1
        end += 1
    else:
        print("end", end)
        break
    
    





with open("input.txt", "r") as file:
    row = file.readlines()
    nums = sorted([int(x) for x in row])

    start = 0
    end = len(nums)-1

    while start != end:
        if nums[start] + nums[end] == 2020:
            print(nums[start] * nums[end])
            break
        if nums[start] + nums[end] < 2020:
            print("toosmall")
            start += 1
            
        if nums[start] + nums[end] > 2020:
            end -= 1
    
        


        
        
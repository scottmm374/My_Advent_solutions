
checksum = 0
with open("input.txt", "r") as file:

    x = file.readlines()
    for line in x:
        rows = line.strip().split()
        row = [int(a) for a in rows]
        nums = sorted(row)
        difference = nums[-1] - nums[0]
        checksum += difference
print(checksum)
        
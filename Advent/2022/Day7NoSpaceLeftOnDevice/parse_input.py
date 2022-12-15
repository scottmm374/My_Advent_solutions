
def main():

    system_files = []

    with open('input.txt', 'r') as file:
        lines = file.readlines()
        # print(lines)
        for line in lines:
            instructions = line.strip().split()
            system_files.append(process(instructions))
    print(system_files)        

def process(data):

    if data[1] == 'ls':
        return f'CONTAINS'
    
    if data[1] == 'cd' and data[2] != '..':
        parent_name = f'PARENT_DIR: "{data[2]}"'
        return parent_name 

    if data[1] == 'cd' and data[2] == '..':
        parent_name = f'Move up one Dir'
        return parent_name 

    if data[0].isnumeric():
        child_size = int(data[0])
        child_name = data[1]
        return child_size, child_name

    if data[0] == 'dir':
        child_dir_name = data[1]
        return child_dir_name



if __name__ == "__main__":
    main()





def main():

   

    with open('input.txt', 'r') as file:
        lines = file.readlines()
        # print(lines)
        for line in lines:
            data = line.strip().split()
            
            if data[1] == 'cd' and data[2] != '..':
                parent_name = data[2]
                
                if parent_name not in system_files:
                    system_files[parent_name] = set()

                if data[1] == 'ls':
                    while data[1] != 'cd':

                    # directories
                        if data[0] == 'dir':
                            dir_name = data[1]
                            if dir_name not in system_files:
                                system_files[dir_name] = None

                        if data[0].isnumeric():
                            child_size = int(data[0])
                            file_name = data[1]
                            if file_name not in system_files:
                                system_files[file_name] = child_size
                    
            if data[1] == 'cd' and data[2] != '..':
                parent_name = data[2]
                print("cd into")
                # if parent_name not in system_files:
                #     system_files[parent_name] = None


            if data[1] == 'cd' and data[2] == '..':
                print("Instruction to move up one level")

            
    print(system_files)
            



if __name__ == "__main__":
    main()
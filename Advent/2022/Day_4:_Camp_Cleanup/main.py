

def main():
  inclusive_ranges = 0
  
  with open('input.txt', 'r') as f:
      for line in f.readlines():
        check = check_ranges(line.strip())
        print("results", check)
        if check == True:
          inclusive_ranges += 1
      

  return inclusive_ranges   

def check_ranges(line):
    ranges = [] 
    new_line = line.replace("-",",")  
    ranges.append(new_line.split(","))


  #  Part_2 solution 
    if int(ranges[0][0]) < int(ranges[0][2]) and int(ranges[0][1]) < int(ranges[0][2]) and int(ranges[0][1]) < int(ranges[0][3]):
        print("False", ranges)
        return False
    if int(ranges[0][0]) > int(ranges[0][2]) and int(ranges[0][0]) > int(ranges[0][3]):
        print("False", ranges)
        return False 
    else:  
      print("True", ranges)
      return True



    # PART 1
    # if int(ranges[0][0]) <= int(ranges[0][2]) and int(ranges[0][1]) >= int(ranges[0][3]):
    #     return True
    # elif int(ranges[0][0]) >= int(ranges[0][2]) and int(ranges[0][1]) <= int(ranges[0][3]):
    #     return True 
    # else:  
    #   return False


    

          
        


if __name__ == '__main__':
    result = main()
    print(result)
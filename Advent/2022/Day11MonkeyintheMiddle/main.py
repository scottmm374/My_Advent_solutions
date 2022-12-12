import math
# create rounds up to 20

def main():
    rounds = 0
    monkey_zero = [79, 98]
    monkey_one = [54, 65, 75, 74]
    monkey_two = [79, 60, 97]
    monkey_three = [74]

    m_zero = 0
    m_one = 0
    m_two = 0
    m_three = 0 

    # count = keep_going(rounds)
    
    while rounds <= 5:
        monkey_zero, monkey_two, monkey_three, m_zero = check_monkey_zero(monkey_zero, monkey_two, monkey_three, m_zero)
        monkey_zero, monkey_one, monkey_two, m_one = check_monkey_one(monkey_zero, monkey_one, monkey_two, m_one)
        monkey_one, monkey_two, monkey_three, m_two = check_monkey_two(monkey_one, monkey_two, monkey_three, m_two)
        monkey_zero, monkey_one, monkey_three, m_three = check_monkey_three(monkey_zero, monkey_one, monkey_three, m_three)
        
        rounds  = rounds + 1
        print(f'-------------Round:{rounds}----------')
        print(f'Zero:{monkey_zero}\n, One:{monkey_one}\n, Two:{monkey_two}\n, Three:{monkey_three}')
    else:   
        return f'{m_zero}, {m_one}, {m_two}, {m_three}'

# def keep_going(count):
#     if count == 20:
#         return False
#     return True   

def check_monkey_zero(arr_0, arr_2, arr_3, count):
    
    temp_0 = arr_0
    temp_2 = arr_2
    temp_3 = arr_3
    m_zero = count

    while len(temp_0) > 0:
        m_zero +=1
        item = temp_0.pop(0)
        new = item * 19
        rounded = math.floor(new / 3)
        if rounded % 23 == 0:
            temp_2.append(rounded)
        else:
            temp_3.append(rounded)
    return(temp_0, temp_2, temp_3, m_zero)


def check_monkey_one(arr_0, arr_1, arr_2, count):
    
    temp_0 = arr_0
    temp_1 = arr_1
    temp_2 = arr_2
    m_one = count

    while len(temp_1) > 0:
        m_one +=1
        item = temp_1.pop(0)
        new = item + 6
        rounded = math.floor(new / 3)
        if rounded % 19 == 0:
            temp_2.append(rounded)
        else:
            temp_0.append(rounded)
    return(temp_0, temp_1, temp_2, m_one)



def check_monkey_two(arr_1, arr_2, arr_3, count):
    
    temp_1 = arr_1
    temp_2 = arr_2
    temp_3 = arr_3
    m_two = count

    while len(temp_2) > 0:
        m_two +=1
        item = temp_2.pop(0)
        new = item * item
        rounded = math.floor(new / 3)
        if rounded % 13 == 0:
            temp_1.append(rounded)
        else:
            temp_3.append(rounded)
    return(temp_1, temp_2, temp_3, m_two)


def check_monkey_three(arr_0, arr_1, arr_3, count):
    
    temp_0 = arr_0
    temp_1 = arr_1
    temp_3 = arr_3
    m_three = count

    while len(temp_3) > 0:
        m_three +=1
        item = temp_3.pop(0)
        new = item + 3
        rounded = math.floor(new / 3)
        if rounded % 17 == 0:
            temp_0.append(rounded)
        else:
            temp_1.append(rounded)
    return(temp_0, temp_1, temp_3, m_three)



if __name__ == "__main__":
    print(main())


    # print(f'Monkey_zero has: {monkey_zero} Round: {round}')
    # print(f'Monkey_one has: {monkey_one} Round: {round}')
    # print(f'monkey_two has: {monkey_two} Round: {round}')
    # print(f'monkey_three has: {monkey_three} Round: {round}')

    
    
 


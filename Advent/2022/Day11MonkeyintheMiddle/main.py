import math
# create rounds up to 20

def main():
    rounds = 1
    monkey_zero = [56, 56, 92, 65, 71, 61, 79]
    monkey_one = [61, 85]
    monkey_two = [54, 96, 82, 78, 69]
    monkey_three = [57, 59, 65, 95]
    monkey_four = [62, 67, 80]
    monkey_five = [91]
    monkey_six = [79, 83, 64, 52, 77, 56, 63, 92]
    monkey_seven = [50, 97, 76, 96, 80, 56]

    m_zero = 0
    m_one = 0
    m_two = 0
    m_three = 0 
    m_four = 0
    m_five = 0
    m_six = 0
    m_seven = 0

    # count = keep_going(rounds)
    # Part one
    # while rounds <= 20:
    while rounds <= 1000:

        monkey_zero, monkey_three, monkey_seven, m_zero = check_monkey_zero(monkey_zero, monkey_three, monkey_seven, m_zero)
        monkey_one, monkey_four, monkey_six, m_one = check_monkey_one(monkey_one, monkey_four, monkey_six, m_one)
        monkey_two, monkey_zero, monkey_seven, m_two = check_monkey_two(monkey_two, monkey_zero, monkey_seven, m_two)
        monkey_three, monkey_one, monkey_five, m_three = check_monkey_three(monkey_three, monkey_one, monkey_five, m_three)

        monkey_four, monkey_two, monkey_six, m_four = check_monkey_four(monkey_four, monkey_two, monkey_six, m_four)
        monkey_five, monkey_one, monkey_four, m_five = check_monkey_five(monkey_five, monkey_one, monkey_four, m_five)
        monkey_six, monkey_zero, monkey_two, m_six = check_monkey_six(monkey_six, monkey_zero, monkey_two, m_six)
        monkey_seven, monkey_three, monkey_five, m_seven = check_monkey_seven(monkey_seven, monkey_three, monkey_five, m_seven)
        
        rounds  = rounds + 1
        print(f'-------------Round:{rounds}----------')
        # print(f'Zero:{monkey_zero}\n, One:{monkey_one}\n, Two:{monkey_two}\n, Three:{monkey_three}\n, Four:{monkey_four}\n, Five:{monkey_five}\n, Six:{monkey_six}\n, Seven:{monkey_seven}')


    monkeys = [m_zero, m_one, m_two, m_three, m_four, m_five, m_six, m_seven] 
    find_max = sorted(monkeys, reverse=True)  
    return find_max[0] * find_max[1]
   

def check_monkey_zero(arr_0, arr_1, arr_2, count):
    
    temp_0 = arr_0
    temp_3 = arr_1
    temp_7 = arr_2
    m_zero = count

    while len(temp_0) > 0:
        m_zero +=1
        item = temp_0.pop(0)
        new = item * 7
        # rounded = math.floor(new / 3)
        if new % 3 == 0:
            temp_3.append(new)
        else:
            temp_7.append(new)
    return(temp_0, temp_3, temp_7, m_zero)


def check_monkey_one(arr_0, arr_1, arr_2, count):
    
    temp_1 = arr_0
    temp_4 = arr_1
    temp_6 = arr_2
    m_one = count

    while len(temp_1) > 0:
        m_one +=1
        item = temp_1.pop(0)
        new = item + 5
        # rounded = math.floor(new / 3)
        if new % 11 == 0:
            temp_6.append(new)
        else:
            temp_4.append(new)
    return(temp_1, temp_4, temp_6, m_one)



def check_monkey_two(arr_0, arr_1, arr_2, count):
    
    temp_2 = arr_0
    temp_0 = arr_1
    temp_7 = arr_2
    m_two = count

    while len(temp_2) > 0:
        m_two +=1
        item = temp_2.pop(0)
        new = item * item
        # rounded = math.floor(new / 3)
        if new % 7 == 0:
            temp_0.append(new)
        else:
            temp_7.append(new)
    return(temp_2, temp_0, temp_7, m_two)


def check_monkey_three(arr_0, arr_1, arr_2, count):
    
    temp_3 = arr_0
    temp_1 = arr_1
    temp_5 = arr_2
    m_three = count

    while len(temp_3) > 0:
        m_three +=1
        item = temp_3.pop(0)
        new = item + 4
        # rounded = math.floor(new / 3)
        if new % 2 == 0:
            temp_5.append(new)
        else:
            temp_1.append(new)
    return(temp_3, temp_1, temp_5, m_three)


def check_monkey_four(arr_0, arr_1, arr_2, count):
    
    temp_4 = arr_0
    temp_2 = arr_1
    temp_6 = arr_2
    m_four = count

    while len(temp_4) > 0:
        m_four +=1
        item = temp_4.pop(0)
        new = item * 17
        # rounded = math.floor(new / 3)
        if new % 19 == 0:
            temp_2.append(new)
        else:
            temp_6.append(new)
    return(temp_4, temp_2, temp_6, m_four)


def check_monkey_five(arr_0, arr_1, arr_2, count):
    
    temp_5 = arr_0
    temp_1 = arr_1
    temp_4 = arr_2
    m_five = count

    while len(temp_5) > 0:
        m_five +=1
        item = temp_5.pop(0)
        new = item + 7
        # rounded = math.floor(new / 3)
        if new % 5 == 0:
            temp_1.append(new)
        else:
            temp_4.append(new)
    return(temp_5, temp_1, temp_4, m_five)

def check_monkey_six(arr_0, arr_1, arr_2, count):
    
    temp_6 = arr_0
    temp_0 = arr_1
    temp_2 = arr_2
    m_six = count

    while len(temp_6) > 0:
        m_six +=1
        item = temp_6.pop(0)
        new = item + 6
        # rounded = math.floor(new / 3)
        if new % 17 == 0:
            temp_2.append(new)
        else:
            temp_0.append(new)
    return(temp_6, temp_0, temp_2, m_six)

def check_monkey_seven(arr_0, arr_1, arr_2, count):
    
    temp_7 = arr_0
    temp_3 = arr_1
    temp_5 = arr_2
    m_seven = count

    while len(temp_7) > 0:
        m_seven +=1
        item = temp_7.pop(0)
        new = item + 3
        # rounded = math.floor(new / 3)
        if new % 13 == 0:
            temp_3.append(new)
        else:
            temp_5.append(new)
    return(temp_7, temp_3, temp_5, m_seven)




if __name__ == "__main__":
    print(main())


    # print(f'Monkey_zero has: {monkey_zero} Round: {round}')
    # print(f'Monkey_one has: {monkey_one} Round: {round}')
    # print(f'monkey_two has: {monkey_two} Round: {round}')
    # print(f'monkey_three has: {monkey_three} Round: {round}')

    
    
 


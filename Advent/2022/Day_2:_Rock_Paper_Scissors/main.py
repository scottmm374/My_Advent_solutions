

def main():
    
    play_rounds = list()
    with open("input.txt") as f:

        for lines in f.readlines():
            play_rounds.append(lines.strip())
            
        
    # print(play_rounds)

   

    my_score = 0
    # opponent_score = 0

    
    for play in play_rounds:
        # opp, me = play.split()
        opp, strat = play.split()
        
        # print(opp, strat)
        # print(f"Round: {play}, I play {strat}, score: {my_score}" )

        if strat == "Y":
            my_score += 3
        elif strat == "Z":
            my_score += 6   
        
    
        if opp == "A" and strat == "Y":
            my_score += 1
        elif opp == "B" and strat == "Y":
            my_score += 2
        elif opp == "C" and strat == "Y":
            my_score += 3
            

        elif opp == "A" and strat == "X":
            my_score += 3
        elif opp == "B" and strat == "X":
            my_score += 1
        elif opp == "C" and strat == "X":
            my_score += 2


        elif opp == "A" and strat == "Z":
            my_score += 2
        elif opp == "B" and strat == "Z":
            my_score += 3
        elif opp == "C" and strat == "Z":
            my_score += 1
        
       
        # Part 1
    
        # if me == "X":
        #     my_score += 1
        # elif me == "Y":
        #     my_score += 2   
        # else: 
        #     my_score += 3
    
        # if opp == "A" and me == "X":
        #     my_score += 3
        # elif opp == "B" and me == "Y":
        #     my_score += 3
        # elif opp == "C" and me == "Z":
        #     my_score += 3
            
        # elif me == "X" and opp == "C":
        #     my_score += 6
        # elif me == "Y" and opp == "A":
        #     my_score += 6
        # elif me == "Z" and opp == "B":
        #     my_score += 6
        
        # else:
        #     continue
        


    print(my_score)







if __name__ == "__main__":
    main()


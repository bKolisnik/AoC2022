def RockPaperScissors(input_lists):
    global_points = 0
    for list in input_lists:
        opponent = list[0]
        player = list[1]

        local_points = 0
        if player == 'X':
            local_points+=1
        elif player =='Y':
            local_points+=2
        elif player == 'Z':
            local_points+=3

        local_points += win_points(opponent,player)
        global_points+=local_points

    return global_points
    

def win_points(opponent,player):
    #9 possible outcomes
    #method is constant time space and O(1) time complexity

    result = {"A":{"X":"draw","Y":"win","Z":"loss"},
                "B":{"Y":"draw","Z":"win","X":"loss"},
                "C":{"Z":"draw","X":"win","Y":"loss"}}

    outcome = result[opponent][player]
    if outcome == "win":
        return 6
    elif outcome == "loss":
        return 0
    else:
        return 3


def RockPaperScissors2(input_lists):
    global_points = 0
    for list in input_lists:
        opponent = list[0]
        outcome = list[1]
        local_points = 0
        if outcome == "X":
            outcome = "loss"
        elif outcome == "Y":
            outcome = "draw"
            local_points+=3
        else:
            outcome = "win"
            local_points+=6

        player = get_move(opponent,outcome)

        if player == 'X':
            local_points+=1
        elif player =='Y':
            local_points+=2
        elif player == 'Z':
            local_points+=3

        global_points+=local_points

    return global_points
    

def get_move(opponent,outcome):
    result = {"A":{"draw":"X","win":"Y","loss":"Z"},
                "B":{"draw":"Y","win":"Z","loss":"X"},
                "C":{"draw":"Z","win":"X","loss":"Y"}}

    move_to_be_made = result[opponent][outcome]
    return move_to_be_made


if __name__ == "__main__":
    with open("input.txt") as file:
        lists = [line.rstrip().split(" ") for line in file]
        print(RockPaperScissors(lists))
        print(RockPaperScissors2(lists))
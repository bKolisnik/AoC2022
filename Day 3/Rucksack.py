def rucksack(sack_list):
    priority_sum = 0
    for sack in sack_list:
        #each sack length must be even in length so this cannot be fractional
        sack_len = len(sack)//2

        set1 = set()
        
        for i in range(0,sack_len):
            set1.add(sack[i])

        for i in range(sack_len,2*sack_len):
            if sack[i] in set1:
                char_in_both = sack[i]
                break
        
        priority = get_priority(char_in_both)
        priority_sum+=priority
        
    return priority_sum

def get_priority(char_in_both):
    if ord(char_in_both) > 95:
        priority = ord(char_in_both) - 96
    else:
        priority = ord(char_in_both) - 38
    return priority

def rucksack2(sack_list):
    priority_sum = 0
    #this time need to traverse 3 elf groups at a time.
    
    #the total number of 3 group sets is 
    num_groups = len(sack_list) //3

    for i in range(0,num_groups):
        group1 = sack_list[3*i]
        group2 = sack_list[3*i + 1]
        group3 = sack_list[3*i + 2]
        
        set1 = set()
        for char in group1:
            set1.add(char)
        set2 = set()
        for char in group2:
            if char in set1:
                set2.add(char)
        for char in group3:
            if char in set2:
                char_in_both = char
                break
        priority = get_priority(char_in_both)
        priority_sum+=priority
    return priority_sum


if __name__ == "__main__":
    with open("input.txt") as file:
        sacks = [line.rstrip() for line in file]
        print(rucksack(sacks))
        print(rucksack2(sacks))

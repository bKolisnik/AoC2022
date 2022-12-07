def tuning(line):

    for ptr2 in range(3,len(line)):
        local_set = set()
        for i in range(4):
            local_set.add(line[ptr2-i])
        if len(local_set) == 4:
            return ptr2+1
        
    
def tuning2(line):
    for ptr2 in range(13,len(line)):
        local_set = set()
        for i in range(14):
            local_set.add(line[ptr2-i])
        if len(local_set) == 14:
            return ptr2+1


if __name__ == "__main__":
    with open("input.txt") as file:
        line = [line.rstrip() for line in file][0]
        #line = "nppdvjthqldpwncqszvftbrmjlhg"
        print(tuning(line))
        print(tuning2(line))
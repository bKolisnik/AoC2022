def calorie_counting(input_list):
    #keep running track of max calroies seen thus far for each elf and compare with max
    max_cals= 0
    current_cals = 0
    for i in input_list:
        if i == '':
            max_cals = max(current_cals, max_cals)
            current_cals = 0
        else:
            current_cals+= int(i)

    return max_cals

def calorie_counting2(input_list):
    #Do not need to sort which is O(nlogn)
    #One pass is all it takes O(n)

    first = 0
    second = 0
    third = 0
    current_cals = 0
    for i in input_list:
        if (i ==''):
            if current_cals > first:
                third = second
                second = first
                first = current_cals
            elif current_cals > second:
                third = second
                second = current_cals
            elif current_cals > third:
                third = current_cals

            current_cals = 0

        else:
            current_cals += int(i)

    return first + second + third

if __name__ == "__main__":
    with open("input.txt") as file:
        lines = [line.rstrip() for line in file]
        lines.append('')
        print(calorie_counting(lines))
        print(calorie_counting2(lines))


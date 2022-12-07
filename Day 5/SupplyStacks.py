from collections import deque
def reverse_stack_list(stack_list):
    for i in range(len(stack_list)):
        stack_list[i].reverse()
    return stack_list

def supply_stacks(lines):

    crates_phase = True

    #if the second character is a number and not a letter or a space we are in the number section

    number_phase = False

    #get number of stacks from line 1, assuming there is at least one stack

    stacks = ((len(lines[0]) - 3) // 4)+1

    #create a list of stacks. Technically this deque 

    stack_list = []
    for i in range(stacks):
        stack_list.append(deque())

    current_stack = 0
    move_phase = False
    number_phase = False
    blank_phase = False
    for line in lines:
        if crates_phase:
            if line[1].isdigit():
                crates_phase = False
                #fix the stack list by reversing each stack. This is only done on the final iteration. It is time complexity O(N) for each stack.
                stack_list = reverse_stack_list(stack_list)
                number_phase = True
            else:
                next_is_letter= False

                for stack_ind in range(stacks):
                    letter_ind = stack_ind*4 + 1
                    letter = line[letter_ind]
                    if letter != " ":
                        stack_list[stack_ind].append(letter)


        if number_phase:
            number_phase = False
            blank_phase = True
            continue
        if blank_phase:
            blank_phase = False
            move_phase = True
            continue

        if move_phase:
            quantity = None
            source = None
            destination = None
            #jump 5 characters and while digit 
            digit = True
            start = 5
            i = 0
            number = []
            while digit:
                char = line[start+i]
                number.append(char)
                if not line[start+i+1].isdigit():
                    digit=False
                else:
                    i+=1
            quantity = int("".join(number))
            digit = True
            start = start+i+1+4+1+1
            i=0
            number = []
            while digit:
                char = line[start+i]
                number.append(char)
                if not line[start+i+1].isdigit():
                    digit=False
                else:
                    i+=1
            source = int("".join(number))
            digit = True
            start = start+i+1+4
            i=0
            number = []
            while digit and (start+i < len(line)):
                char = line[start+i]
                number.append(char)
                if start+i+1 < len(line):
                    if not line[start+i+1].isdigit():
                        digit=False
                    else:
                        i+=1
                else:
                    digit = False
            destination = int("".join(number))
            
            for i in range(quantity):
                element = stack_list[source-1].pop()
                stack_list[destination-1].append(element)


    #once you have gone through every line
    #get the element at the top of each stack
    message = []
    for i in range(len(stack_list)):
        char = stack_list[i][-1]
        message.append(char)

    return "".join(message)


def supply_stacks2(lines):
    crates_phase = True

    #if the second character is a number and not a letter or a space we are in the number section

    number_phase = False

    #get number of stacks from line 1, assuming there is at least one stack

    stacks = ((len(lines[0]) - 3) // 4)+1

    #create a list of stacks. Technically this deque 

    stack_list = []
    for i in range(stacks):
        stack_list.append(deque())

    current_stack = 0
    move_phase = False
    number_phase = False
    blank_phase = False
    for line in lines:
        if crates_phase:
            if line[1].isdigit():
                crates_phase = False
                #fix the stack list by reversing each stack. This is only done on the final iteration. It is time complexity O(N) for each stack.
                stack_list = reverse_stack_list(stack_list)
                number_phase = True
            else:
                next_is_letter= False

                for stack_ind in range(stacks):
                    letter_ind = stack_ind*4 + 1
                    letter = line[letter_ind]
                    if letter != " ":
                        stack_list[stack_ind].append(letter)


        if number_phase:
            number_phase = False
            blank_phase = True
            continue
        if blank_phase:
            blank_phase = False
            move_phase = True
            continue

        if move_phase:
            quantity = None
            source = None
            destination = None
            #jump 5 characters and while digit 
            digit = True
            start = 5
            i = 0
            number = []
            while digit:
                char = line[start+i]
                number.append(char)
                if not line[start+i+1].isdigit():
                    digit=False
                else:
                    i+=1
            quantity = int("".join(number))
            digit = True
            start = start+i+1+4+1+1
            i=0
            number = []
            while digit:
                char = line[start+i]
                number.append(char)
                if not line[start+i+1].isdigit():
                    digit=False
                else:
                    i+=1
            source = int("".join(number))
            digit = True
            start = start+i+1+4
            i=0
            number = []
            while digit and (start+i < len(line)):
                char = line[start+i]
                number.append(char)
                if start+i+1 < len(line):
                    if not line[start+i+1].isdigit():
                        digit=False
                    else:
                        i+=1
                else:
                    digit = False
            destination = int("".join(number))
            
            temp_stack = deque()
            for i in range(quantity):
                element = stack_list[source-1].pop()
                temp_stack.append(element)
            for i in range(quantity):
                element = temp_stack.pop()
                stack_list[destination-1].append(element)


    #once you have gone through every line
    #get the element at the top of each stack
    message = []
    for i in range(len(stack_list)):
        char = stack_list[i][-1]
        message.append(char)

    return "".join(message)


if __name__ == "__main__":
    with open("input.txt") as file:
        lines = [line.rstrip('\n') for line in file]

    print(supply_stacks(lines))
    print(supply_stacks2(lines))
    

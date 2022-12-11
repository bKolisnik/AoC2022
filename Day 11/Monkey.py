import os
from collections import deque, defaultdict
#hardcoding monkeys

class Monkey():
    def __init__(self,items, operation, test):
        self.items = items
        self.operation = operation
        self.test = test


def monkey_in_middle(monkeys,max_round = 20):

    round = 0
    monkey_business = defaultdict(int)
    while round < max_round:
        monkey_queue = deque(monkeys)
        monkey_index = 0
        while monkey_queue:
            monkey = monkey_queue.popleft()
            while monkey.items:
                old_worry = monkey.items.popleft()
                monkey_business[monkey_index] += 1
                new_worry = monkey.operation(old_worry)
                new_worry = new_worry // 3
                next_monkey_index = monkey.test(new_worry)
                monkeys[next_monkey_index].items.append(new_worry)

            monkey_index +=1
        round+=1

    #get two max item numbers counted
    max_count = 0
    second_max_count = 0
    for key in monkey_business:
        if monkey_business[key] > max_count:
            second_max_count = max_count
            max_count = monkey_business[key]
        elif monkey_business[key] > second_max_count:
            second_max_count = monkey_business[key]
    return max_count*second_max_count

def monkey_in_middle2(monkeys,max_round = 10000):

    round = 0
    monkey_business = defaultdict(int)
    while round < max_round:
        monkey_queue = deque(monkeys)
        monkey_index = 0
        while monkey_queue:
            monkey = monkey_queue.popleft()
            while monkey.items:
                old_worry = monkey.items.popleft()
                monkey_business[monkey_index] += 1
                new_worry = monkey.operation(old_worry)
                next_monkey_index = monkey.test(new_worry)
                monkeys[next_monkey_index].items.append(new_worry)

            monkey_index +=1
        round+=1

    #get two max item numbers counted
    max_count = 0
    second_max_count = 0
    for key in monkey_business:
        if monkey_business[key] > max_count:
            second_max_count = max_count
            max_count = monkey_business[key]
        elif monkey_business[key] > second_max_count:
            second_max_count = monkey_business[key]
    return max_count*second_max_count


def op0(worry):
    return worry*19

def test0(worry):
    if (worry % 23) == 0:
        return 2
    else:
        return 3

def op1(worry):
    return worry + 6

def test1(worry):
    if (worry % 19) == 0:
        return 2
    else:
        return 0

def op2(worry):
    return worry*worry

def test2(worry):
    if (worry % 13) == 0:
        return 1
    else:
        return 3

def op3(worry):
    return worry + 3

def test3(worry):
    if (worry % 17) == 0:
        return 0
    else:
        return 1


def oper0(worry):
    return worry*2

def tester0(worry):
    if (worry % 5) == 0:
        return 6
    else:
        return 1

def oper1(worry):
    return worry * 13

def tester1(worry):
    if (worry % 2) == 0:
        return 2
    else:
        return 6

def oper2(worry):
    return worry + 5

def tester2(worry):
    if (worry % 19) == 0:
        return 7
    else:
        return 5

def oper3(worry):
    return worry + 6

def tester3(worry):
    if (worry % 7) == 0:
        return 0
    else:
        return 4

def oper4(worry):
    return worry + 1

def tester4(worry):
    if (worry % 17) == 0:
        return 0
    else:
        return 1

def oper5(worry):
    return worry + 4

def tester5(worry):
    if (worry % 13) == 0:
        return 4
    else:
        return 3

def oper6(worry):
    return worry + 2

def tester6(worry):
    if (worry % 3) == 0:
        return 2
    else:
        return 7

def oper7(worry):
    return worry*worry

def tester7(worry):
    if (worry % 11) == 0:
        return 3
    else:
        return 5



if __name__ == "__main__":
    #TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), "input.txt")
    #m0 = Monkey(deque([79,98]),op0,test0)
    #m1 = Monkey(deque([54,65,75,74]),op1,test1)
    #m2 = Monkey(deque([79,60,97]),op2,test2)
    #m3 = Monkey(deque([74]),op3,test3)

    #monkeys_list = [m0,m1,m2,m3]

    m0 = Monkey(deque([98,89,52]),oper0,tester0)
    m1 = Monkey(deque([57, 95, 80, 92, 57, 78]),oper1,tester1)
    m2 = Monkey(deque([82, 74, 97, 75, 51, 92, 83]),oper2,tester2)
    m3 = Monkey(deque([97, 88, 51, 68, 76]),oper3,tester3)
    m4 = Monkey(deque([63]),oper4,tester4)
    m5 = Monkey(deque([94, 91, 51, 63]),oper5,tester5)
    m6 = Monkey(deque([61,54,94,71,74,68,98,83]),oper6,tester6)
    m7 = Monkey(deque([90, 56]),oper7,tester7)

    monkeys_list = [m0,m1,m2,m3, m4, m5, m6, m7]
    print(monkey_in_middle(monkeys_list))
    print(monkey_in_middle2(monkeys_list))


import ast
from functools import cmp_to_key
from collections import deque

def correct_order(pair):
    order_stack = deque()
    order_stack.append(pair)

    while order_stack:
        left, right = order_stack.pop()

        if type(left) == int and type(right) == int:
            if left != right:
                return left < right
        elif type(left) == list and type(right) == list:

            for i in range(max(len(left),len(right))-1,-1,-1):
                if i > len(left)-1:
                    order_stack.append([None,right[i]])
                elif i > len(right)-1:
                    order_stack.append([left[i],None])
                else:
                    order_stack.append([left[i],right[i]])

        elif type(left) == list and type(right) == int:
            order_stack.append([left, [right]])
        
        elif type(left) == int and type(right) == list:
            order_stack.append([[left],right])

        #at this point one of them must be none
        else:
            return left is None

    return True

def distress(pairs_of_lists):
    indices = []

    for index, pair in enumerate(pairs_of_lists):

        #if left list runs out of items first it is vali. If right list runs out of items first it is not valid.

        if correct_order(pair):
            indices.append(index+1)
    
    return sum(indices)


def cmp_pair(list1,list2):
    return -1 if correct_order([list1,list2]) else 1

def distress2(sequence):
    sorted_sequence = sorted(sequence,key=cmp_to_key(cmp_pair))
    index_2 = None
    index_6 = None
    for i in range(len(sorted_sequence)):
        if sorted_sequence[i] == [[2]]:
            index_2 = i
        elif sorted_sequence[i] == [[6]]:
            index_6 = i
    return (index_2+1)*(index_6+1)

if __name__ == "__main__":

    with open('input.txt') as file:
        pairs = [[eval(i) for i in pair.splitlines()] for pair in file.read().split('\n\n')]
        print(distress(pairs))

    with open('input.txt') as file:
        text = file.read()
        sequence = text.split('\n')
        sequence = [eval(seq) for seq in sequence if seq != '']
        sequence.append([[2]])
        sequence.append([[6]])
        print(distress2(sequence))
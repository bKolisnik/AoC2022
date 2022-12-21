def swap_neighbours(left,right,ll):
    #if we want the start and last nodes to be updated uncomment this but not necessary for this AoC problem.
    '''
    if ll.start_node == left:
        ll.start_node = right
    elif ll.start_node == right:
        ll.start_node = left
    if ll.last_node == left:
        ll.last_node = right
    elif ll.last_node == right:
        ll.last_node = left'''
    temp = left.left
    temp2 = right.right
    temp2.left = left
    temp.right = right
    left.right = right.right
    left.left = right
    right.right = left
    right.left = temp
class CircularNode:
    def __init__(self,data):
        self.item = data
        self.left = None
        self.right = None

    def rotate_right(self,count,ll):
        if count < 1:
            return
        for _ in range(count):
            swap_neighbours(self,self.right,ll)

    def rotate_left(self,count,ll):
        if count < 1:
            return
        for _ in range(count):
            swap_neighbours(self.left,self,ll)

class CircularLinkedList:
    def __init__(self):
        self.start_node = None
        self.last_node = None
        self.length = 0

    def insert_to_end(self,data):
        self.length+=1
        if self.start_node is None:
            new_node = CircularNode(data)
            new_node.left = new_node
            new_node.right = new_node
            self.start_node = new_node
            self.last_node = new_node
        else:
            new_node = CircularNode(data)
            self.last_node.right = new_node
            new_node.left = self.last_node
            new_node.right = self.start_node
            self.last_node = new_node
            self.start_node.left = new_node

def print_list(ll):
    results = []
    node = ll.start_node
    results.append(node.item)
    node=node.right
    for _ in range(ll.length-1):
        results.append(node.item)
        node=node.right
    return results

def part1(values):
    list_nodes = []
    ll = CircularLinkedList()
    for i in range(len(values)):
        ll.insert_to_end(values[i])
        list_nodes.append(ll.last_node)
    
    zero = None
    for node in list_nodes:
        if node.item > 0:
            node.rotate_right(node.item,ll)
        elif node.item < 0:
            node.rotate_left(-1*node.item,ll)
        else:
            zero = node
    
    node = zero
    result = 0
    moves_right = 1000 % ll.length
    for _ in range(3):
        for _ in range(moves_right):
            node= node.right
        result+=node.item
    return result

def part2(values):
    decryption = 811589153

    list_nodes = []
    ll = CircularLinkedList()
    for i in range(len(values)):
        ll.insert_to_end(decryption*values[i])
        list_nodes.append(ll.last_node)
    
    zero = None
    for _ in range(10): #Need to do 10 rounds of mixing first.
        for node in list_nodes:
            if node.item > 0:
                node.rotate_right((node.item) % (ll.length-1),ll) #this is % (linkedlist length - 1) because there are length - 1 swaps until you are back to the original list order.
            elif node.item < 0:
                node.rotate_left((-1*node.item) % (ll.length-1),ll)
            else:
                zero = node
        #values = print_list(ll)

    node = zero
    result = 0
    moves_right = 1000 % ll.length
    for _ in range(3):
        for _ in range(moves_right):
            node= node.right
        result+=node.item
    return result

if __name__ == "__main__":
    with open('input.txt') as file:

        values = [int(val) for val in file.read().split('\n') if val != '']
        print(part1(values))
        print(part2(values))

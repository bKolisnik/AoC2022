import os

from queue import PriorityQueue
from collections import deque
import copy

def get_neighbours(grid,node):
    #node is a tuple
    neighbours = []

    x = node[0]
    y = node[1]
    max_y, max_x = len(grid),len(grid[0])
    no_left = False
    no_right = False
    no_up = False
    no_down = False
    if x == 0:
        no_left = True
    elif x == max_x-1:
        no_right = True
    if y == 0:
        no_up = True
    elif y == max_y-1:
        no_down = True
    
    if not no_left and (ord(grid[y][x-1]) <= ord(grid[y][x])+1):
        neighbours.append((x-1,y))
    
    if not no_right and (ord(grid[y][x+1]) <= ord(grid[y][x])+1):
        neighbours.append((x+1,y))

    if not no_up and (ord(grid[y-1][x]) <= ord(grid[y][x])+1):
        neighbours.append((x,y-1))
    
    if not no_down and (ord(grid[y+1][x]) <= ord(grid[y][x])+1):
        neighbours.append((x,y+1))

    return neighbours

def get_neighbours_reverse(grid,node):
    #node is a tuple
    neighbours = []

    x = node[0]
    y = node[1]
    max_y, max_x = len(grid),len(grid[0])
    no_left = False
    no_right = False
    no_up = False
    no_down = False
    if x == 0:
        no_left = True
    elif x == max_x-1:
        no_right = True
    if y == 0:
        no_up = True
    elif y == max_y-1:
        no_down = True
    
    if not no_left and (ord(grid[y][x-1])+1 >= ord(grid[y][x])):
        neighbours.append((x-1,y))
    
    if not no_right and (ord(grid[y][x+1])+1 >= ord(grid[y][x])):
        neighbours.append((x+1,y))

    if not no_up and (ord(grid[y-1][x])+1 >= ord(grid[y][x])):
        neighbours.append((x,y-1))
    
    if not no_down and (ord(grid[y+1][x])+1 >= ord(grid[y][x])):
        neighbours.append((x,y+1))

    return neighbours


def djikstra(grid,source,target):
    '''return shortest num_steps for the shortest path'''
    distance = [[float('inf') for j in range(len(grid[0]))] for i in range(len(grid))]
    #distances will alwasy be one in this problem.
    prev = [[None for j in range(len(grid[0]))] for i in range(len(grid))]

    distance[source[1]][source[0]] = 0

    pq = PriorityQueue()

    seen = set()

    '''
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            pq.put((distance[i][j],(j,i)))'''
    #only need to add all of the nodes to the pq if we want the entire spanning tree.
    pq.put((distance[source[1]][source[0]],(source[0],source[1])))

    while not pq.empty():
        (_, u) = pq.get()

        if u in seen:
            continue

        else:
            seen.add(u)

        if u[0] == target[0] and u[1] == target[1]:
            break

        #for each neightbour of u still in pq (hasnt been visited yet)
        neighbours = get_neighbours(grid,u)

        for v in neighbours:
            if not (v in seen):
                proposed_dist = distance[u[1]][u[0]] + 1
                if proposed_dist < distance[v[1]][v[0]]:
                    distance[v[1]][v[0]] = proposed_dist
                    prev[v[1]][v[0]] = (u[0],u[1])
                    pq.put((distance[v[1]][v[0]],v))

    '''
    s = deque() #at this point u is still the target
    if prev[u[1]][u[0]]: 
        while u:
            s.append(u)
            u = prev[u[1]][u[0]]
    '''
    return distance[u[1]][u[0]] # length including source and target

def djikstra2(grid,source):
    '''return shortest num_steps for the shortest path'''
    distance = [[float('inf') for j in range(len(grid[0]))] for i in range(len(grid))]
    #distances will alwasy be one in this problem.
    prev = [[None for j in range(len(grid[0]))] for i in range(len(grid))]

    distance[source[1]][source[0]] = 0

    pq = PriorityQueue()

    seen = set()

    '''
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            pq.put((distance[i][j],(j,i)))'''

    pq.put((distance[source[1]][source[0]],(source[0],source[1])))
    
    i = 0
    while not pq.empty():
        (_, u) = pq.get()
        i+=1
            
        if u in seen:
            continue
        
        seen.add(u)

        #for each neightbour of u still in pq (hasnt been visited yet)
        neighbours = get_neighbours_reverse(grid,u)

        for v in neighbours:
            if v in seen:
                continue
            proposed_dist = distance[u[1]][u[0]] + 1
            if proposed_dist < distance[v[1]][v[0]]:
                distance[v[1]][v[0]] = proposed_dist
                prev[v[1]][v[0]] = (u[0],u[1])
                pq.put((distance[v[1]][v[0]],v))


    return distance

def all_starting_locations(grid):
    starts = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "S":
                grid[i][j] = 'a'
                starts.append((j, i))
            elif grid[i][j] == 'a':
                starts.append((j, i))

    return starts

def locate_start(grid):

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "S":
                grid[i][j] = 'a'
                return (j, i)
    return (None, None)

def locate_end(grid):

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "E":
                grid[i][j] = 'z'
                return (j, i)
    return (None, None)

def hill_climbing(grid):
    #current position is S
    #target position is E

    start_x, start_y = locate_start(grid)
    end_x, end_y = locate_end(grid)
    #previous two ops done in O(M*N)

    #reach E in as few steps as possible, can move one square up, down, left, right. 
    # Elevation of destination square can be at most one higher than current square.
    #Elevation of destination square can lower than curretn square.

    #djikstras algorithm on a grid
    min_length = djikstra(grid,(start_x,start_y),(end_x,end_y))

    return min_length


def hill_climbing2(grid):
    #So, you'll need to find the shortest path from any square at elevation a to the square marked E.
    starts = all_starting_locations(grid)
    end_x, end_y = locate_end(grid)
    #previous two ops done in O(M*N)

    #reach E in as few steps as possible, can move one square up, down, left, right. 
    # Elevation of destination square can be at most one higher than current square.
    #Elevation of destination square can lower than curretn square.

    #djikstras algorithm on a grid
    min_length = float('inf')
    distance = djikstra2(grid,(end_x,end_y))
    for start in starts:

        min_length = min(min_length,distance[start[1]][start[0]])

    return min_length

if __name__ == "__main__":
    TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), "input.txt")
    with open(TESTDATA_FILENAME) as file:
        grid = [list(line.rstrip()) for line in file]

    grid2 = copy.deepcopy(grid)
    print(hill_climbing(grid))
    print(hill_climbing2(grid2))
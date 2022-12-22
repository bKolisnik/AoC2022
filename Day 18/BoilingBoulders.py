from collections import deque

def get_neighbours(rock,graph):

    #do a check in each of 6 directions for rock
    neighbours = []

    possible_vals = (-1,1)
    positions = (0,1,2)
    candidates = []
    for val in possible_vals:
        for position in positions:
            candidate = [rock[0],rock[1],rock[2]]
            candidate[position] += val
            candidates.append(tuple(candidate))

    for candidate in candidates:
        if candidate in graph:
            neighbours.append(candidate)

    return neighbours

def part1(coords):
    #coords will be a list of tuples
    #part1 is counting neighbours for each cube which are not rocks. 
    #I will do this using BFS
    graph = set(coords)

    queue = deque()
    for coord in graph:
        queue.append(coord)
    seen = set()
    surface_area = 0
    while queue:
        rock = queue.popleft()
        if rock not in seen:
            seen.add(rock)

            #get neighbours and add to queue
            neighbours = get_neighbours(rock,graph)
            surface_area += 6 - len(neighbours)
            for neighbour in neighbours:
                if neighbour in seen:
                    continue
                queue.append(neighbour)
                #seen.add(neighbour)

    return surface_area
    
def get_neighbours_air(air,graph,mins,maxs):

    #do a check in each of 6 directions for rock
    neighbours = []

    possible_vals = (-1,1)
    positions = (0,1,2)
    candidates = []
    for val in possible_vals:
        for position in positions:
            candidate = [air[0],air[1],air[2]]
            candidate[position] += val
            if candidate[0] < mins[0] or candidate[0] > maxs[0] + 2:
                continue
            elif candidate[1] < mins[1] or candidate[1] > maxs[1] + 2:
                continue
            elif candidate[2] < mins[2] or candidate[2] > maxs[2] + 2:
                continue
            candidates.append(tuple(candidate))
    rocks=0
    for candidate in candidates:
        if candidate in graph:
            rocks+=1
        else:
            neighbours.append(candidate)

    return neighbours, rocks

def part2(coords):
    #flood fill starting from air outside the rocks

    min_x, min_y, min_z = -1,-1,-1
    max_x = -1
    max_y = -1
    max_z = -1

    for coord in coords:
        if coord[0] > max_x:
            max_x = coord[0]
        if coord[1] > max_y:
            max_y = coord[1]
        if coord[2] > max_z:
            max_z = coord[2]
    
    mins = (min_x,min_y,min_z)
    maxs = (max_x,max_y,max_z)

    graph = set(coords)
    queue = deque()
    queue.append((-1,-1,-1))

    seen = set()
    rock_faces = 0
    while queue:

        air = queue.popleft()
        neighbours, rocks = get_neighbours_air(air,graph,mins,maxs)
        rock_faces += rocks
        for neighbour in neighbours:
            if neighbour in seen:
                continue
            queue.append(neighbour)
            seen.add(neighbour)
    return rock_faces

if __name__ == "__main__":
    with open('input.txt') as file:
        values = []
        for line in file.read().split('\n'):
            if line != '':
                coords = line.split(',')
                values.append(tuple([int(coord) for coord in coords]))


    print(part1(values)) #part1 surface area included both interior and exterior surface area
    print(part2(values)) #part2 is only exterior surface area


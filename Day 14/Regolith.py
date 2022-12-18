import math
from collections import defaultdict

class Sand:

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.rest = False
    def move(self,grid):
        if self.y+1 > len(grid)-1:
            return True
        if grid[self.y+1][self.x] == 0:
            grid[self.y][self.x] = 0
            grid[self.y+1][self.x] = 1
            self.y = self.y +1
            return False
        if self.x-1 < 0:
            return True
        if grid[self.y+1][self.x-1] == 0:
            grid[self.y][self.x] = 0
            grid[self.y+1][self.x-1] = 1
            self.x = self.x-1
            self.y = self.y +1
            return False
        if self.x+1 > len(grid[0]) -1:
            return True
        if grid[self.y+1][self.x+1] == 0:
            grid[self.y][self.x] = 0
            grid[self.y+1][self.x+1] = 1
            self.x = self.x+1
            self.y = self.y +1
            return False
        else:
            self.rest = True
            return False

class SandPart2:
    def __init__(self,x,y,max_y):
        self.x = x
        self.y = y
        self.rest = False
        self.max_y = max_y
    def move(self,grid):

        if grid[(self.y+1,self.x)] == 0:
            grid[(self.y,self.x)] = 0
            grid[(self.y+1,self.x)] = 1
            self.y = self.y +1
            if self.y == self.max_y-1:
                self.rest = True

        elif grid[(self.y+1,self.x-1)] == 0:
            grid[(self.y,self.x)] = 0
            grid[(self.y+1,self.x-1)] = 1
            self.x = self.x-1
            self.y = self.y +1
            if self.y == self.max_y-1:
                self.rest = True

        elif grid[(self.y+1,self.x+1)] == 0:
            grid[(self.y,self.x)] = 0
            grid[(self.y+1,self.x+1)] = 1
            self.x = self.x+1
            self.y = self.y +1
            if self.y == self.max_y-1:
                self.rest = True

        else:
            self.rest = True

def get_direction_change(last_rock_x,last_rock_y,rock_x,rock_y):
    change_x = rock_x - last_rock_x
    change_y = rock_y - last_rock_y
    return (change_x,change_y)

def create_rock_grid(segments):
    min_x = float('inf')
    max_x = 0
    max_y = 0

    for segment in segments:
        for rock in segment:
            if int(rock[0]) > max_x:
                max_x = int(rock[0])
            if int(rock[0]) < min_x:
                min_x = int(rock[0])
            if int(rock[1]) > max_y:
                max_y = int(rock[1])

    grid = [[0 for j in range(max_x-min_x+1)] for i in range(max_y+1)]

    for segment in segments:
        last_rock = segment[0]
        last_rock_x = int(last_rock[0]) - min_x
        last_rock_y = int(last_rock[1])
        grid[last_rock_y][last_rock_x] = 1

        for i in range(1, len(segment)):
            rock = segment[i]
            rock_x = int(rock[0]) - min_x
            rock_y = int(rock[1])
            change_x, change_y = get_direction_change(last_rock_x,last_rock_y, rock_x,rock_y)
        
            if change_x != 0:
                if change_x > 0:
                    for i in range(1,change_x+1):
                        grid[last_rock_y][last_rock_x+i] = 1
                else:
                    for i in range(change_x,0):
                        grid[last_rock_y][last_rock_x+i] = 1
            else:
                if change_y > 0:
                    for i in range(1,change_y+1):
                        grid[last_rock_y+i][last_rock_x] = 1
                else:
                    for i in range(change_y,0):
                        grid[last_rock_y+i][last_rock_x] = 1

            last_rock = rock
            last_rock_x = int(last_rock[0]) - min_x
            last_rock_y = int(last_rock[1])
    
    return grid, min_x


def create_rock_grid2(segments):

    max_y = 0

    for segment in segments:
        for rock in segment:
            if int(rock[1]) > max_y:
                max_y = int(rock[1])

    grid = defaultdict(int)

    for segment in segments:
        last_rock = segment[0]
        last_rock_x = int(last_rock[0])
        last_rock_y = int(last_rock[1])
        grid[(last_rock_y,last_rock_x)] = 1

        for i in range(1, len(segment)):
            rock = segment[i]
            rock_x = int(rock[0])
            rock_y = int(rock[1])
            change_x, change_y = get_direction_change(last_rock_x,last_rock_y, rock_x,rock_y)
        
            if change_x != 0:
                if change_x > 0:
                    for i in range(1,change_x+1):
                        grid[(last_rock_y,last_rock_x+i)] = 1
                else:
                    for i in range(change_x,0):
                        grid[(last_rock_y,last_rock_x+i)] = 1
            else:
                if change_y > 0:
                    for i in range(1,change_y+1):
                        grid[(last_rock_y+i,last_rock_x)] = 1
                else:
                    for i in range(change_y,0):
                        grid[(last_rock_y+i,last_rock_x)] = 1

            last_rock = rock
            last_rock_x = int(last_rock[0])
            last_rock_y = int(last_rock[1])
    
    return grid, max_y

def sand_rest(grid,min_x):
    sand_origin_x = 500 - min_x
    sand_origin_y = 0
    sand_count = 0
    fallen_off = False
    while not fallen_off:
        sand_rest = False
        s = Sand(sand_origin_x,sand_origin_y)
        grid[sand_origin_y][sand_origin_x]=1
        sand_count+=1
        while (not sand_rest) and (not fallen_off):
            fallen_off = s.move(grid)
            sand_rest = s.rest
    return sand_count-1

def sand_rest2(grid,max_y):
    sand_origin_x = 500
    sand_origin_y = 0
    sand_count = 0
    full = False
    while not full:
        sand_rest = False
        s = SandPart2(sand_origin_x,sand_origin_y,max_y)
        grid[(sand_origin_y,sand_origin_x)]=1
        sand_count+=1
        while (not sand_rest):
            s.move(grid)
            sand_rest = s.rest
        if grid[(sand_origin_y,sand_origin_x)] == 1:
            full = True
    return sand_count

if __name__ == "__main__":
    with open('input.txt') as file:

        segments = [segment.split(' -> ') for segment in file.read().split('\n')]

        points = [None]*len(segments)
        for i,segment in enumerate(segments):
            for pair in segment:
                if points[i] is None:
                    points[i] = [pair.split(',')]
                else:
                    points[i].append(pair.split(','))

        grid, min_x = create_rock_grid(points)
        grid2,max_y = create_rock_grid2(points)
        print(sand_rest(grid,min_x))
        print(sand_rest2(grid2,max_y+2))


        
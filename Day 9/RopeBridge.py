import os
from collections import defaultdict

def squared_magnitude(vec):
    return (vec[0]*vec[0]) + (vec[1]*vec[1])

class RopeEnd:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def move(self, delta_x, delta_y):
        self.x += delta_x
        self.y += delta_y

class Tail(RopeEnd):

    def __init__(self, x, y, head):
        self.head = head
        self.visited = defaultdict(int)
        self.visited[(x,y)] = 1
        super().__init__(x,y)

    def move_head(self, delta_x, delta_y):
        self.head.move(delta_x, delta_y)

    def squared_magnitude(self):
        return ((self.head.x - self.x)*(self.head.x - self.x)) + ((self.head.y - self.y)*(self.head.x - self.x))

    def calculate_displacement_to_head(self):
        return (self.head.x-self.x,self.head.y-self.y)

    def follow(self):
        displacement = self.calculate_displacement_to_head()
        #if the sqaured distance is greater than 2 we need to follow the head
        if squared_magnitude(displacement) > 2:
            #if the head and tail aren't touching and aren't in the same row or column, the tail always moves one step diagonally to keep up

            #lower the displacment directions that are greater than 1 to 1 in magnitude.

            if displacement[0] > 1:
                new_displacement_x = 1
            elif displacement[0] < -1:
                new_displacement_x = -1
            else:
                new_displacement_x = displacement[0]

            if displacement[1] > 1:
                new_displacement_y = 1
            elif displacement[1] < -1:
                new_displacement_y = -1
            else:
                new_displacement_y = displacement[1]

            self.move(new_displacement_x,new_displacement_y)
            self.visited[(self.x,self.y)]+=1


def ropebridge(moves):
    head = RopeEnd(0,0)
    tail = Tail(0,0,head)

    for direction, move in moves:
        move = int(move)
        while(move > 0):
            if direction == "U":
                delta_y = 1
                delta_x = 0
            elif direction == "D":
                delta_y = -1
                delta_x = 0
            elif direction == "L":
                delta_y = 0
                delta_x = -1
            elif direction == "R":
                delta_y = 0
                delta_x = 1
            tail.move_head(delta_x,delta_y)
            tail.follow()
            move-=1

    unique_vists = 0
    for key in tail.visited:
        unique_vists+=1
    return unique_vists


def ropebridge2(moves):
    head = RopeEnd(0,0)
    last_head = head
    tails = []
    for i in range(9):
        last_head = Tail(0,0,last_head)
        tails.append(last_head)

    for direction, move in moves:
        move = int(move)
        while(move > 0):
            if direction == "U":
                delta_y = 1
                delta_x = 0
            elif direction == "D":
                delta_y = -1
                delta_x = 0
            elif direction == "L":
                delta_y = 0
                delta_x = -1
            elif direction == "R":
                delta_y = 0
                delta_x = 1
            
            tails[0].move_head(delta_x,delta_y)
            for i in range(len(tails)):
                tails[i].follow()
            move-=1

    unique_vists = 0
    for key in tails[len(tails)-1].visited:
        unique_vists+=1
    return unique_vists

if __name__ == "__main__":
    TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), "input.txt")
    with open(TESTDATA_FILENAME) as file:
        moves = [line.rstrip().split(' ',1) for line in file]
        print(ropebridge(moves))
        print(ropebridge2(moves)) #2447 was too high
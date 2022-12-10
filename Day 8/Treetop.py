import os
from copy import deepcopy
def count_visible(grid):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]:
                count+=1
    return count

def combine_grids(tl_visible,br_visible):
    visible = [[False for x in range(len(tl_visible[0]))] for y in range(len(tl_visible))]
    for i in range(len(tl_visible)):
        for j in range(len(tl_visible[0])):
            if tl_visible[i][j] or br_visible[i][j]:
                visible[i][j] = True
    return visible

def count_visible_trees(tl_visible,br_visible):
    visible = combine_grids(tl_visible,br_visible)

    return count_visible(visible)


def set_boundaries_visible(visible):
    #edge trees are always visible
    for j in range(len(visible[0])):
        visible[0][j] = True
        visible[len(visible)-1][j] = True

    for i in range(len(visible)):
        visible[i][0] = True
        visible[i][len(visible[0])-1] = True
    return visible

def set_tl_visible(grid, visible):
    visible = set_boundaries_visible(visible)

    max_seen_left = [grid[i][0] for i in range(len(grid))]
    max_seen_top = deepcopy(grid[0])

    #dp to build up the top left table
    for i in range(1,len(visible)-1):
        for j in range(1,len(visible[i])-1):
            if grid[i][j] > max_seen_left[i]:
                visible[i][j] = True
                max_seen_left[i] = grid[i][j]

            if grid[i][j] > max_seen_top[j]:
                visible[i][j] = True
                max_seen_top[j] = grid[i][j]
    return visible

def set_br_visible(grid, visible):
    visible = set_boundaries_visible(visible)

    max_seen_right = [grid[i][len(grid[0])-1] for i in range(len(grid))]
    max_seen_bottom = deepcopy(grid[len(grid)-1])

    #dp to build up the bottom right table
    for i in range(len(visible)-2,0,-1):
        for j in range(len(visible[i])-2,0,-1):
            if grid[i][j] > max_seen_right[i]:
                visible[i][j] = True
                max_seen_right[i] = grid[i][j]

            if grid[i][j] > max_seen_bottom[j]:
                visible[i][j] = True
                max_seen_bottom[j] = grid[i][j]
    return visible

def treetop(grid):
    #tree is visible if all of the trees between the tree in question and an edge of the tree are shorter than it.
    #how many trees are visible from outside the grid

    #can we do this in one pass so O(M*N) time complexity? Yes!

    import copy

    #we will create two visible grids
    tl_visible = [[False for x in range(len(grid[0]))] for y in range(len(grid))]
    br_visible = [[False for x in range(len(grid[0]))] for y in range(len(grid))]
    tl_visible = set_tl_visible(grid, tl_visible)
    br_visible = set_br_visible(grid, br_visible)

    #once we have the two grids check each position and see if any are visible if they are add to count
    return count_visible_trees(tl_visible,br_visible)


def get_scenic_scores(grid):
    #dp for each direction in O(M*N)




    top = deepcopy(grid)
    for j in range(len(grid[0])):
        top[0][j] = 0

    for i in range(1,len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] > grid[i-1][j]:
                top[i][j] = 1 + top[i-1][j]
            else:
                top[i][j] = 1

    bottom = deepcopy(grid)
    for j in range(len(grid[0])):
        bottom[len(grid)-1][j] = 0

    for i in range(len(grid)-2,-1,-1):
        for j in range(len(grid[0])):
            if grid[i][j] > grid[i+1][j]:
                bottom[i][j] = 1 + bottom[i+1][j]
            else:
                bottom[i][j] = 1

    left = deepcopy(grid)
    for i in range(len(grid)):
        left[i][0] = 0

    for i in range(len(grid)):
        for j in range(1,len(grid[0])):
            if grid[i][j] > grid[i][j-1]:
                left[i][j] = 1 + left[i][j-1]
            else:
                left[i][j] = 1

    right = deepcopy(grid)
    for i in range(len(grid)):
        right[i][len(grid[0])-1] = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])-2,-1,-1):
            if grid[i][j] > grid[i][j+1]:
                right[i][j] = 1 + right[i][j+1]
            else:
                right[i][j] = 1

    return left, top, right, bottom


def left_scenic_score(grid,i,j):
    if j == 0:
        return 0
    else:
        left = j -1
        scenic = 1
        while left > 0 and grid[i][left] < grid[i][j]:
            scenic+=1
            left-=1

        return scenic

def right_scenic_score(grid,i,j):
    if j == len(grid[0])-1:
        return 0
    else:
        right = j +1
        scenic = 1
        while right < len(grid[0])-1 and grid[i][right] < grid[i][j]:
            scenic+=1
            right+=1

        return scenic

def top_scenic_score(grid,i,j):
    if i == 0:
        return 0
    else:
        top = i -1
        scenic = 1
        while top > 0 and grid[top][j] < grid[i][j]:
            scenic+=1
            top-=1

        return scenic

def bottom_scenic_score(grid,i,j):
    if i == len(grid)-1:
        return 0
    else:
        bottom = i +1
        scenic = 1
        while bottom < len(grid)-1 and grid[bottom][j] < grid[i][j]:
            scenic+=1
            bottom+=1

        return scenic

def max_scenic_score(grid):
    max_scenic_score = -1
    for i in range(len(grid)):
        for j in range(len(grid[0])):

            left_scenic = left_scenic_score(grid,i,j)
            right_scenic = right_scenic_score(grid,i,j)
            top_scenic = top_scenic_score(grid,i,j)
            bottom_scenic = bottom_scenic_score(grid,i,j)

            scenic_score = left_scenic*right_scenic*top_scenic*bottom_scenic
            max_scenic_score = max(max_scenic_score,scenic_score)

    return max_scenic_score



    left, top, right, bottom = get_scenic_scores(grid)

    #final_scenic_scores = [[None for x in range(len(grid[0]))] for y in range(len(grid))]

    max_scenic_score = -1
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            scenic_score = left[i][j]*top[i][j]*right[i][j]*bottom[i][j]
            max_scenic_score = max(max_scenic_score,scenic_score)

    return max_scenic_score
    

def treetop2(grid):

    return max_scenic_score(grid)


'''
30373
25512
65332
33549
35390
unfortunately the 3 2 2 9 0 rightmost column is why we cannot use dynamic programming.
The top right 3 must be able to see 3 down. No way to keep track of this recursively. Just have to search.

bottom = deepcopy(grid)
for j in range(len(grid[0])):
    bottom[len(grid)-1][j] = 0

for i in range(len(grid)-2,-1,-1):
    for j in range(len(grid[0])):
        if grid[i][j] > grid[i+1][j]:
            bottom[i][j] = 1 + bottom[i+1][j]
        else:
            bottom[i][j] = 1

there was an example attempt for dp in each direction but it does not work. check out the example for the downards looking dp which begins with the bottom row and moves up.


'''


if __name__ == "__main__":
    TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), "input.txt")
    with open(TESTDATA_FILENAME) as file:
        grid = [list(line.rstrip()) for line in file]
    for i in range(len(grid)):
        for j in range(len(grid)):
            grid[i][j] = int(grid[i][j])
    print(treetop(grid))
    print(treetop2(grid))
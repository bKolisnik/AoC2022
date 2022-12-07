from collections import deque

class Folder:

    def __init__(self):
        self.children = dict()
        self.total_size = 0
        self.child_file_size = 0

def postorder_get_folder_sizes(root,max_folder_size=float('inf')):
    #as you come up the dfs set the folder sizes, keep track of folders
    
    #get the total sum of all of the folder sizes that are at most max_folder_size
    if root is None:
        return 0
    
    input_stack = deque() # this stack will be used to traverse the tree
    output_stack = deque() # this stack will store the output
    input_stack.append(root)
    while input_stack:

        curr = input_stack.pop()
        output_stack.append(curr)

        for child in curr.children:
            input_stack.append(curr.children[child])

    total_folder_sizes = 0
    while output_stack:

        node = output_stack.pop()

        if len(node.children) == 0:
            node.total_size = node.child_file_size
            total = node.total_size
            if total <= max_folder_size:
                total_folder_sizes+=total

        else:
            total = 0
            node.total_size = node.child_file_size
            total+=node.total_size
            for child in node.children:
                node.total_size += node.children[child].total_size
                total+=node.children[child].total_size
            if total <= max_folder_size:
                total_folder_sizes+=total

    return total_folder_sizes

def postorder_delete_smallest_to_make_space(root):
    #as you come up the dfs set the folder sizes, keep track of folders
    
    #get the total sum of all of the folder sizes that are at most max_folder_size
    if root is None:
        return 0
    
    input_stack = deque() # this stack will be used to traverse the tree
    output_stack = deque() # this stack will store the output
    input_stack.append(root)
    while input_stack:

        curr = input_stack.pop()
        output_stack.append(curr)

        for child in curr.children:
            input_stack.append(curr.children[child])


    min_disk_space = 30000000
    total_disk_space = 70000000
    min_folder_size_large_enough = float('inf')

    #need total used space and then
    results_stack = deque()
    while output_stack:

        node = output_stack.pop()

        if len(node.children) == 0:
            node.total_size = node.child_file_size
            results_stack.append(node.total_size)
            

        else:
            node.total_size = node.child_file_size

            for child in node.children:
                node.total_size += node.children[child].total_size
            
            results_stack.append(node.total_size)
            

    used_space = results_stack[-1]
    freespace = total_disk_space - used_space
    while results_stack:
        folder_size = results_stack.popleft()
        if freespace + folder_size >= min_disk_space:
            min_folder_size_large_enough = min(min_folder_size_large_enough, folder_size)


    return min_folder_size_large_enough


def no_space(lines):
    #do a bfs on the tree
    #first construct the tree
    f = None

    root = None
    visited = deque()
    for line in lines:
        if line[0:4] == "$ cd":

            dir_name = line.split(" ", 2)[-1]
            if dir_name == "/":
                f = Folder()
                root = f
                visited.append(f)
            elif dir_name == ".." and len(visited) > 1:
                visited.pop()
                f = visited[-1]
            elif dir_name == ".." and len(visited) == 1:
                f = visited[-1]
            elif dir_name != "..":
                f = f.children[dir_name]
                visited.append(f)


        elif line[0].isdigit():
            file_size = int(line.split(" ", 1)[0])
            f.child_file_size += file_size

        elif line[0:3] == "dir":
            child_dir = line.split(" ", 1)[1]
            f.children[child_dir] = Folder()


    #now we have a tree starting from root we need to construct the file sizes
    return postorder_get_folder_sizes(root,max_folder_size=100000)


def no_space2(lines):
    f = None

    root = None
    visited = deque()
    for line in lines:
        if line[0:4] == "$ cd":

            dir_name = line.split(" ", 2)[-1]
            if dir_name == "/":
                f = Folder()
                root = f
                visited.append(f)
            elif dir_name == ".." and len(visited) > 1:
                visited.pop()
                f = visited[-1]
            elif dir_name == ".." and len(visited) == 1:
                f = visited[-1]
            elif dir_name != "..":
                f = f.children[dir_name]
                visited.append(f)


        elif line[0].isdigit():
            file_size = int(line.split(" ", 1)[0])
            f.child_file_size += file_size

        elif line[0:3] == "dir":
            child_dir = line.split(" ", 1)[1]
            f.children[child_dir] = Folder()

    return postorder_delete_smallest_to_make_space(root)
    

if __name__ == "__main__":
    with open("input.txt") as file:
        #this is a dfs or bfs on a tree (not necessarily binary tree)
        line = [line.rstrip() for line in file]
        #line = "nppdvjthqldpwncqszvftbrmjlhg"
        print(no_space(line))
        print(no_space2(line))
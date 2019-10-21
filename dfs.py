from collections import deque
import constants

def dfs(start, goal):
    visited = []
    path = []
    fringe = deque()
    fringe.append([0, start, path, visited])

    while fringe:
        current = fringe.pop()
        depth = current[0]
        current_node = current[1]
        path = current[2]
        visited = current[3]

        if current_node == goal:
            return path + [current_node]

        visited = visited + [current_node]

        child_nodes = getNeighbors(current_node)
        for node in child_nodes:
            if node not in visited:
                if node == goal:
                    return path + [node]
                depth_of_node = len(path)
                fringe.append([-depth_of_node, node, path + [node], visited])

    return path

def getNeighbors(current):
    neighbors = []
    x = current[0]
    y = current[1]
    x_add = x + 1
    x_sub = x - 1
    y_add = y + 1
    y_sub = y - 1

    if x_sub > 0:
        neighbors.append([x_sub, y])
    
    if y_sub > 0:
        neighbors.append([x, y_sub])

    if x_add <= 5:
        neighbors.append([x_add, y])
    
    if y_add <= 5:
        neighbors.append([x, y_add])
    
    return neighbors

if __name__ == "__main__":

    path = dfs([1,1], [constants.win_strength, constants.win_intellect])
    print("path", path) # ==> [(1,2), (2,2), (2,3)]
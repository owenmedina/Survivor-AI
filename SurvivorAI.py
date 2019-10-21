from collections import deque
import constants

def dfs(start, goal):
    visited = [start]
    path = [start]
    fringe = deque()
    fringe.append([0, start, path, visited]) # depth, position, path, visited nodes

    while fringe:
        current = fringe.pop()
        depth = current[0]
        current_node = current[1]
        path = current[2]
        visited = current[3]

        if current_node == goal:
            return path 

        child_nodes = getNeighbors(current_node)
        for node in child_nodes:
            if node not in visited:
                fringe.append([depth + 1, node, path + [node], visited + [node]])

    return path

def bfs(start, goal):
    visited = [start]
    path = [start]
    fringe = deque()
    fringe.append([0, start, path, visited]) # depth, position, path, visited nodes

    while fringe:
        current = fringe.popleft()
        depth = current[0]
        current_node = current[1]
        path = current[2]
        visited = current[3]

        if current_node == goal:
            return path 

        child_nodes = getNeighbors(current_node)
        for node in child_nodes:
            if node not in visited:
                fringe.append([depth + 1, node, path + [node], visited + [node]])

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

    if x_add <= constants.MAX_SKILL_LEVEL:
        neighbors.append([x_add, y])
    
    if y_add <= constants.MAX_SKILL_LEVEL:
        neighbors.append([x, y_add])
    
    return neighbors

if __name__ == "__main__":

    result = bfs([1,1], [constants.WIN["strength"], constants.WIN["intellect"]])
    print("path", result)
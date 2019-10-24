from collections import deque
import constants

def dfs(start, goal):
    visited = [start]
    path = [start]
    fringe = deque()
    actions = []
    fringe.append([0, start, path, visited, actions]) # depth, position, path, visited nodes, actions taken

    while fringe:
        current = fringe.pop()
        depth = current[0]
        current_node = current[1]
        path = current[2]
        visited = current[3]
        actions = current[4]

        if current_node == goal:
            return current

        child_nodes = getNeighbors(current_node)
        for node in child_nodes:
            (position, move, survivor_type) = node   
            if position not in visited:
                fringe.append([depth + 1, position, path + [position], visited + [position], actions + [move + " " + survivor_type]])

    return [len(path), path[-1], path, visited, actions]

def bfs(start, goal):
    visited = [start]
    path = [start]
    fringe = deque()
    actions = []
    fringe.append([0, start, path, visited, actions]) # depth, position, path, visited nodes, actions taken

    while fringe:
        current = fringe.popleft()
        depth = current[0]
        current_node = current[1]
        path = current[2]
        visited = current[3]
        actions = current[4]

        if current_node == goal:
            return current

        child_nodes = getNeighbors(current_node)
        for node in child_nodes:
            (position, move, survivor_type) = node   
            if position not in visited:
                fringe.append([depth + 1, position, path + [position], visited + [position], actions + [move + " " + survivor_type]])

    return [len(path), path[-1], path, visited, actions]

def getNeighbors(current):

    neighbors = []
    x = current[0]
    y = current[1]
    x_add = x + 1
    x_sub = x - 1
    y_add = y + 1
    y_sub = y - 1

    if x_sub > 0:
        neighbor_info = ([x_sub, y], "eliminate", "athlete") 
        neighbors.append(neighbor_info)
    
    if y_sub > 0:
        neighbor_info = ([x, y_sub], "eliminate", "genius") 
        neighbors.append(neighbor_info)

    if x_add <= constants.MAX_SKILL_LEVEL:
        neighbor_info = ([x_add, y], "recruit", "athlete") 
        neighbors.append(neighbor_info)
    
    if y_add <= constants.MAX_SKILL_LEVEL:
        neighbor_info = ([x, y_add], "recruit", "genius")
        neighbors.append(neighbor_info)
    
    return neighbors

def run_ai(strategy):
    result = 0
    if strategy == "bfs":
        result = bfs([1,1], [constants.WIN["strength"], constants.WIN["intellect"]])
    elif strategy == "dfs":
        result = dfs([1,1], [constants.WIN["strength"], constants.WIN["intellect"]])
    print("depth: ", result[0])
    print("postion: ", result[1])
    print("path: ", result[2])
    print("visited: ", result[3])
    print("actions: ", result[4])

if __name__ == "__main__":

    result = dfs([1,1], [constants.WIN["strength"], constants.WIN["intellect"]])
    print("depth: ", result[0])
    print("postion: ", result[1])
    print("path: ", result[2])
    print("visited: ", result[3])
    print("actions: ", result[4])
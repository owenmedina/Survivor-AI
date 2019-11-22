from collections import deque
import constants
import SurvivorBot
import copy

class PriorityQueue(object): 
    def __init__(self): 
        self.queue = [] 
  
    def __str__(self): 
        return ' '.join([str(i) for i in self.queue]) 
  
    # for checking if the queue is empty 
    def isEmpty(self): 
        return len(self.queue) == [] 
  
    # for inserting an element in the queue 
    def insert(self, data): 
        self.queue.append(data) 
  
    # for popping an element based on Priority 
    def pop(self): 
        try: 
            max = 0
            for i in range(len(self.queue)):
                curr = self.queue[-1] # last element of data is always priority value
                if curr > self.queue[max]: 
                    max = i
            item = self.queue[max] 
            del self.queue[max] 
            return item 
        except IndexError: 
            print() 
            exit() 

def dfs(start, goal, survivors, total_skills):
    survivors_copy = copy.deepcopy(survivors)
    skills_copy = copy.deepcopy(total_skills)
    visited = [start]
    path = [start]
    fringe = deque()
    actions = []
    fringe.append([0, start, path, visited, actions, survivors_copy, skills_copy]) # depth, position, path, visited nodes, actions taken

    while fringe:
        current = fringe.pop()
        depth = current[0]
        current_node = current[1]
        path = current[2]
        visited = current[3]
        actions = current[4]
        current_survivors = current[5]
        current_skills = current[6]

        if current_node == goal:
            total_skills.update(current_skills)
            return current

        child_nodes = getNeighbors(current_node, current_survivors, current_skills)
        for node in child_nodes:
            (position, move, survivor_type, new_survivors, new_skills) = node   
            if position not in visited:
                fringe.append([depth + 1, position, path + [position], visited + [position], actions + [move + " " + survivor_type], new_survivors, new_skills])

    total_skills.update(skills_copy)
    return [len(path), path[-1], path, visited, actions, survivors_copy, skills_copy]

def bfs(start, goal, survivors, total_skills):
    survivors_copy = copy.deepcopy(survivors)
    skills_copy = copy.deepcopy(total_skills)
    visited = [start]
    path = [start]
    fringe = deque()
    actions = []
    fringe.append([0, start, path, visited, actions, survivors_copy, skills_copy]) # depth, position, path, visited nodes, actions taken

    while fringe:
        current = fringe.popleft()
        depth = current[0]
        current_node = current[1]
        path = current[2]
        visited = current[3]
        actions = current[4]
        current_survivors = current[5]
        current_skills = current[6]

        if current_node == goal:
            total_skills.update(current_skills)
            return current

        child_nodes = getNeighbors(current_node, current_survivors, current_skills)
        for node in child_nodes:
            (position, move, survivor_type, new_survivors, new_skills) = node   
            if position not in visited:
                fringe.append([depth + 1, position, path + [position], visited + [position], actions + [move + " " + survivor_type], new_survivors, new_skills])

    total_skills.update(skills_copy)
    return [len(path), path[-1], path, visited, actions, survivors_copy, skills_copy]

def manhattanDistance(start, goal, survivors, total_skills):
    # append the first occuring node of whatever has the nearest distance to the goal
    survivors_copy = copy.deepcopy(survivors)
    skills_copy = copy.deepcopy(total_skills)
    visited = [start]
    path = [start]
    fringe = PriorityQueue()
    actions = []
    fringe.insert([0, start, path, visited, actions, survivors_copy, skills_copy]) # depth, position, path, visited nodes, actions taken

    while fringe:
        current = fringe.pop()
        print("Priority:", current[-1])
        depth = current[0]
        current_node = current[1]
        path = current[2]
        visited = current[3]
        actions = current[4]
        current_survivors = current[5]
        current_skills = current[6]
        priority_value = current[-1]

        if current_node == goal:
            total_skills.update(current_skills)
            return current

        child_nodes = getMDNeighbors(current_node, current_survivors, current_skills)
        for node in child_nodes:
            (position, move, survivor_type, new_survivors, new_skills, priority_value) = node   
            if position not in visited:
                fringe.insert([depth + 1, position, path + [position], visited + [position], actions + [move + " " + survivor_type], new_survivors, new_skills, priority_value])

    total_skills.update(skills_copy)
    return [len(path), path[-1], path, visited, actions, survivors_copy, skills_copy, priority_value]

def getNeighbors(current, survivors, total_skills):
    neighbors = []
    x = current[0]
    y = current[1]
    x_add = x + 1
    x_sub = x - 1
    y_add = y + 1
    y_sub = y - 1

    if x_sub > 0:
        new_survivors = copy.deepcopy(survivors)
        new_skills = copy.deepcopy(total_skills)
        athlete = SurvivorBot.find_athlete(new_survivors)
        SurvivorBot.eliminate_survivor(athlete, new_survivors, new_skills)
        neighbor_info = ([x_sub, y], "eliminate", athlete, new_survivors, new_skills) 
        neighbors.append(neighbor_info)
    
    if y_sub > 0:
        new_survivors = copy.deepcopy(survivors)
        new_skills = copy.deepcopy(total_skills)
        genius = SurvivorBot.find_genius(new_survivors)
        SurvivorBot.eliminate_survivor(genius, new_survivors, new_skills)
        neighbor_info = ([x, y_sub], "eliminate", genius, new_survivors, new_skills) 
        neighbors.append(neighbor_info)

    if x_add <= constants.MAX_SKILL_LEVEL:
        new_survivors = copy.deepcopy(survivors)
        new_skills = copy.deepcopy(total_skills)
        athlete = SurvivorBot.recruit_athlete(new_survivors, new_skills)
        neighbor_info = ([x_add, y], "recruit", athlete, new_survivors, new_skills) 
        neighbors.append(neighbor_info)
    
    if y_add <= constants.MAX_SKILL_LEVEL:
        new_survivors = copy.deepcopy(survivors)
        new_skills = copy.deepcopy(total_skills)
        genius = SurvivorBot.recruit_genius(new_survivors, new_skills)
        neighbor_info = ([x, y_add], "recruit", genius, new_survivors, new_skills)
        neighbors.append(neighbor_info)
    
    return neighbors

def getMDNeighbors(current, survivors, total_skills):
    neighbors = []
    x = current[0]
    y = current[1]
    x_add = x + 1
    x_sub = x - 1
    y_add = y + 1
    y_sub = y - 1

    if x_sub > 0:
        print("x_sub: " + str(x_sub))
        new_survivors = copy.deepcopy(survivors)
        new_skills = copy.deepcopy(total_skills)
        athlete = SurvivorBot.find_athlete(new_survivors)
        SurvivorBot.eliminate_survivor(athlete, new_survivors, new_skills)
        manhattan_distance = getManhattanDistance(x_sub, y)
        neighbor_info = ([x_sub, y], "eliminate", athlete, new_survivors, new_skills, manhattan_distance) 
        neighbors.append(neighbor_info)
    
    if y_sub > 0:
        print("y_sub: " + str(y_sub))
        new_survivors = copy.deepcopy(survivors)
        new_skills = copy.deepcopy(total_skills)
        genius = SurvivorBot.find_genius(new_survivors)
        SurvivorBot.eliminate_survivor(genius, new_survivors, new_skills)
        manhattan_distance = getManhattanDistance(x, y_sub)
        neighbor_info = ([x, y_sub], "eliminate", genius, new_survivors, new_skills, manhattan_distance) 
        neighbors.append(neighbor_info)

    if x_add <= constants.MAX_SKILL_LEVEL:
        new_survivors = copy.deepcopy(survivors)
        new_skills = copy.deepcopy(total_skills)
        SurvivorBot.recruit_athlete(new_survivors, new_skills)
        manhattan_distance = getManhattanDistance(x_add, y)
        neighbor_info = ([x_add, y], "recruit", "athlete", new_survivors, new_skills, manhattan_distance) 
        neighbors.append(neighbor_info)
    
    if y_add <= constants.MAX_SKILL_LEVEL:
        new_survivors = copy.deepcopy(survivors)
        new_skills = copy.deepcopy(total_skills)
        SurvivorBot.recruit_genius(new_survivors, new_skills)
        manhattan_distance = getManhattanDistance(x, y_add)
        neighbor_info = ([x, y_add], "recruit", "genius", new_survivors, new_skills, manhattan_distance)
        neighbors.append(neighbor_info)
    
    return neighbors

def getManhattanDistance(x, y):
    win_strength = constants.WIN["strength"]
    win_intellect = constants.WIN["intellect"]
    return -(abs(win_strength - x) + abs(win_intellect - y))

def run_ai(strategy, survivors, skills):
    result = dict()
    original_skills = copy.deepcopy(skills)
    if strategy == "bfs":
        result['BFS'] = bfs([constants.total_skills["strength"], constants.total_skills["intellect"]], [constants.WIN["strength"], constants.WIN["intellect"]], survivors, skills)
    elif strategy == "dfs":
        result['DFS'] = dfs([constants.total_skills["strength"], constants.total_skills["intellect"]], [constants.WIN["strength"], constants.WIN["intellect"]], survivors, skills)
    elif strategy == "manhattan distance":
        result['MD'] = manhattanDistance([constants.total_skills["strength"], constants.total_skills["intellect"]], [constants.WIN["strength"], constants.WIN["intellect"]], survivors, skills)
    elif strategy == "compare":
        result['MD'] = manhattanDistance([constants.total_skills["strength"], constants.total_skills["intellect"]], [constants.WIN["strength"], constants.WIN["intellect"]], survivors, skills)
        skills.update(original_skills)
        result['BFS'] = bfs([constants.total_skills["strength"], constants.total_skills["intellect"]], [constants.WIN["strength"], constants.WIN["intellect"]], survivors, skills)
    elif strategy == "compared":
        result['MD'] = manhattanDistance([constants.total_skills["strength"], constants.total_skills["intellect"]], [constants.WIN["strength"], constants.WIN["intellect"]], survivors, skills)
        skills.update(original_skills)
        result['DFS'] = dfs([constants.total_skills["strength"], constants.total_skills["intellect"]], [constants.WIN["strength"], constants.WIN["intellect"]], survivors, skills)
    
    for key, value in result.items():
        print("You are using", key)
        print("This strategy reached a depth of", value[0])
        print("\nThe goal state is", value[1])
        print("\nThe strategy traversed through the following path to reach the goal state:", value[2])
        print("\nThe strategy visited the following states/nodes:", value[3])
        print("\nThe actions that can be done from the resulting path are the following:", value[4])

# if __name__ == "__main__":

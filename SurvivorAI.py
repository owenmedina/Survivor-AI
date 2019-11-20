from collections import deque
import constants
import SurvivorBot
import copy

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

def run_ai(strategy, survivors, skills):
    result = 0
    if strategy == "bfs":
        print("You are using BFS!")
        result = bfs([constants.total_skills["strength"], constants.total_skills["intellect"]], [constants.WIN["strength"], constants.WIN["intellect"]], survivors, skills)
    elif strategy == "dfs":
        print("You are using DFS!")
        result = dfs([constants.total_skills["strength"], constants.total_skills["intellect"]], [constants.WIN["strength"], constants.WIN["intellect"]], survivors, skills)
    print("This strategy reached a depth of", result[0])
    print("\nThe goal state is", result[1])
    print("\nThe strategy traversed through the following path to reach the goal state:", result[2])
    print("\nThe strategy visited the following states/nodes:", result[3])
    print("\nThe actions that can be done from the resulting path are the following:", result[4])
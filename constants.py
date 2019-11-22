import random

# TODO: Make strategies constant and method overloading and add phrases to survivor game and survivor AI
NUM_INITIAL_SURVIVORS = 3

# skills
MAX_SKILL_LEVEL = 5
NUM_SKILLS = 2
# list of skills for survival
skills = ["strength", "intellect"]
survivors = dict()
total_skills = dict()
total_skills[skills[0]] = 0
total_skills[skills[1]] = 0

# win conditions
WIN = dict()
WIN["strength"] = random.randint(1,MAX_SKILL_LEVEL)
WIN["intellect"] = random.randint(1,MAX_SKILL_LEVEL)

# user messages
GAME_GREETING = "Welcome to Survivor.....well kinda\n"
GAME_SENTENCE1 = "This is a simplified, modified version of Survivor."
GAME_SENTENCE2A = "In this game, you will be presented with " + str(NUM_INITIAL_SURVIVORS) + " initial survivors with varying levels of skills related to "
GAME_SENTENCE2B = skills[0] + " and " + skills[1] + "."
GAME_SENTENCE2 = GAME_SENTENCE2A + GAME_SENTENCE2B
GAME_SENTENCE3 = "Your goal will be to eliminate and recruit survivors to achieve a level of " + str(WIN["strength"]) + " for strength and " + str(WIN["intellect"]) + " for intellect."
GAME_INSTRUCTIONS = GAME_SENTENCE1 + "\n" + GAME_SENTENCE2 + "\n" + GAME_SENTENCE3 + "\n"
GAME_GOOD_LUCK = "Good luck and happy surviving!"
GAME_ACTION_CHOICE = "What would you like to do? Type your answer. \n > Recruit \n > Eliminate \n > Show Survivors \n > Show Skills \n > Show Goal \n > Run AI"
GAME_CHOICE_RECRUIT = "What type do you wish to recruit? Type your answer. \n > Athlete > Genius"
GAME_CHOICE_ELIMINATE = "Who would you like to eliminate? Type the name of the survivor. Must be case-sensitive."
GAME_STRATEGY_CHOICE = "What search strategy do you wish to use? Type your answer. \n > BFS > DFS"
INVALID_ANSWER_WARNING = "Please type a valid answer.\n"
WIN_MESSAGE = "You've successfully won Survivor! Congratulations!"
LOSE_MESSAGE = "Sorry, you did not win Survivor."

# search strategies
# uninformed
STRATEGIES = ["bfs", "dfs"]
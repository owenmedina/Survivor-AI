NUM_INITIAL_SURVIVORS = 12
NUM_SKILLS = 3
WIN_CONDITION = 5
# list of skills for survival
skills = ["food", "shelter", "intellect"]
GAME_GREETING = "Welcome to Survivor.....well kinda\n"
GAME_SENTENCE1 = "This is a simplified, modified version of Survivor."
GAME_SENTENCE2A = "In this game, you will be presented with " + str(NUM_INITIAL_SURVIVORS) + " initial survivors with varying levels of skills related to"
GAME_SENTENCE2B = skills[0] + ", " + skills[1] + " and " + skills[2] + "."
GAME_SENTENCE2 = GAME_SENTENCE2A + GAME_SENTENCE2B
GAME_SENTENCE3 = "Your goal will be to eliminate and recruit survivors to achieve a level of " + str(WIN_CONDITION) + " for all skills."
GAME_INSTRUCTIONS = GAME_SENTENCE1 + "\n" + GAME_SENTENCE2 + "\n" + GAME_SENTENCE3 + "\n"
GAME_GOOD_LUCK = "\nGood luck and happy surviving!"
INITIAL_RECRUIT_GREETING = "Here are your initial recruits: \n"

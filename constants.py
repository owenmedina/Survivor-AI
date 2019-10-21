import random

# win conditions
WIN = dict()
WIN["strength"] = random.randint(1,5)
WIN["intellect"] = random.randint(1,5)

NUM_INITIAL_SURVIVORS = 3
NUM_SKILLS = 2
# list of skills for survival
skills = ["strength", "intellect"]
GAME_GREETING = "Welcome to Survivor.....well kinda\n"
GAME_SENTENCE1 = "This is a simplified, modified version of Survivor."
GAME_SENTENCE2A = "In this game, you will be presented with " + str(NUM_INITIAL_SURVIVORS) + " initial survivors with varying levels of skills related to "
GAME_SENTENCE2B = skills[0] + " and " + skills[1] + "."
GAME_SENTENCE2 = GAME_SENTENCE2A + GAME_SENTENCE2B
GAME_SENTENCE3 = "Your goal will be to eliminate and recruit survivors to achieve a level of " + str(WIN["strength"]) + " for strength and " + str(WIN["intellect"]) + " for intellect."
GAME_INSTRUCTIONS = GAME_SENTENCE1 + "\n" + GAME_SENTENCE2 + "\n" + GAME_SENTENCE3 + "\n"
GAME_GOOD_LUCK = "Good luck and happy surviving!"
GAME_ACTION_CHOICE = "What would you like to do? Type your answer. \n > Recruit \n > Eliminate \n > Show Survivors \n > Show Skills \n > Show Goal"
GAME_CHOICE_RECRUIT = "What type do you wish to recruit? Type your answer. \n > Athlete > Genius"
GAME_CHOICE_ELIMINATE = "Who would you like to eliminate? Type the name of the survivor. Must be case-sensitive."
INVALID_ANSWER_WARNING = "Please type a valid answer.\n"
WIN_MESSAGE = "You've successfully won Survivor! Congratulations!"
LOSE_MESSAGE = "Sorry, you did not win Survivor."

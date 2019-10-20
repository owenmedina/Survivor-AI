import requests
import random
import constants
import SurvivorBot

def main():
  print(constants.GAME_GREETING)
  print(constants.GAME_INSTRUCTIONS)
  print(constants.GAME_GOOD_LUCK)
  print("\n")

  # recruit initial survivors
  SurvivorBot.initial_recruit()

  # Game Proper
  while not SurvivorBot.goal_test() and SurvivorBot.survivors_recruited < constants.NUM_MAX_SURVIVORS_TO_RECRUIT:
    action = input(constants.GAME_ACTION_CHOICE + "\n").lower()
    if action == "recruit":
      recruit_choice = input(constants.GAME_CHOICE_RECRUIT + "\n").lower()
      if recruit_choice == "gatherer":
        SurvivorBot.recruit_gatherer()
        SurvivorBot.survivors_recruited += 1
      elif recruit_choice == "builder":
        SurvivorBot.recruit_builder()
        SurvivorBot.survivors_recruited += 1
      elif recruit_choice == "genius":
        SurvivorBot.recruit_genius()
        SurvivorBot.survivors_recruited += 1
      else:
        print(constants.INVALID_ANSWER_WARNING)
    elif action == "eliminate":
      eliminate_choice = input(constants.GAME_CHOICE_ELIMINATE + "\n")
      SurvivorBot.eliminate_survivor(eliminate_choice)
    elif action == "show survivors":
      SurvivorBot.print_survivors()
    elif action == "show skills":
      SurvivorBot.print_skill_levels()
    else:
      print(constants.INVALID_ANSWER_WARNING)

    print(SurvivorBot.survivors_recruited)
    
    if SurvivorBot.goal_test():
      print(constants.WIN_MESSAGE)
      break

  if SurvivorBot.goal_test():
    print(constants.WIN_MESSAGE)
  else:
    print(constants.LOSE_MESSAGE)
  
if __name__ == "__main__":
  main()




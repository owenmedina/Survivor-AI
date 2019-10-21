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

  # game proper
  while not SurvivorBot.goal_test():
    action = input(constants.GAME_ACTION_CHOICE + "\n").lower()
    if action == "recruit":
      recruit_choice = input(constants.GAME_CHOICE_RECRUIT + "\n").lower()
      if recruit_choice == "athlete":
        SurvivorBot.recruit_athlete()
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
    elif action == "show goal":
      SurvivorBot.print_goal()
    else:
      print(constants.INVALID_ANSWER_WARNING)
    
    if SurvivorBot.goal_test():
      print(constants.WIN_MESSAGE)
      break

if __name__ == "__main__":
  main()




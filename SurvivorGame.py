import requests
import random
import constants
import SurvivorBot
import SurvivorAI

def main():
  print(constants.GAME_GREETING)
  print(constants.GAME_INSTRUCTIONS)
  print(constants.GAME_GOOD_LUCK)
  print("\n")

  # recruit initial survivors
  
  SurvivorBot.initial_recruit(constants.survivors, constants.total_skills)

  # game proper
  while not SurvivorBot.goal_test(constants.total_skills):
    action = input(constants.GAME_ACTION_CHOICE + "\n").lower()
    if action == "recruit":
      recruit_choice = input(constants.GAME_CHOICE_RECRUIT + "\n").lower()
      if recruit_choice == "athlete":
        SurvivorBot.recruit_athlete(constants.survivors, constants.total_skills)
        SurvivorBot.survivors_recruited += 1
      elif recruit_choice == "genius":
        SurvivorBot.recruit_genius(constants.survivors, constants.total_skills)
        SurvivorBot.survivors_recruited += 1
      else:
        print(constants.INVALID_ANSWER_WARNING)
    elif action == "eliminate":
      eliminate_choice = input(constants.GAME_CHOICE_ELIMINATE + "\n")
      SurvivorBot.eliminate_survivor(eliminate_choice, constants.survivors, constants.total_skills)
    elif action == "show survivors":
      SurvivorBot.print_survivors(constants.survivors)
    elif action == "show skills":
      SurvivorBot.print_skill_levels(constants.total_skills)
    elif action == "show goal":
      SurvivorBot.print_goal()
    elif action == "run ai":
      strategy = input(constants.GAME_STRATEGY_CHOICE + "\n").lower()
      if strategy == "bfs" or strategy == "dfs":
        SurvivorAI.run_ai(strategy)
      else:
        print(constants.INVALID_ANSWER_WARNING)
    else:
      print(constants.INVALID_ANSWER_WARNING)
    
    if SurvivorBot.goal_test(constants.total_skills):
      print(constants.WIN_MESSAGE)
      break

if __name__ == "__main__":
  main()




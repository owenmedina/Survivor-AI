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
  survivors = dict()
  total_skills = dict()
  total_skills[constants.skills[0]] = 0
  total_skills[constants.skills[1]] = 0
  SurvivorBot.initial_recruit(survivors, total_skills)

  # game proper
  while not SurvivorBot.goal_test(total_skills):
    action = input(constants.GAME_ACTION_CHOICE + "\n").lower()
    if action == "recruit":
      recruit_choice = input(constants.GAME_CHOICE_RECRUIT + "\n").lower()
      if recruit_choice == "athlete":
        SurvivorBot.recruit_athlete(survivors, total_skills)
        SurvivorBot.survivors_recruited += 1
      elif recruit_choice == "genius":
        SurvivorBot.recruit_genius(survivors, total_skills)
        SurvivorBot.survivors_recruited += 1
      else:
        print(constants.INVALID_ANSWER_WARNING)
    elif action == "eliminate":
      eliminate_choice = input(constants.GAME_CHOICE_ELIMINATE + "\n")
      SurvivorBot.eliminate_survivor(eliminate_choice, survivors, total_skills)
    elif action == "show survivors":
      SurvivorBot.print_survivors(survivors)
    elif action == "show skills":
      SurvivorBot.print_skill_levels(total_skills)
    elif action == "show goal":
      SurvivorBot.print_goal()
    else:
      print(constants.INVALID_ANSWER_WARNING)
    
    if SurvivorBot.goal_test(total_skills):
      print(constants.WIN_MESSAGE)
      break

if __name__ == "__main__":
  main()




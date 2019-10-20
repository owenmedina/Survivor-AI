import requests
import random
import constants
import SurvivorBot

def main():
  print(constants.GAME_GREETING)
  print(constants.GAME_INSTRUCTIONS)
  print(constants.GAME_GOOD_LUCK)

  # initialize set of survivors as initially empty
  survivors = dict()
  # recruit initial survivors
  print(constants.INITIAL_RECRUIT_GREETING)
  SurvivorBot.initial_recruit(survivors)

if __name__ == "__main__":
  main()




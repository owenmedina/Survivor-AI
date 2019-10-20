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

if __name__ == "__main__":
  main()




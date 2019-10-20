import requests
import random

class SurvivorBot:
  # initialize set of survivors as initially empty
  survivors = dict()
  # initialize list of essentials for survival
  essentials = ["food", "shelter", "intellect"]

  def request_names(num, survivors):
    names = list()

    request_uri = 'https://randomuser.me/api/?results=' + str(num)
    response = requests.get(request_uri)

    for person in response.json()['results']:
      new_name = person['name']['first']
      if new_name in survivors.keys():
        request_names(1) # request another unique name
      else:
        names.append(new_name)
    
    return names
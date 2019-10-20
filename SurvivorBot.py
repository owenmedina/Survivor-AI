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

  def initial_recruit():
    names = request_names(12, survivors)
    for x in range(12):
      traits = dict()

      # Give survivor specialization
      # Try to distribute specialization uniformly
      special = essentials[x%3]
      traits[special] = random.randint(1,3)

      # Make non-specialization 0
      for e in essentials:
        if e != special:
          traits[e] = 0
      
      # Assign traits to survivor
      survivors[names[x]] = traits

  def recruit_gatherer():
    name = request_names(1, survivors)
    traits = dict()

    # Give survivor food specialization
    special = essentials[0]
    traits[special] = random.randint(1,3)

    # Make non-specialization 0
    for e in essentials:
      if e != special:
        traits[e] = 0
    
    # Assign traits to survivor
    survivors[name[0]] = traits

    return name[0]

  def recruit_builder():
    name = request_names(1, survivors)
    traits = dict()

    # Give survivor shelter specialization
    special = essentials[1]
    traits[special] = random.randint(1,3)

    # Make non-specialization 0
    for e in essentials:
      if e != special:
        traits[e] = 0
    
    # Assign traits to survivor
    survivors[name[0]] = traits

    return name[0]

  def recruit_genius():
    name = request_names(1, survivors)
    traits = dict()

    # Give survivor intellect specialization
    special = essentials[2]
    traits[special] = random.randint(1,3)

    # Make non-specialization 0
    for e in essentials:
      if e != special:
        traits[e] = 0
    
    # Assign traits to survivor
    survivors[name[0]] = traits

    return name[0]

  # Testers
  initial_recruit()
  print(len(survivors))
  for name, traits in survivors.items(): 
      print(name + ":\n")
      for trait, value in traits.items():
        print("\t" + trait + ": " + str(value) + "\n")

  recruit_genius()
  print(len(survivors))
  for name, traits in survivors.items(): 
      print(name + ":\n")
      for trait, value in traits.items():
        print("\t" + trait + ": " + str(value) + "\n")
import requests
import random
import constants

def print_survivors(survivors):
  for name, skills in survivors.items(): 
    print(name + ":\n")
    for skill, value in skills.items():
      print("\t" + skill + ": " + str(value) + "\n")

def get_skill_levels(survivors):
  skills = dict()
  skills["food"] = 0
  skills["shelter"] = 0
  skills["intellect"] = 0
  for name, skills in survivors.items(): 
    for skill, value in skills.items():
      skills[skill] = skills[skill] + value

  # print to user
  print("Current skill levels:\n")
  for skill, value in skills.items():
    print("\t" + skill + ": " + str(value))
  return skills

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

def initial_recruit(survivors):
  print("Recruiting first " + str(constants.NUM_INITIAL_SURVIVORS) + " survivors!")
  names = request_names(constants.NUM_INITIAL_SURVIVORS, survivors)
  for x in range(constants.NUM_INITIAL_SURVIVORS):
    skills = dict()

    # Give survivor specialization
    # Try to distribute specialization uniformly
    special = constants.skills[x%constants.NUM_SKILLS]
    skills[special] = random.randint(1,constants.NUM_SKILLS)

    # Make non-specialization 0
    for e in constants.skills:
      if e != special:
        skills[e] = 0
    
    # Assign skills to survivor
    survivors[names[x]] = skills

  print_survivors(survivors)
  print("\n")
  get_skill_levels(survivors)

def recruit_gatherer(survivors):
  name = request_names(1, survivors)
  skills = dict()

  # Give survivor food specialization
  special = constants.skills[0]
  skills[special] = random.randint(1,constants.NUM_SKILLS)

  # Make non-specialization 0
  for e in constants.skills:
    if e != special:
      skills[e] = 0
  
  # Assign skills to survivor
  survivors[name[0]] = skills

  return name[0]

def recruit_builder(survivors):
  name = request_names(1, survivors)
  skills = dict()

  # Give survivor shelter specialization
  special = constants.skills[1]
  skills[special] = random.randint(1,constants.NUM_SKILLS)

  # Make non-specialization 0
  for e in constants.skills:
    if e != special:
      skills[e] = 0
  
  # Assign skills to survivor
  survivors[name[0]] = skills

  return name[0]

def recruit_genius(survivors):
  name = request_names(1, survivors)
  skills = dict()

  # Give survivor intellect specialization
  special = constants.skills[2]
  skills[special] = random.randint(1,constants.NUM_SKILLS)

  # Make non-specialization 0
  for e in constants.skills:
    if e != special:
      skills[e] = 0
  
  # Assign skills to survivor
  survivors[name[0]] = skills

  return name[0]

def eliminate_survivor(name, survivors):
  if name in survivors.keys():
    del survivors[name]
  else:
    print("Can't delete a non-existent survivor!")
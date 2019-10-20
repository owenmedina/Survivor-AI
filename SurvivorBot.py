import requests
import random
import constants

# initialize set of survivors as initially empty
survivors = dict()

# initialize skills
total_skills = dict()
total_skills["food"] = 0
total_skills["shelter"] = 0
total_skills["intellect"] = 0

def print_survivors():
  for name, skills in survivors.items(): 
    print(name + ":\n")
    for skill, value in skills.items():
      print("\t" + skill + ": " + str(value) + "\n")

def print_skill_levels():
  # print to user
  print("Current skill levels:\n")
  for skill, value in total_skills.items():
    print("\t" + skill + ": " + str(value))

def request_names(num):
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
  print("Recruiting first " + str(constants.NUM_INITIAL_SURVIVORS) + " survivors!")
  names = request_names(constants.NUM_INITIAL_SURVIVORS)
  for x in range(constants.NUM_INITIAL_SURVIVORS):
    skills = dict()

    # Give survivor specialization
    # Try to distribute specialization uniformly
    special = constants.skills[x%constants.NUM_SKILLS]
    skills[special] = random.randint(1,constants.NUM_SKILLS)
    # Update total_skills
    total_skills[special] += skills[special]

    # Make non-specialization 0
    for e in constants.skills:
      if e != special:
        skills[e] = 0
    
    # Assign skills to survivor
    survivors[names[x]] = skills

  print_survivors()
  print_skill_levels()

def recruit_gatherer():
  name = request_names(1)
  skills = dict()

  # Give survivor food specialization
  special = constants.skills[0]
  skills[special] = random.randint(1,constants.NUM_SKILLS)
  # Update total_skills
  total_skills[special] += skills[special]

  # Make non-specialization 0
  for e in constants.skills:
    if e != special:
      skills[e] = 0
  
  # Assign skills to survivor
  survivors[name[0]] = skills

  return name[0]

def recruit_builder():
  name = request_names(1)
  skills = dict()

  # Give survivor shelter specialization
  special = constants.skills[1]
  skills[special] = random.randint(1,constants.NUM_SKILLS)
  # Update total_skills
  total_skills[special] += skills[special]

  # Make non-specialization 0
  for e in constants.skills:
    if e != special:
      skills[e] = 0
  
  # Assign skills to survivor
  survivors[name[0]] = skills

  return name[0]

def recruit_genius():
  name = request_names(1)
  skills = dict()

  # Give survivor intellect specialization
  special = constants.skills[2]
  skills[special] = random.randint(1,constants.NUM_SKILLS)
  # Update total_skills
  total_skills[special] += skills[special]

  # Make non-specialization 0
  for e in constants.skills:
    if e != special:
      skills[e] = 0
  
  # Assign skills to survivor
  survivors[name[0]] = skills

  return name[0]

def eliminate_survivor(name):
  if name in survivors.keys():
    del survivors[name]
  else:
    print("Can't delete a non-existent survivor!")

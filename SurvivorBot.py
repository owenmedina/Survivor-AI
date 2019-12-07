import requests
import random
import constants

# counts how many people have been recruited
survivors_recruited = 0

def print_survivors(survivors):
  for name, skills in survivors.items(): 
    print(name + ":\n")
    for skill, value in skills.items():
      print("\t" + skill + ": " + str(value) + "\n")

def print_skill_levels(total_skills):
  # print to user
  print("Current skill levels:\n")
  for skill, value in total_skills.items():
    print("\t" + skill + ": " + str(value))

def print_goal():
  # print to user
  print("Goal:\n")
  for skill, value in constants.WIN.items():
    print("\t" + skill + ": " + str(value))

def request_names(num, survivors):
  names = list()
  request_uri = 'https://randomuser.me/api/?nat=us&results=' + str(num)
  response = requests.get(request_uri)

  for person in response.json()['results']:
    new_name = person['name']['first']
    if new_name in survivors.keys():
      unique_name = request_names(1, survivors)
      names.append(unique_name[0]) # request another unique name
    else:
      names.append(new_name)
  
  return names

def initial_recruit(survivors, total_skills):
  print("Recruiting first " + str(constants.NUM_INITIAL_SURVIVORS) + " survivors!")
  names = request_names(constants.NUM_INITIAL_SURVIVORS, survivors)
  for x in range(constants.NUM_INITIAL_SURVIVORS):
    skills = dict()

    # Give survivor specialization
    # Try to distribute specialization uniformly
    special = constants.skills[x%constants.NUM_SKILLS]
    skills[special] = 1
    # Update total_skills
    total_skills[special] += skills[special]

    # Make non-specialization 0
    for e in constants.skills:
      if e != special:
        skills[e] = 0
    
    # Assign skills to survivor
    survivors[names[x]] = skills

  print_survivors(survivors)
  print_skill_levels(total_skills)

def recruit_athlete(survivors, total_skills):
  name = request_names(1, survivors)
  skills = dict()

  # Give survivor food specialization
  special = constants.skills[0]
  skills[special] = 1
  # Update total_skills
  total_skills[special] += skills[special]

  # Make non-specialization 0
  for e in constants.skills:
    if e != special:
      skills[e] = 0
  
  # Assign skills to survivor
  survivors[name[0]] = skills

  # Print confirmation to user
  print(name[0] + ":\n")
  for skill, value in skills.items():
      print("\t" + skill + ": " + str(value) + "\n")

  return name[0]

def recruit_genius(survivors, total_skills):
  name = request_names(1, survivors)
  skills = dict()

  # Give survivor intellect specialization
  special = constants.skills[1]
  skills[special] = 1
  # Update total_skills
  total_skills[special] += skills[special]

  # Make non-specialization 0
  for e in constants.skills:
    if e != special:
      skills[e] = 0
  
  # Assign skills to survivor
  survivors[name[0]] = skills

  # Print confirmation to user
  print("Recruited " + name[0] + ":\n")
  for skill, value in skills.items():
      print("\t" + skill + ": " + str(value) + "\n")

  return name[0]

def find_athlete(survivors): # Finds the first athlete in survivors
  for name, skills in survivors.items(): 
    for skill, value in skills.items():
        if skill == "strength" and value != 0:
            return name

def find_genius(survivors): # Finds the first genius in survivors
  for name, skills in survivors.items(): 
    for skill, value in skills.items():
        if skill == "intellect" and value != 0:
            return name

def eliminate_survivor(name, survivors, total_skills):
  if name in survivors.keys():
    name_traits = survivors[name]
    for trait, value in name_traits.items():
      total_skills[trait] -= value
    del survivors[name]
  else:
    print("Can't delete a non-existent survivor: " + name)

def goal_test(total_skills):
  for trait, value in total_skills.items():
    if (value != constants.WIN[trait]):
      return False
  return True

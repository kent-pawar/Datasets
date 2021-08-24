''' JavaScript Object Notation '''
import json

with open('states.json') as f:
  data = json.load(f)

print(data)
'''
with open('states.json') as f:
  print(f.read())
'''
'''
#Create New JSON File

with open('new_states.json', 'w') as f:
  json.dump(data, f, indent=2)
'''

#Updating Existing Json File:
#Existing File name: states.json

import json

#function to add data in pre-existing JSON File

def write_json(new_data, file_name):
  with open(file_name, 'r+') as file:
    # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside states
        file_data["states"].append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)

# Python new data to be added:

d = {"name": "Yogesh",
      "abbreviation": "YO",
      "area_codes": ["251", "270", "838", "025", "127"]}

write_json(d, 'states.json')

with open('states.json') as f:
  data = json.load(f)

print(data)
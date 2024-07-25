Python script
The following is the python script
Create a JSON File named data.json
The file named data.json will store the json file given in the assignment
1.	Subtask 1 - ls
Pyls.py
import json # Open the JSON file and load the data 
with open('data.json', 'r') as file: 
data = json.load(file)
 # Accessing data 
print(data["name"]) # Output: "interpreter"

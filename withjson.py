#Json are represented in the form of dictionaries.

import json
interns = {
    "Zach":"zach123",
    "victor": "victor123",
    "tochukwu": "tochi123",
    "jane" : "jane911",
    "bukola": False,
}


# names = json.dump("names.json", "interns")
# print(interns)
with open("names.json", "w") as reader:
    print(json.dump(interns, reader))

all_names = json.dump(interns, reader)
print(all_names)

print(type(all_names))

#use json to 
import json


with open('PHONEBOOK.json') as file_object:
    PHONEBOOK = json.load(file_object)
for k, v in PHONEBOOK.items():
    print(k, ':', v)

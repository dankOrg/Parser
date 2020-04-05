import json
from collections import namedtuple
from json import JSONEncoder

#Later import allData, not groups
from Group import Group

def main():

    #Read file to groupjson

    with open("message_1.json") as f:
        groupJson = f.read()

    groupJson = json.loads(groupJson)
    groupObj = Group(groupJson['participants'], groupJson['messages'], groupJson['title'],
        groupJson['is_still_participant'], groupJson['thread_type'], groupJson['thread_path'])
    

if __name__ == "__main__":
    main()
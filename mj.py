import json
import os

def add_to_dict(date, time, value, name):
    tag = value[0]
    del value[0]
    
    root = {}

    if os.path.exists("data.json"):
        with open("data.json", "r", encoding="utf-8") as f:
            try:
                root = json.load(f)
            except json.JSONDecodeError:
                pass
    else:
        with open('data.json', 'w') as f:
            pass
        root = {}

    if date not in root:
        root[date] = {}
    if time not in root[date]:
        root[date][time] = {}
    if tag not in root[date][time]:
        root[date][time][tag] = {}

    for i in range(len(name)):
        root[date][time][tag].update({name[i]: value[i]})

    with open('data.json', 'w') as f:
        json.dump(root, f, indent=4)
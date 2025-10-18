import json

def write(info, location):
    try:
        with open("mem.json", "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}
    data[location] = info
    with open("mem.json", "w") as f:
        json.dump(data, f)

def wipe():
    open("mem.json", "w").close()

def get(location):
    with open("mem.json", "r") as f:
        data = json.load(f)
    return data.get(location)

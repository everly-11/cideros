import json
import requests

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

def request(url):
    return(requests.get(url).text.replace("\r\n", "\n").removesuffix("\n"))

def getfile(name):
    with open(name, "r") as f:
        return f.read()

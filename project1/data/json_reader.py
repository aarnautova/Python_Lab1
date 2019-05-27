import json


def load_file(filename):
    with open(filename) as json_file:
        return json_file


def load_dict(filename):
    try:
        with open(filename) as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        with open(filename, 'w') as json_file:
            json.dump({"nextId": 0,
                       "items": []}, json_file, indent=4)
            return json.load(json_file)


def write_empty_file(filename):
    with open(filename, 'w') as json_file:
        json.dump({"nextId": 0,
                   "items": []}, json_file, indent=4)


def write_file(filename, data):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

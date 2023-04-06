import json

def load_file(filename, *args, **kwargs):
    with open(filename, "r") as fp:
        data = json.load(fp, *args, **kwargs)
    return data

def save_file(data, filename, *args, **kwargs):
    with open(filename, "w") as fp:
        json.dump(data, fp, *args, **kwargs)
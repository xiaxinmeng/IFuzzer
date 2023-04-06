def ndjsondump(objects):
    return '\n'.join(json.dumps(obj) for obj in objects)
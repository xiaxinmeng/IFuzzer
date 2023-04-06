def b(dictionary, keys, information):
    for key in keys[:-1]:
            dictionary = dictionary[key]
    dictionary[keys[-1]] = information
    return dictionary
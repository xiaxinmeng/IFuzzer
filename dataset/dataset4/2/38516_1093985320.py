class BetterDictionary(dict):
    def bag(classobject, sequence):
        "Fast way to count things"
        b = classobject()
        for k in sequence:
            b[k] = b.get(k,0) + 1
        return b
    bag = classmethod(bag)
import copy

ship = {'Name': 'Slagschip', 'Blocks': 5}

shipData = copy.deepcopy(ship) # needed, otherwise linked-object
shipData['uuid'] = Id # unique Id
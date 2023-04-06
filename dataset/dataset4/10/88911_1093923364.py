config = {'w': 5, 'x': 10, 'y': False, 'z': True}

p = ArgumentParser()
p.add_argument('-x', type=int, default=config['x'])
p.add_argument('-y', action='store_true', default=config['y'])
ns = p.parse_args(['-h'])
for entry in os.scandir(os.path.dirname(os.path.abspath(__file__))):
    if entry.name == 'stat.py':
        print('os.scandir:', entry.stat().st_nlink)
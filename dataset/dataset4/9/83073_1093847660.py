import sys

def hook(name, args):
    if name.startswith('compile'):
        print(name, args)

sys.addaudithook(hook)
compile('a = 1', '<dummy>', 'exec')
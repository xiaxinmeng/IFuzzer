def hook(name, args):
    if name.startswith('socket'):
        print('I', name, args)  # I/R in the IDLE/run processes.
sys.addaudithook(hook)
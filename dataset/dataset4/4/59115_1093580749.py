class dict_action(argparse.Action):
    def __init__(self, *a, **k):
        argparse.Action.__init__(self, *a, **k)
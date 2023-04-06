class Team(UserList):
    def __init__(self, names=None):
        if names:
            UserList.__init__(self,
                [Player(name) for name in names])
        else:
            UserList.__init__()
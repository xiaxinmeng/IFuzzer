class S(str):
    def __str__(self):
        return 'S: ' + str.__str__(self)
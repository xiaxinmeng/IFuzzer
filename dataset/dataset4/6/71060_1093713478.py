if unicode:
    def _stringify(string):
        # convert to 7-bit ascii if possible
        try:
            return string.encode("ascii")
        except UnicodeError:
            return string
else:
    def _stringify(string):
        return string

class AssertionError(Exception):
    def __init__(self,msg):
        self.msg = f"User AssertionError: {msg}"
        # other code

def __init__(*args, **kwargs):
    self = args[0]
    self._name = args[1]
    self._args = args[2:]
    self._kwargs = kwargs
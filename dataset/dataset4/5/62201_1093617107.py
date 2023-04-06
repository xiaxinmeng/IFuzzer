class RawConfigParser:
    def __init__(self, defaults=None, dict_type=dict):
        self._dict = dict_type
        self._sections = self._dict()
        self._defaults = self._dict()
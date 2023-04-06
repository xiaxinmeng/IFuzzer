import sys
from datetime import datetime

class TimePrompt:
    def __init__(self, prefix, suffix):
        self.prefix, self.suffix = prefix, suffix
    def __str__(self):
        return f'{self.prefix}{datetime.now()}{self.suffix}'
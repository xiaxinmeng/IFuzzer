class Color(AutoNumber):
    def __init__(self, pantone=None):
        self.pantone = pantone or 'unknown'

class Swatch(Color):
    AUBURN = ('3497')
    SEA_GREEN = ('1246')
    BLEACHED_CORAL = () # New color, no Pantone code yet!
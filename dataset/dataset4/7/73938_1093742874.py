class Label(Enum):

    RedApple = 1
    GreenApple = 2

    @classmethod
    def _missing_(cls, name):
        for member in cls:
            if member.name.lower() == name.lower():
                return member
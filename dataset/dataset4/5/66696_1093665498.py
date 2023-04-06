class SuperEnum(Enum):
    pass

class SubEnum(SuperEnum):
    sample = 5
    def visible(self):
        return "saw me, right?"
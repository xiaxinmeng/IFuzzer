class SuperEnum(Enum):
    def invisible(self):
        return "but you didn't see me!"

class SubEnum(SuperEnum):
    sample = 5
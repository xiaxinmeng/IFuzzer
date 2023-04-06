class LenientStrEnum(str, Enum):
    @classmethod
    def _missing_(cls, value):
        logger.warning(
            f"[{cls.__name__}] encountered an unknown value!\n"
            f"Luckily I'm a LenientStrEnum, so I won't crash just yet.\n"
            f"You might want to add a new case though.\n"
            f"Value was: '{value}'"
        )
        return UnexpectedStr(value)
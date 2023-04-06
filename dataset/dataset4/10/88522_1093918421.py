class CaseInsensitiveStrEnum(str, Enum):
    @classmethod
    def _missing_(cls, value):
        for member in cls._member_map_.values():
            if member._value_.lower() == value.lower():
                return member
        return super()._missing_(value)
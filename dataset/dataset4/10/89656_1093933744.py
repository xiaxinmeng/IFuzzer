class ABC(enum.Enum):
    a = enum.auto()
    b = enum.auto()
    c = enum.auto()


print(sys.version)
print(*ABC, str(ABC.a), repr(ABC.a))
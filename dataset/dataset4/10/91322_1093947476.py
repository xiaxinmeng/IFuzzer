class RunMode(Enum):
    release = auto()
    debug = auto()

@dataclass
class Run:
    Mode: TypeAlias = RunMode
    mode: Mode = Mode.release
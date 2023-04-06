
class QuasiABC:
    @property
    @abstractmethod
    def x(self) -> int: ...

@dataclass(frozen=True)
class E(QuasiABC):
    x: int

E(10)

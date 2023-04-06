from typing import Sequence, Protocol

class SequenceWithMethod(Sequence, Protocol):
    def method(self) -> None: pass
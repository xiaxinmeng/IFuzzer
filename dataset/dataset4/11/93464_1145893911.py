from enum import Enum, auto
from typing import Any

class Day(Enum):

    def _generate_next_value_(name: str, start: int, count: int, last_values: list[Any]) -> Any:
        return name

    MONDAY = auto()
    # etc

    @property
    def abbr(self):
        return {
            self.MONDAY: "Mon",
            # etc
        }[self]

print(Day.MONDAY, Day.MONDAY.value, Day.MONDAY.abbr)
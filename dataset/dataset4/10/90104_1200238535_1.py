from dataclasses import dataclass, field
from datetime import date

date_alias = date

@dataclass
class T:
    date: date_alias = field()
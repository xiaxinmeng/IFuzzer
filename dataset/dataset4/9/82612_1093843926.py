
import dataclasses
from typing import Optional

@dataclasses.dataclass
class TestingDataclass:
    base_path: dataclasses.InitVar[Optional[str]] = None

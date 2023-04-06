from typing import List, Union


class Level0A:
    pass


class Level0B:
    class Level1A:
        subs: List[Level0A]

    class Level1B:
        subs: List[Level1A]
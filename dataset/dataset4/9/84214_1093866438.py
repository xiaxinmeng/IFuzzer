from typing import List


class Level0A:
    pass


class Level0B:
    class Level1A:
        pass

    class Level1B(Level1A):
        pass

    class Level1C:
        test: Level1A
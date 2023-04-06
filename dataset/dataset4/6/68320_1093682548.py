from pathlib import Path

class PPath(Path):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

test = PPath("dir", "test.txt")
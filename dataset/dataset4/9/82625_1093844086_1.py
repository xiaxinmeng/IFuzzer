from dataclasses import dataclass

@dataclass(frozen=True)
class Dataclass:
    #...big list of members
    member20: int
    
    def __init__(self, member20: str, **kwargs):
        # Oh, that's better :)
        self.__default_init__(member20=int(member20), **kwargs)
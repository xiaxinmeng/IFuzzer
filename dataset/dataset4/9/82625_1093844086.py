from dataclasses import dataclass

@dataclass(frozen=True)
class Dataclass:
    #...big list of members
    member20: int
    
    def __init__(self, member20: str, **kwargs):
        # self.member20 = int(member20)
        object.__setattr__(self, "member20", int(member20))
        # Now we have to trivially initialize 
        # 20 other members like that :[
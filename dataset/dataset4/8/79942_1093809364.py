import dataclasses
import othermodule # is an external dependency

@dataclass
class City:
    name: str
    position: othermodule.Point # Point is a dataclass

    def update_position(self):
        obj = anymodule.get_position(name=self.name)
        
        # The classic solution would be to do
        self.position.x = obj.x
        self.position.y = obj.y

        # what if othermodule adds z (altitude) to Point?
        # we could imagine:
        dataclasses.update(self.position, obj)

        # I'm currently doing:
        self.position.__dict__.update(obj.__dict__)
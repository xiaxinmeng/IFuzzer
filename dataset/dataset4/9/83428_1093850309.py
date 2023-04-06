@dataclass
class Foo:
    bar = field(default=some_descriptor)
    # technically this is a descriptor field without a default value or at the very least, the dataclass constructor can't know because it doesn't know what field, if any, this delegates to. This means this will show up as optional in the __init__ signature but it might not be.

    bar = field(default=some_descriptor, default_factory=lambda:4)
    # this could be a solve for the above problem. The dc constructor would install the constructor at the class level and assign 4 to the instance attribute in the __init__. Still doesn't tell the dc constructor if a field is optional or not when it's default value is a descriptor and no default_factory is passed. And it feels a lot more like hack than anything else.
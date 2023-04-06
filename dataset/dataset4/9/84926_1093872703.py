
from abc import ABCMeta, abstractnestedclass

class BaseComponent(metaclass=ABCMeta):
    @abstractnestedclass
    class Config:
        pass

class MissingNestedComponent(BaseComponent):
    # This will raise when constructed because 
    # BaseComponent.Config is not implemented
    pass

class NonraisingComponent(BaseComponent):
    # This will be constructable
    class NonraisingComponentConfig(BaseComponent.Config):
        pass
    pass

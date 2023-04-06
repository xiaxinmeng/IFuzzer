
from abc import ABCMeta, ABC
from typing import Union

class MetaclassMixin(ABC):
    pass 

class Meta(MetaclassMixin, ABCMeta):
    pass

print(Union[str, Meta])

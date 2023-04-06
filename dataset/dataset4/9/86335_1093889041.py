
from typing import overload, Any, Optional

@overload
def utf8(value: None) -> None: 
    ...
@overload
def utf8(value: bytes) -> bytes: 
    ...
def utf8(value: Optional[bytes]) -> Optional[bytes]:
    if value is None:
        return None
    return b''

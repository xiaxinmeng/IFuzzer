import random
from uuid import UUID

def uuid4_fast():
    return UUID(int=random.getrandbits(128), version=4)
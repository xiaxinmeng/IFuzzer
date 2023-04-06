
class EqHashHack:
    def __init__(self, k, cb):
        self._k = k
        self._cb = cb

    def __hash__(self):
        return hash(self._k)

    def __eq__(self, *args, **kwargs):
        self._cb()
        return False
        
lock = asyncio.Lock()
vars(lock)[EqHashHack(k="_loop", cb=lambda: lock.aquire())] = None

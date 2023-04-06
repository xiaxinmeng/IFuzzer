@dataclass
class User:
    name: str
    ws: WebSocket = field(hide=True)


user = User("NiumXp", None)
assert asdict(user) == {"name": "NiumXp"}
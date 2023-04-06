class User: pass

class Group:
  users: WeakSet[User]

  def __init__(self, users: Iterable[User]):
    self.users = WeakSet(users)
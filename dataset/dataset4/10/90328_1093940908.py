from typing import NewType

UserId = NewType('UserId', int)
ProUserId = NewType('ProUserId', UserId)

x: ProUserId = ProUserId(UserId(1))
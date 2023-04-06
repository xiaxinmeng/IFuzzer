T = TypeVar("T")

class MessageCallArgs(NamedTuple, Generic[T]):
    caller: Actor
    actorAddress: TypedActorAddress[T]
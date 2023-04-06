if TYPE_CHECKING:
    class TD(TypedDict, Generic[T]):
        a: T
else:
    class TD(TypedDict):
        a: T

d: TD[int] = {"a": 1}
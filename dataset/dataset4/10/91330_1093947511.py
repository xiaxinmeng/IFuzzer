class Descriptor(Generic[T]):
    def __get__(self, __obj: object | None, __owner: Any) -> T:
        return getattr(__obj, "_x")

    def __set__(self, __obj: object | None, __value: T) -> None:
        setattr(__obj, "_x", __value)

@dataclass
class InventoryItem:
    quantity_on_hand: Descriptor[int] = Descriptor[int]()

i = InventoryItem(13)     # calls __set__ with 13
print(i.quantity_on_hand) # 13 -- obtained via call to __get__
i.quantity_on_hand = 29   # calls __set__ with 29
print(i.quantity_on_hand) # 29 -- obtained via call to __get__
@dataclass
class InventoryItem:
    quantity_on_hand: Descriptor[int] # No default value

i = InventoryItem(13)      # Sets quantity_on_hand to 13 -- No call to Descriptor.__set__
print(i.quantity_on_hand)  # 13 -- No call to Descriptor.__get__
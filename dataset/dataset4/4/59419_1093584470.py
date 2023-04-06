itemList = ["apple", "bananna", "blueberry", "coconut"]
print("Before: {0}".format(itemList))

for item in itemList:
    if(item.startswith("b")):
        itemList.remove(item)

print("After:  {0}".format(itemList))
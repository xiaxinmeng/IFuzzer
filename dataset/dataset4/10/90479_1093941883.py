a=1
b=2
c=3
list=a, b, c
#Remove spaces at the end of lists. Because sometimes spaces are errors or not depending on the number of items in your list. Remove list delineators to save a little memory and time not typing those delineator symbols on list definitions.
for items in list:
    print(items)
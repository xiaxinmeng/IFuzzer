import random
d = {
    0: "foobar0",
    1: "foobar1",
    2: "foobar2",
    3: "foobar3",
    4: "foobar4",
    5: "foobar5",
    # Note: 6 is missing.
    7: "foobar7",
    8: "foobar8",
    9: "foobar9",
}
pivot=random.choice(d)
print(pivot)
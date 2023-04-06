def test(a='a', b='b'):
    print(a, b)

opta = dict()
optb = dict(a=1, b=2)
test(**(opta or {}))  # <- works on all python
test(**optb or {})    # <- fails on current hg tip
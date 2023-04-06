i.inlined_asdict = asdict
assert asdict(i) == i.asdict() == i.inlined_asdict(i)
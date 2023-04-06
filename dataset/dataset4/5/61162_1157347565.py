cx = sqlite3.connect(":memory:")
with cx.savepoint("sp1"):
    with cx.savepoint("sp2"):
        pass

# alternatively, we could auto-generate savepoint names internally
with cx.savepoint():
    with cx.savepoint():
        pass
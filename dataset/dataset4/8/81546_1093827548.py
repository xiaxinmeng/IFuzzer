def rec():
    try:
        rec()
    except Exception:
        rec()
rec()
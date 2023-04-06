if word[:n] == attr and word != "__builtins__" and hasattr(object, word):
    val = getattr(object, word)
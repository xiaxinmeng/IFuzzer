def is_std(package: str) -> bool:
    """Returns True if package module came with from Python."""

    if package in C.BUILTIN_MODULE_NAMES:
        return True
    spec = get_spec(package)
    if spec and isinstance(spec.origin, str):
        return any(
            (
                spec.origin.startswith(C.STDLIB_PATH),
                spec.origin in ["built-in", "frozen"],
                spec.origin.endswith(".so"),
            )
        )
    else:
        return False
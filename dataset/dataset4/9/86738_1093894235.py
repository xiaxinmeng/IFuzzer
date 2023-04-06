@dataclass(eq=True, frozen=True)
class ArgumentPath:
    must_exist: bool = False
    # Add other conditions as needed.

    def __call__(self, val):
        result = Path(val)
        if self.must_exist:
            if not result.exists():
                raise ValueError(f"path {result} must exist")
        return result
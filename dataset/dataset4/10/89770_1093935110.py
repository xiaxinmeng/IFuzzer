class Explanation(Exception):
    __module__ = "builtins"
    def __str__(self) -> str:
        return f"\n{self.args[0]}"
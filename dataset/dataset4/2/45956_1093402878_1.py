print()
try:
    With().huh
except AttributeError as exc:
    print(exc)

print()
import enum  # broken value property tries to access self.not_here
class TestEnum(enum.Enum):
    one = 1

print(TestEnum.one.value)
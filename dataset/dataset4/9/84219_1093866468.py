
import pathlib


class CustomAccessor(pathlib._NormalAccessor):
    pass


def print_accessor(path):
    if isinstance(path._accessor, CustomAccessor):
        print("    %r: custom" % path)
    else:
        print("    %r: normal" % path)


print("Here's a path with a custom accessor:")
p = pathlib.Path("/tmp")
p._accessor = CustomAccessor()
print_accessor(p)

print("Our accessor type is retained in resolve(), absolute() and readlink():")
print_accessor(p.absolute())
print_accessor(p.resolve())
#print_accessor(p.readlink())

print("But not in any other path-creating methods!")
print_accessor(p.with_name("foo"))
print_accessor(p.with_suffix(".foo"))
print_accessor(p.relative_to("/"))
print_accessor(p / "foo")
print_accessor(p.joinpath("foo"))
print_accessor(p.parent)
print_accessor(p.parents[0])
print_accessor(list(p.iterdir())[0])
print_accessor(list(p.glob("*"))[0])
print_accessor(list(p.rglob("*"))[0])
#print_accessor(p.expanduser())

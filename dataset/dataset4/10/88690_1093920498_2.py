class S(typing.Sized):
        def __len__(self):
            return 0

print("'Sized' in typing_unnamed:", 'Sized' in typing_unnamed)
print("[t.__name__ for t in S.__mro__]:", [t.__name__ for t in S.__mro__])  # here __name__ is resolved!
print("getattr(typing.Sized, '__name__', None):", getattr(typing.Sized, '__name__', None))
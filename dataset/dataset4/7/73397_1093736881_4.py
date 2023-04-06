import traceback

class ClearFrames:
   def __init__(self, clear_frames):
       self.clear_frames = clear_frames
   def __enter__(self):
       return self

   def __exit__(self, exc_type, exc_value, tb):
       assert exc_type is ZeroDivisionError, exc_type
       if self.clear_frames:
           traceback.clear_frames(tb)  # This is the only difference between the tests.
       return True

# This is essentially the same test case as before, but structured using
# a context manager that either does or does not clear the traceback frames.
def clear_test(clear_frames):
    spam = Spam()
    assert spam.get_next() == 1
    with ClearFrames(clear_frames):
        spam.get_next()
    try:
        assert spam.get_next() == 3
    except StopIteration:
        print(" ... got StopIteration")
        return
    print(" ... clear_test passed")

print("\nDo not clear frames")
clear_test(False)
print("\nClear frames")
clear_test(True)
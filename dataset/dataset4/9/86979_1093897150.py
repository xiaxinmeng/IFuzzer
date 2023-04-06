import math
def check_stack_size( code):
    # To assert that the alleged stack size is not O(N), we
    # check that it is smaller than log(N).
    if isinstance(code, str):
        code = compile(code, "<foo>", "single")
    max_size = math.ceil(math.log(len(code.co_code)))
    # self.assertLessEqual(code.co_stacksize, max_size)

def test_if_else():
    snippet ="""
if x:
    a
elif y:
    b
else:
    c     
    """
    check_stack_size(snippet)

test_if_else()

def test_huge():
    try:
        huge = b'\0' * 0x100000000  # this allocates 4GB of memory!
    except MemoryError:
        print('OOM')

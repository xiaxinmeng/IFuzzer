from os import DirEntry, scandir

def test_is_dir():
    for item in os.scandir(TEST_DIR):
        if item.is_dir():
            #         ^^ note change
            print(item.path)
    return
def test_is_dir():
    for item in os.scandir(TEST_DIR):
        if item.is_dir:
            print(item.path)
    return
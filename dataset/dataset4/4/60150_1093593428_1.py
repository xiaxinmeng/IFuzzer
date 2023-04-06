if os.path.exists(TEST_PATH):
    shutil.rmtree(TEST_PATH)
if not os.path.exists(TEST_PATH):
    os.makedirs(TEST_PATH)
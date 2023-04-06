with unittest.mock.patch('shutil.sys') as mock_sys:
    del mock_sys.__stdout__
    print(shutil.get_terminal_size((3, 3)))
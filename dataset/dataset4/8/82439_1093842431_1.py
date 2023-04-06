def test_error_callargs_unconfigured_too_many_args():

	dll = ctypes.windll.LoadLibrary('tests/demo_dll.dll')
	square_int = dll.square_int

	with pytest.raises(ValueError):
		a = square_int(1, 2, 3)
def test_error_callargs_unconfigured_too_few_args():

	dll = ctypes.windll.LoadLibrary('tests/demo_dll.dll')
	mul_ints = dll.mul_ints

	with pytest.raises(ValueError):
		a = mul_ints(7)
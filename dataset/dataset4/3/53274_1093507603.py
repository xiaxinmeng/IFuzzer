def test_main(verbose=None):
    try:
        cwd = os.getcwd()
        test_support.run_unittest(BaseHTTPServerTestCase,
                                SimpleHTTPServerTestCase,
                                CGIHTTPServerTestCase
                                )
    finally:
        os.chdir(cwd)

if __name__ == '__main__':
    test_main()
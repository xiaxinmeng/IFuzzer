def test_main(verbose=None):
    test_classes = (
        TestBasicOps,
        TestVariousIteratorArgs,
        TestGC,
    )
    support.run_unittest(*test_classes)
def test_main(verbose=None):
    test_classes = [TestHeapPython, TestErrorHandling]
    test_support.run_unittest(*test_classes)

    test_support.reload('heapq', hiding='_heapq')
    test_support.run_unittest(*test_classes)
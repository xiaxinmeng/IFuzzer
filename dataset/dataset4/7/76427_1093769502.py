def skip_segfault_on_android(test):
    # Issue python/cpython#76319: Raising SIGSEGV on Android may not cause a crash.
    return unittest.skipIf(is_android,
                           'raising SIGSEGV on Android is unreliable')(test)
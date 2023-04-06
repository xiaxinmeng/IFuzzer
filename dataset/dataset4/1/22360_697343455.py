
        # There's no way to unregister a codec search function, so we just
        # ensure we render this one fairly harmless after the test
        # case finishes by using the test case repr as the codec name
        # The codecs module normalizes codec names, although this doesn't
        # appear to be formally documented...
        # We also make sure we use a truly unique id for the custom codec
        # to avoid issues with the codec cache when running these tests
        # multiple times (e.g. when hunting for refleaks)

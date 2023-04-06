def test_strftime_format_check(self):
    # Test that strftime does not crash on invalid format strings
    # that may trigger a buffer overread. When not triggered,
    # strftime may succeed or raise ValueError depending on
    # the platform.
    for x in [ '', 'A', '%A', '%AA' ]:
        for y in range(0x0, 0x10):
            for z in [ '%', 'A%', 'AA%', '%A%', 'A%A%', '%#' ]:
                try:
                    time.strftime(x * y + z)
                except ValueError:
                    pass
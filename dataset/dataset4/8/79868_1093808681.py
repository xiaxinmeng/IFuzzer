import difflib

def bugged_diff(expected, actual):
    expected = expected.splitlines( 1 )
    actual = actual.splitlines( 1 )

    # diff = difflib.ndiff( expected, actual )
    if expected != actual:
        diff = difflib.context_diff( expected, actual, fromfile='expected input', tofile='actual output', lineterm='\n' )
        return '\n' + ''.join( diff )


if __name__ == '__main__':
    expected = "testing.main_unit_tests.test_dictionaryBasicLogging:416 - dictionary\n" \
            "testing.main_unit_tests.test_dictionaryBasicLogging:417 - dictionary {1: 'defined_chunk'}"

    actual = "15:49:35:912.348986 - testing.main_unit_tests - dictionary\n" \
            "15:49:35:918.879986 - testing.main_unit_tests - dictionary {1: 'defined_chunk'}"

    print( expected, actual )
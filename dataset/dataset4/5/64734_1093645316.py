def main(regrtest_args):
    args = [sys.executable,
            '-W', 'default',      # Warnings set to 'default'
            '-bb',                # Warnings about bytes/bytearray
            '-E',                 # Ignore environment variables
            ]
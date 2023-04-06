
import plistlib
dat = b'AAAAAAAAAAAwAAA\xc9AAAAAAAAAAAAA\x9cAAAAAAAAAAAAAAAAAA\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00AAAAA\x04\xb2\xaaAAAAAA'
plistlib.loads(dat, fmt=plistlib.FMT_BINARY)

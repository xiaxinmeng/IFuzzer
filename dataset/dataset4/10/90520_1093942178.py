import os.path
paths = [
    r'C:\CON',
    r'C:\PRN',
    r'C:\AUX',
    r'C:\NUL',
    r'C:\COM1',
    r'C:\COM2',
    r'C:\COM3',
    r'C:\COM9',
    r'C:\LPT1',
    r'C:\LPT2',
    r'C:\LPT3',
    r'C:\LPT9',
    r'C:\foo. . .',
]
for path in paths:
    print(os.path.abspath(path))
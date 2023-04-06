
from typing import Union


class FakePath:
    def __init__(self, path):
        self.path = path

    def __fspath__(self) -> Union[str, bytes]:
        return self.path


if __name__ == "__main__":
    from tempfile import TemporaryDirectory

    # You need to create `existing_path` directory

    with TemporaryDirectory(dir=FakePath("existing_path")) as str_path:
        print(str_path)  # 'existing_path/...'

    with TemporaryDirectory(dir=FakePath(b"existing_path")) as byte_path:
        print(byte_path)  # expected b'existing_path/...' but raised TypeError


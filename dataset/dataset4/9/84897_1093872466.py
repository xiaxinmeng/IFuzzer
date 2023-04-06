
import mmap
import pathlib
import tempfile


def main():
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = pathlib.Path(tmp)
        path = tmp_path / "eg"

        path.write_bytes(b"Hello, World!")

        with path.open("rb") as rf:
            mm = mmap.mmap(rf.fileno(), 0, mmap.MAP_SHARED, mmap.PROT_READ)
            path.write_bytes(b"")
            bytes(mm)

if __name__ == "__main__":
    main()

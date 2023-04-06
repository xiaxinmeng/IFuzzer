def main():
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = pathlib.Path(tmp)
        path = tmp_path / "eg"

        path.write_bytes(b"Hello, World!")

        with path.open("r+b") as rf:
            mm = mmap.mmap(rf.fileno(), 0, mmap.MAP_SHARED, mmap.PROT_READ)
            rf.truncate(0)
            bytes(mm)

if __name__ == "__main__":
    main()
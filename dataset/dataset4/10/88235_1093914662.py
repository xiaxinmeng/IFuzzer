from pathlib import Path

base_dir = Path("/path/to/lotta/files/")
files = base_dir.glob("*.txt")            # return immediately
first_file = next(files)                  # doesn't return immediately
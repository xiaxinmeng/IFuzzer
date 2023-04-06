
from pathlib import Path
import os
import subprocess

dir_name = os.environ.get("WORKSPACE", None) or "."
output_directory = Path(dir_name) / "results"
res = subprocess.run(["mytest", "--output", output_directory])

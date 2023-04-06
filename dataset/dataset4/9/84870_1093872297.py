
import os
from pathlib import Path

os.chdir(Path(__file__).parent)
print(Path(__file__).absolute())

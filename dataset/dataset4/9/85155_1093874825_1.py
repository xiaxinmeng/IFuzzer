import sys
from pathlib import Path
from urllib.request import urlopen
path = Path(sys.argv[1])
path.write_text('Hello, World!')
with urlopen(path.as_uri()) as resp:
    print(resp.read())
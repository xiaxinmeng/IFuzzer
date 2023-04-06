# Both work in Python 3.9 and 3.10, but both fail in 3.11.0a3
from importlib.resources import files, read_text
read_text("hypothesis.vendor", "tlds-alpha-by-domain.txt")
files("hypothesis.vendor").joinpath("tlds-alpha-by-domain.txt").read_text()
import sys
import atheris

with atheris.instrument_imports():
  import json

def harness(data):
    fdp = atheris.FuzzedDataProvider(data)
    obj = fdp.ConsumeString(fdp.ConsumeIntInRange(0, 8))
    new = json.loads(json.dumps(obj))
    assert obj == new, "DIFFERENT!: {} {}".format(repr(obj), repr(new))

atheris.Setup(sys.argv, harness)
atheris.Fuzz()
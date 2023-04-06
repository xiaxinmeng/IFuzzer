import _csv

class MockFile:
    def write(self, _):
        pass

writer = _csv.writer(MockFile())
writer.writerow(["A"*0x10000, '"'*0x7fffff00]) 
class Test:
    def __init__(self, value):
        self.value = value

def main():
    ts = [Test(x) for x in range(10)]
    sum(t.value for t in ts)
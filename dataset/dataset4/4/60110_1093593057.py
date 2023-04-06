class MyString(str): pass

def convert(s):
    return MyString("*" + s)

parser = ArgumentParser()
parser.add_argument("--test", dest="test", type=convert, default="foo")
args = parser.parse_args()

print(args.test)
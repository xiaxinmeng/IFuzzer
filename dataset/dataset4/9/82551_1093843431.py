class AClass(object):
    def __init__(self, val=[]):
        self.contents = val

    def add_content(self, newcontent):
        self.contents.append(newcontent)
        return self

    def print(self):
        for val in self.contents:
            print(str(val))


if __name__ == '__main__':
    sc = AClass()
    sc = sc.add_content("Value1").add_content("Value2")

    sb = AClass()
    sb = sb.add_content("Value3").add_content("Value4")

    sc.print()
    print("--------------------------------")
    sb.print()
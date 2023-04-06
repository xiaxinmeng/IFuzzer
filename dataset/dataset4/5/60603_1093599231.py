import argparse

class TestAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        print("default: {}({})\tdest: {}({})".format(self.default, type(self.default), getattr(namespace, self.dest), type(getattr(namespace, self.dest))))
        if getattr(namespace, self.dest) is self.default:
            print("Replacing with: ", values)
            setattr(namespace, self.dest, values)
        # extra logical code not necessary for testcase

parser = argparse.ArgumentParser()
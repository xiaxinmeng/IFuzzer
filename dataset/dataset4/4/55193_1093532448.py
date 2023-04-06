parser = argparse.ArgumentParser()
a_action = parser.add_argument('-a')
b_action = parser.add_argument('-b')
c_action = parser.add_argument('-c')
d_action = parser.add_argument('-d')
parser.add_mutually_exclusive_group(a_action, c_action)
parser.add_mutually_exclusive_group(a_action, d_action)
...
def opposite(bool):
  if bool is True:
    return False
  elif bool is False:
    return True

from argparse import ArgumentParser
parser = ArgumentParser()
parser.set_defaults(**config_defaults)
parser.add_argument('-V', '--verbose', dest='vrb', action='store_const', const=opposite(config_defaults['verbose']), help='switch on/off verbosity')
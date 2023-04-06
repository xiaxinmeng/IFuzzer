import argparse

def nonnegative_not_suppressed(arg):
  try:
    x = int(arg)
    if x >= 0:
      return x
    else:
      raise argparse.ArgumentTypeError('Enter a nonnegative integer')
  except:
    raise argparse.ArgumentTypeError('Enter a nonnegative integer')

def nonnegative_suppressed(arg):
  try:
    x = int(arg)
    if x >= 0:
      return x
    else:
      raise ValueError('Enter a nonnegative integer')
  except:
    raise ValueError('Enter a nonnegative integer')

p = argparse.ArgumentParser('parser')
p.add_argument('--no-suppress', type=nonnegative_not_suppressed)
p.add_argument('--suppress', type=nonnegative_suppressed)
p.parse_args(['--no-suppress', '-4']) # Displays "Enter a nonnegative integer"
p.parse_args(['--suppress', '-4']) # Displays "invalid nonnegative_suppressed value: '-4'"
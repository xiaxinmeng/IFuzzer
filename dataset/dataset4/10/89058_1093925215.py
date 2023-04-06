import sys

count = 0
def main():

  def f():
    global count
    count += 1
    try:
        f()
    except RecursionError:
        f()

  sys.setrecursionlimit(30)
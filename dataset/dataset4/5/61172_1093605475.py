if __name__ == '__main__':
  try:
    test.support.reap_threads(unittest.main)()
  finally:
    test.support_reap_children()
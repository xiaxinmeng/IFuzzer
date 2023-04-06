def main():
  second_thread = SecondThread()
  second_thread.start()

  # Take the import_lock and then release global interpreter lock in the
  # import_lock_helper module by calling any blocking operation.
  import import_lock_helper

  second_thread.join()

main()
with ThreadPoolExecutor(queue_size=500) as executor:
  for item in parse_a_long_list_of_work(somefile.xml):
    executor.submit(Job(item))
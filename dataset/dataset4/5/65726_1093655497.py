if processes:
   executor = ProcessPoolExecutor()
elif threads:
   executor = ThreadPoolExecutor(1) # or any other value
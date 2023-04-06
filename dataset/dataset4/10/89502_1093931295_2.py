
with ThreadPoolExecutor(max_workers=1, thread_class=MyThread) as executor:
    future = executor.submit(pow, 323, 1235)
    print(future.result())

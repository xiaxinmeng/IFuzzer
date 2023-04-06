def called_very_often():
    with ThreadPool(...) as pool:
        pool.run(blocking_work, args)
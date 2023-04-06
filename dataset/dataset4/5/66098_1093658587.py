for element in element_generator:
    while len(running) >= max_tasks:
        done, pending = concurrent.futures.wait(running, timeout=15.0, return_when=concurrent.futures.FIRST_COMPLETED)
        process_results(done)
        running = pending

    running.add(executor.submit(exe_subprocess, element)) 
 
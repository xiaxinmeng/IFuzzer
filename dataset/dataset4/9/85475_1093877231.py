import time
for clock in "monotonic", "perf_counter":
    print(f"{clock}: {time.get_clock_info(clock)}")
import time
for i in range(10):
    print(f"\r{i}", end='', flush=True)
    time.sleep(1)
print('\n')
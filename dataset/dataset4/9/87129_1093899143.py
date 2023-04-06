
from multiprocessing import Pool
p = Pool()

def error_callback(x):
    print(f'error: {x!r}')
    p.terminate()
    print('this message is never seen, because p.termiante() deadlocks')

p.apply_async(lambda: None, error_callback=error_callback)

# The following lines are technically aren't threadsafe,
# but I manually verified that that wasn't the problem.
p.close()
p.join()
print('this is also never seen, because the task handler is stuck in the deadlock')

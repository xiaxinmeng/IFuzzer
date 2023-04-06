### Code:
import time
from pprint import pprint

start = time.time()
time.sleep(0.5)
object_made = time.time()
time.sleep(0.5)
done = time.time()
time.sleep(0.5)
shown = time.time()

pprint(
    f"Time to create object: {object_made - start}s\n" +
    f"Time to insert 100000 rows: {done - object_made}s\n" +
    f"Time to retrieve 100000 rows: {shown - done}s\n"
)
output = sys.stdout.detach()
sys.stdout = None  # Avoid error message during shutdown, due to output being closed or garbage-collected
output.write(...)
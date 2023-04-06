expires = "3.00"
try:
    expires = int(expires)
except ValueError:
    expires = int(float(expires) * 1e6)

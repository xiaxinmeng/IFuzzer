import io
with io.open('ca.crt') as f:
    ca_crt = f.read()
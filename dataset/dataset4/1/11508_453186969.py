script = '''
import ssl
ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
print(ctx.minimum_version)
'''

proc = subprocess.run([sys.executable, '-c', script],
                      capture_output=True,
                      text=True,
                      check=True,
                      env={**os.environ, 'OPENSSL_CONF': '/non-existing-file'})
assert proc.stdout.strip() == 'TLSVersion.MINIMUM_SUPPORTED'
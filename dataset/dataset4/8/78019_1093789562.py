from io import BytesIO
import http.client

def upload(timeout=None):
    test_file = BytesIO(b"0" * 15 * 1024**2)

    if timeout is not None:
        conn = http.client.HTTPConnection("httpbin.org", timeout=timeout)
    else:
        conn = http.client.HTTPConnection("httpbin.org")

    conn.request("PUT", "/put", body=test_file)
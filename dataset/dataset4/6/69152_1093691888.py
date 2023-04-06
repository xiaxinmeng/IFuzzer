proxy_conn = HTTPConnection("proxy")
proxy_conn.request("CONNECT", "website:443")
proxy_resp = proxy_conn.getresponse()
if proxy_resp.status == PROXY_AUTHENTICATION_REQUIRED:
    # Handle proxy_resp.msg["Proxy-Authenticate"]
    ...
# Handle proxy_resp.msg["X-ProxyMesh-IP"]
...
tunnel = proxy_conn.detach()  # Returns socket and any buffered data
website_conn = HTTPSConnection("website", tunnel=tunnel)
website_conn.request("GET", "/")
...
website_conn.close()
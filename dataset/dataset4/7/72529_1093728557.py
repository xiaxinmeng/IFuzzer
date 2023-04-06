if sys.platform == 'darwin':
    import botocore.vendored.requests.utils, urllib.request
    botocore.vendored.requests.utils.proxy_bypass = urllib.request.proxy_bypass_environment
    botocore.vendored.requests.utils.getproxies = urllib.request.getproxies_environment

    urllib.request.proxy_bypass = urllib.request.proxy_bypass_environment
    urllib.request.getproxies = urllib.request.getproxies_environment
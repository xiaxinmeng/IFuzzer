
import ssl

def verified_stdlib_context(protocol=None, *, cert_reqs=ssl.CERT_REQUIRED, check_hostname=True, **kwargs):
    return ssl._create_unverified_context(protocol, cert_reqs=cert_reqs, check_hostname=check_hostname, **kwargs)

ssl._create_stdlib_context = verified_stdlib_context

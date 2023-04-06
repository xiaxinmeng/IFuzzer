
# workaround for OpenSSL with compression
openssl_extension_kwargs["libraries"].append("z")

file = CDLL("libcrypto.a(libcrypto.so.1.0.0)")
member = CDLL("libcrypto.a(libcrypto.so.1.0.0)", DEFAULT_MODE | 0x00040000)
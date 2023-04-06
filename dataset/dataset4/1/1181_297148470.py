
#ifndef OPENSSL_VERSION_1_1
OpenSSL_add_all_digests();
ERR_load_crypto_strings();
ENGINE_load_builtin_engines();
#endif

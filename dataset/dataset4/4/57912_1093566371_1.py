Py_RndHashSeed = intmask((hash("a") ^ len("a") ^ ord("a")) * DIVIDE) - (ord("a") << 7)
junk_len = 1024
junk =  (("%%0%dX" % junk_len) % random.getrandbits(junk_len *
8)).decode("hex")
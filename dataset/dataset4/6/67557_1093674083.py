txt=b"\x0a\x0a\x0a\x00"
uni=txt.decode("utf-32")
sub="a"*(2**30)
uni.count(sub)
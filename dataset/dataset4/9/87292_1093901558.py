
import io

io.BytesIO(b"abc\ndef\nghi\n").readlines(0) 
# this evaluates to [b"abc\n", b"def\n", b"ghi\n"]

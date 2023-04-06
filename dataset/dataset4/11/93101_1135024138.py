
        # The meaning of a tell() cookie is: seek to position, set the
        # decoder flags to dec_flags, read bytes_to_feed bytes, feed them
        # into the decoder with need_eof as the EOF flag, then skip
        # chars_to_skip characters of the decoded result.  For most simple
        # decoders, tell() will often just give a byte offset in the file.

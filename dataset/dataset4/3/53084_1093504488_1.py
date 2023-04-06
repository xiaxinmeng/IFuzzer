class BinaryDataCodec(codecs.Codec):

    # Note: Binding these as C functions will result in the class not
    # converting them to methods. This is intended.
    encode = codecs.readbuffer_encode
    decode = codecs.latin_1_decode
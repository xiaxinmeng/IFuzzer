class IncrementalDecoder(codecs.BufferedIncrementalDecoder):
    _buffer_decode = codecs.utf_16_le_decode

class StreamReader(codecs.StreamReader):
    decode = codecs.utf_16_le_decode
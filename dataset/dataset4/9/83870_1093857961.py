for c in [b'\x01', b'\x7f', b'\xff', b'\x0f', b'\xf0']:
    self.assertTrue(struct.unpack('>?', c)[0])
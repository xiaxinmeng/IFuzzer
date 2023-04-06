def chunk(block):
    return b'{0:x}\r\n{1}\r\n'.format(len(block), block)
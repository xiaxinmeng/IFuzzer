self.fp.write(struct.pack("<lLL", zinfo.CRC, zinfo.compress_size,
                 zinfo.file_size))
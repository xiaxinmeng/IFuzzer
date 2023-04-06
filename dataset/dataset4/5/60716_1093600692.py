def test_jpeg(h, f):    
    if (h[6:10] in (b'JFIF', b'Exif')) or (h[:2] == b'\xff\xd8' and (b'JFIF' in h[:32] or b'8BIM' in h[:32])):
        return 'jpeg'
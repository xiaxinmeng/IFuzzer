def test_jpeg(h, f):
    """JPEG data in JFIF or Exif format"""
    if not h.startswith(b'\xff\xd8'):#Test empty files, and incorrect start of file
        return None
    else:
        if f:#if we test a file, test end of jpeg
            f.seek(-2,2)
            if f.read(2).endswith(b'\xff\xd9'):
                return 'jpeg'
        else:#if we just test the header, consider this is a valid jpeg and not test end of file
            return 'jpeg'
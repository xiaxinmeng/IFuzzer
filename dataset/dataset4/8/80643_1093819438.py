def _exam_ratio(self, threshold=10):
    """If the ratio exceeds threshold, it may be a ZIP Bomb."""
    sum_file_size = sum([data.file_size for data in self.filelist])
    sum_compress_size = sum([data.compress_size for data in self.filelist])
    ratio = sum_file_size / sum_compress_size
    if (ratio > threshold):
        raise BadZipFile("Zip Bomb Detected")
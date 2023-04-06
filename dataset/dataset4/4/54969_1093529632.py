def fake_st_size_side_effect(*args, **kwargs):
    src, = args
    stats = stat(src)
    return stat_result((stats.st_mode, stats.st_ino, stats.st_dev, stats.st_nlink,
                       stats.st_uid, stats.st_gid, stats.st_size + 10,
                       stats.st_atime, stats.st_mtime, stats.st_ctime))

class Issue10760TestCase(TestCase):
    def setUp(self):
        fd, self.src = mkstemp()
        write(fd, '\x00' * 4)
        close(fd)
        fd, self.dst = mkstemp()
        close(fd)

    def test(self):
        with patch("os.lstat") as lstat:
            lstat.side_effect = fake_st_size_side_effect
            tar_file = TarFile.open(self.dst, 'w:gz')
            tar_file.add(self.src)
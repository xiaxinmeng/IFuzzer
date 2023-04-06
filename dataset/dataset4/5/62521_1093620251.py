class MyTarVolumeSet(tarfile.TarVolumeSet):

    def __init__(self, template, max_vol_size):
        self.template = template
        self.max_vol_size = max_vol_size

    def new_volume_handler(self, tarfile, volume_number):
        self.open_volume(self.template % volume_number, tarfile)

volumes = MyTarVolumesSet("test.tar.%03d")
with tarfile.open(fileobj=volumes, mode="w:") as tar:
    for t in tar:
        print(t.name)
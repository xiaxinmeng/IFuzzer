class MyTarVolumeSet(tarfile.TarVolumeSet):

    def __init__(self, template):
        self.template = template

    def open_volume(self, volume_number):
        return open(self.template % volume_number, "rb")

volumes = MyTarVolumesSet("test.tar.%03d")
with tarfile.open(fileobj=volumes, mode="r:") as tar:
    for t in tar:
        print(t.name)

def make_whlfile(*args, owner=None, group=None, **kwargs):
    return shutil._make_zipfile(*args, **kwargs)


shutil.register_archive_format("whl", make_whlfile, description="Wheel file")
shutil.register_unpack_format(
    "whl", [".whl"], shutil._unpack_zipfile, description="Wheel file"
)
